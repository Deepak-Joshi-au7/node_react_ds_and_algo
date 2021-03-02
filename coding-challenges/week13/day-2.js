/*
Question - 1

The FizzBuzz challenge goes something like this. Write a function that does the following:
console logs the numbers from 1 to n, where n is the integer the function takes as its parameter
logs fizz instead of the number for multiples of 3
logs buzz instead of the number for multiples of 5
logs fizzbuzz for numbers that are multiples of both 3 and 5
*/

const FizzBuzz = (n) =>{
    arrN = [];
    multiplesOf3 = [];
    multiplesOf5 = [];
    commonMultiplesOfBoth = [];
    for(let i=1; i<n ; i++){
        arrN.push(i);
        multiplesOf3.push(i*3);
        multiplesOf5.push(i*5);
    }
    for(let i = 0;i<multiplesOf3.length;i++){
        for(let j = 0;j< multiplesOf5.length;j++){
            if(multiplesOf3[i]==multiplesOf5[j]){
                commonMultiplesOfBoth.push(multiplesOf3[i]);
            }
        }
    }
    console.log(multiplesOf3);
    console.log(multiplesOf5);
    console.log(commonMultiplesOfBoth);
    return(commonMultiplesOfBoth);
};

FizzBuzz(10);


/*
Question - 2
A word is an anagram of another word if both use the same letters in the same quantity, but arranged differently.
Understanding the challenge

You can state this challenge in the following terms: write a function that checks if two provided strings are anagrams of each other; letter casing shouldn’t matter. Also, consider only characters, not spaces or punctuation. For example:
anagram('finder', 'Friend')  --> true
anagram('hello', 'bye') --> false
*/
const anagram = (word1,word2)=>{
    count = 0;
    for (let i in word1){
        for(let j in word2){
            if (i === j){
                count++;
            }
        }
    }
    var result = (count == word2.length && count == word1.length) ? true : false ;
    return result;
};
console.log(anagram('finder', 'Friend'));
console.log(anagram('hello', 'bye'));




/*
Question - 3
Find the Vowels
This is probably one of the less challenging challenges (no pun intended) — in terms of difficulty — but that doesn’t detract from the fact that you could come across it during a job interview. It goes like this.
Understanding the challenge
You can state the vowels challenge as follows: write a function that takes a string as argument and returns the number of vowels contained in that string.
The vowels are “a”, “e”, “i”, “o”, “u”.
Examples:
findVowels('hello') // --> 2
findVowels('why') // --> 0
*/
const findVowels = (str)=>{
    let vowels = ["a","e","i","o","u"];
    str = str.toLowerCase();
    count = 0;
    for(let i in vowels){
        for(let j in str){
            if(vowels[i] === str[j])
                count++;
        }
    }
    return count;
};
console.log(findVowels('HelLo'));
console.log(findVowels('WhY'));