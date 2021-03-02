/*
1- Write a Javascript function that takes an array and a value and search that value in the array.
    a.Function should take two arguments - an array and a value to search inside the array.

    b.If the element is found, the function should return the position of the element in an array.

    c.If the element is not found, the function should return "-1".

*/
var arr = []
value = prompt("Enter the number: ")
function array_search(arr,value){
    for(var i = 0;i<arr.length;i++){
        if (arr[i]==value){
            return i
        }else{
            return -1
        }
    }
}
array_search(arr,value)
/*
2 - Write a Javascript program that prints multiplication table of 5 upto 10.
 
The output should show:
1 * 5 = 5
2 * 5 = 10
.
.
.
10 * 5 = 50

*/
var num; 
function table_multiply(num){
    for (var i = 0;i<11;i++){
        var table_of = num * i;
        (num>5) ? console.log(`${i} * ${num} = ${table_of}`): "Use the table more than 5"
        };
};
table_multiply(7)
