/*
Return the lowest index at which a value (second argument) should be inserted into an array (first argument) once it has been sorted. The returned value should be a number.

For example, getIndexToIns([1, 2, 3, 4], 1.5) should return 1 because it is greater than 1 (which has index 0), but less than 2 (which has index 1).
Likewise, getIndexToIns([20, 3, 5], 19) should return 2 because once the array has been sorted it will look like [3, 5, 20] and 19 is less than 20 (index 2) and greater than 5 (index 1).
*/

// let arr  = [20, 3, 5];
// let value = 1.5;

const getIndexToIns = (arr,value)=>{
    var ind = 0;
    arr = arr.sort(function(a, b){return a - b;});
    for(var i = 0; i<arr.length-1;i++){
        if (value > arr[i] && value < arr[i+1]){
            return i+1;
        }
    }
};
console.log(getIndexToIns([20, 3, 5],19));
console.log(getIndexToIns([1, 2, 3, 4], 1.5));

/*
Question - 2
Write a function that takes an integer minutes and converts it to seconds.
Examples
convert(5) ➞ 300
convert(3) ➞ 180
convert(2) ➞ 120
*/

const convert = (min) =>{
    return min*60;
};
console.log(convert(5));
console.log(convert(2));
console.log(convert(3));




/*
Question - 3
Create a function that takes two numbers as arguments and return their sum.
Examples -- addition(3, 2) ➞ 5
addition(-3, -6) ➞ -9
addition(7, 3) ➞ 10
*/

const addition = (int1,int2) =>{
    return int1+int2;
};
console.log(addition(-3, -6));
console.log(addition(7, 3));

