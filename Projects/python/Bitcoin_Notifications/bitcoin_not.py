from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time
from datetime import datetime 

# lists of the Top 10 currencies

currency = {1 : {'Indian Rupees' : 'IND'},
            2 : {'Bahrain Dinar':'BHD'},
            3 : {'European Euro':'EUR'},
            4 : {'US dollar':'USD'},
            5 : {'Canadian Dollar':'CAD'},
            6 : {'The japanese yen':'JPY'},
            6 : {'British Pound':'GBP'},
            7 : {'Australian Dollar':'AUD'},
            8 : {'Singapur Dollar':'SGD'},
            9 : {'Malaysian Ringgit':'MYR'},
            10 : {'Chinese Yuan Renminbi':'CNY'}}

for i in currency:
  print(str(i) + ' => ' + currency[i].keys()[0] + ' : ' + currency[i].values()[0])
currency_number = int(input('Enter the number of the currency which bitcoin updates you want from the above list : '))

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
ifttt_webhook_url = 'https://maker.ifttt.com/trigger/{}/with/key/dFIVd-edQhhaMH92WWSjTE'
parameters = {
  'start':'1',
  'limit':'1',
  'convert':''
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'bb430795-0012-4d92-825c-4df179b810ee',
}


parameters['convert'] = currency[currency_number].values()[0]
print('You choose ' + parameters['convert'] + ' Currency')



session = Session()
session.headers.update(headers)


def bitcoin_price_notifications():
  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    price = data['data'][0]['quote'][parameters['convert']]['price']
    print(price)
    return float(price)

  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

def post_ifttt_webhook(event,value):
  data = {'value1': value}
  ifttt_event_url = ifttt_webhook_url.format(event)
  session.post(ifttt_event_url,json = data)

# post_ifttt_webhook('bitcoin_price_emergency',Bitcoin_price_notifications)
BITCOIN_PRICE_THRESHOLD = 6000
def format_bitcoin_history(bitcoin_history):
  rows = []
  for bitcoin_price in bitcoin_history:
      # Formats the date into a string: '24.02.2018 15:09'
      date = bitcoin_price['date'].strftime('%d.%m.%Y %H:%M')
      price = bitcoin_price['price']
      # <b> (bold) tag creates bolded text
      # 24.02.2018 15:09: $<b>10123.4</b>
      row = '{}: $<b>{}</b>'.format(date, price)
      rows.append(row)
  return '<br>'.join(rows)

def main():
    bitcoin_history = []
    while True:
        price = bitcoin_price_notifications()
        date = datetime.now()
        bitcoin_history.append({'date': date, 'price': price})

        # Send an emergency notification
        if price < BITCOIN_PRICE_THRESHOLD:
            post_ifttt_webhook('bitcoin_price_emergency', price)

        # Send a Telegram notification
        # Once we have 5 items in our bitcoin_history send an update
        if len(bitcoin_history) == 5 :
            post_ifttt_webhook('bitcoin_price_update',format_bitcoin_history(bitcoin_history))
            print('BITCOIN PRICE UPDATES SENT TO YOUR TELEGRAM')
            # Reset the history
            bitcoin_history = []

        # Sleep for 5 minutes 
        # (For testing purposes you can set it to a lower number)
        time.sleep(60)

if __name__ == '__main__':
  main()