/*
Question - 1 

Create a function to concatenate two integer arrays.
Examples
concat([1, 3, 5], [2, 6, 8]) ➞ [1, 3, 5, 2, 6, 8]

concat([7, 8], [10, 9, 1, 1, 2]) ➞ [7, 8, 10, 9, 1, 1, 2]

concat([4, 5, 1], [3, 3, 3, 3, 3]) ➞ [4, 5, 1, 3, 3, 3, 3, 3]
*/
const concat = (arr1,arr2)=>{
    let arr3 = arr1.concat(arr2);
    return arr3;
};
console.log(concat([1, 3, 5], [2, 6, 8]));
console.log(concat([7, 8], [10, 9, 1, 1, 2]));
console.log(concat([4, 5, 1], [3, 3, 3, 3, 3]));


/*
Question - 2

Create a function that takes an array and a string as arguments and return the index of the string.
Examples
findIndex(["hi", "edabit", "fgh", "abc"], "fgh") ➞ 2

findIndex(["Red", "blue", "Blue", "Green"], "blue") ➞ 1

findIndex(["a", "g", "y", "d"], "d") ➞ 3

findIndex(["Pineapple", "Orange", "Grape", "Apple"], "Pineapple") ➞ 0
*/
const findIndex  = (arr1,element)=>{
    let ind = arr1.indexOf(element);
    return ind;
};
console.log(findIndex(["Red", "blue", "Blue", "Green"], "blue"));

console.log(findIndex(["a", "g", "y", "d"], "d"));

console.log(findIndex(["Pineapple", "Orange", "Grape", "Apple"], "Pineapple"));

/*
Question - 3

Write a function to check if an array contains a particular number.
Examples
check([1, 2, 3, 4, 5], 3) ➞ true

check([1, 1, 2, 1, 1], 3) ➞ false

check([5, 5, 5, 6], 5) ➞ true

check([], 5) ➞ false
*/
const check = (arr1,num)=>{
    var n  = 0;
    for(let i in arr1){
        n = arr1[i];
        if(num == n){
            return true;
        }
    }
    return false;
};
console.log(check([1, 2, 3, 4, 5], 3));

console.log(check([1, 1, 2, 1, 1], 3));

console.log(check([5, 5, 5, 6], 5));

console.log(check([], 5));


/*
Question - 4

Create a function that takes an object argument sizes (contains width, length, height keys) and returns the volume of the box.
Examples
volumeOfBox({ width: 2, length: 5, height: 1 }) ➞ 10

volumeOfBox({ width: 4, length: 2, height: 2 }) ➞ 16

volumeOfBox({ width: 2, length: 3, height: 5 }) ➞ 30
*/

const volumeOfBox = (obj) =>{
    return Object.values(obj).reduce((a,b)=>a*b);
};
console.log(volumeOfBox({ width: 2, length: 5, height: 1 }));
console.log(volumeOfBox({ width: 4, length: 2, height: 2 }));
console.log(volumeOfBox({ width: 2, length: 3, height: 5 }));