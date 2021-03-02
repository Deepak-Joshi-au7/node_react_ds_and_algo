/*
1- Write a Javascript program that produces a star pattern likes this.
*
**
***
****
*****
****
***
**
*
*/
var rows = 5;
for (i=1; i<rows+1; i++){
    let str = "";
    for (j=1; j<=i; j++){
        str += '*'
    }
    console.log(str);
};

for(i = rows-1; i>0; i--){
    let str = "";
    for (j=0; j<i; j++){
        str+='*'
    };
    console.log(str)
};
/*
2- Write javascript program for following conditions:
1. A function  evenFunction() that returns if a number is even or not.
*/
var num =  
function evenFunction(num){
    if (num % 2 == 0){
        return "This number is Even";
    }
    else{
        return "Number is not Even";
    }
}

// 2. A function oddFunction() that returns if a number is odd or not.
var num = prompt("Enter the Number: ");
function oddFunction(num){
    if (num % 2 == 0){
        console.log("This number is Even");
        return "This number is Even";
    }
    else{
        console.log("Number is not Even");
        return "Number is not Even";
    }
}
oddFunction(num)
// 3. A function squareFunction() that returns if a number is square or not.
var num;
function sqRoot(num){
    for (var i = 1;i<num/2;i++){
        if (i*i == num){
            console.log(`${num} is squareRoot of ${i}`);
        }
        else {
            console.log( `${num} is not a sqRoot`) 
        };
    }
}
sqRoot(25)