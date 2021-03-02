/*
Question - 1

Create a function that returns only strings with unique characters.
Examples
filterUnique(["abb", "abc", "abcdb", "aea", "bbb"]) ➞ ["abc"]
// "b" occurs in "abb" more than once, "b" occurs in "abcdb" more than once, etc.

filterUnique(["88", "999", "989", "9988", "9898"]) ➞ []

filterUnique(["ABCDE", "DDEB", "BED", "CCA", "BAC"]) ➞ ["ABCDE", "BED", "BAC"]
*/



function uniqueCharac(arr){
    var count = 0;
    var arr1 = [];
    var count1 = 0;
    arr.forEach(str => {
        for (var i = 0 ; i< str.length ; i++){
            for(var j = 0;j<str.length;j++ ){
                if(str[i]==str[j]){
                    count++;
                }
            }
            if (count > 1 && i < str.length){
                i=i+1;
            }else{
                count1++;
            }
            count = 0;
        }
        if(count1 == str.length){
            arr1.push(str);
        }
        count1 = 0;
    });
    return arr1;
}
console.log(uniqueCharac(["ABCDE", "DDEB", "BED", "CCA", "BAC"]));
console.log(uniqueCharac(["88", "999", "989", "9988", "9898"]));
console.log(uniqueCharac(["abb", "abc", "abcdb", "aea", "bbb"]));




/*
Question - 2

Create a function that takes two numbers as arguments (num, length) and returns an array of multiples of num up to length.
Examples
arrayOfMultiples(7, 5) ➞ [7, 14, 21, 28, 35]

arrayOfMultiples(12, 10) ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

arrayOfMultiples(17, 6) ➞ [17, 34, 51, 68, 85, 102]
*/


const arrayOfMultiples = (num,len) =>{
    var arr = [];
    var i = 1;
    while (arr.length < len){
        arr.push(num*i);
        i++;
    }
    return arr;
};
console.log(arrayOfMultiples(12,10));
console.log(arrayOfMultiples(17, 6));
console.log(arrayOfMultiples(7, 5));


/*
Question - 3

Create a function that takes an object and returns the keys and values as separate arrays.
Examples
keysAndValues({ a: 1, b: 2, c: 3 })
➞ [["a", "b", "c"], [1, 2, 3]]

keysAndValues({ a: "Apple", b: "Microsoft", c: "Google" })
➞ [["a", "b", "c"], ["Apple", "Microsoft", "Google"]]
*/

// { a: 1, b: 2, c: 3 };
// { a: "Apple", b: "Microsoft", c: "Google" }
const keysAndValues = (obj)=>{
    arr = [];
    arr.push(Object.keys(obj));
    arr.push(Object.values(obj));
    return arr;
};
console.log(keysAndValues({ a: "Apple", b: "Microsoft", c: "Google" }));
console.log(keysAndValues({ a: 1, b: 2, c: 3 }));

