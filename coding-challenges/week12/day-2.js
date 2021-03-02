// Questions:-
/*
1- Write a function to remove duplicates from an array.

Sample input- [1,2,3,4,3,2,1]
Sample output - [1,2,3,4]
*/
// solution:- 
array = [1,2,3,10,16,18,5,6,7,8,10,4,3,2,16,5,6,18,7,1]

var indexPtr = 0
var iteratingPtr = 0

while(indexPtr < array.length) {
    iteratingPtr = indexPtr+1;
    while(iteratingPtr < array.length) {
        if(array[indexPtr] == array[iteratingPtr]) {
            array.splice(iteratingPtr,1)
        }iteratingPtr++
    }indexPtr++
}

console.log(array)



/*
2- Given two strings, return true if they are anagrams of one another
 
	For example: Mary is an anagram of Army
*/
// solution:-

function checkAnagram( str1,str2 ) {

    str1 = str1.replace(/ /g,"").toLowerCase();
    str2 = str2.replace(/ /g,"").toLowerCase();

    arr1 = str1.split("");
    arr2 = str2.split("");

    arr1.sort();
    arr2.sort();

    var _str1 = "";
    var _str2 = "";

    arr1.forEach(element => _str1+=element);
    arr2.forEach(element => _str2+=element);

    if(_str1 == _str2) {
        return 'Given strings were anagram.';
    } else {
        return 'Given strings were not anagram.';
    }
}

console.log(checkAnagram('Li s ten', 'Si le nt'))

