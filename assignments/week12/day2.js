// Questions

// 1- Implement enqueue and dequeue using only two stacks.
// solution:-

const stack1 = [];
const stack2 = [];


function Enqueue(value) {
    if(stack1.length){
        stack1.push(value)
    }else{
        return 'Overflow Condition'
    }
}

function Dequeue() {
    if(stack2 == 0) {
        if(stack1 == 0) {
            return "Underflow Condition"
        }
        while(stack1.length>0) {
            stack2.push(stack1.pop());
        }
    }
    return stack2.pop()
}

Enqueue('a');
Enqueue('b');
Enqueue('c');
Dequeue('c');
//console.log(stack2)


// 2- Write a function fib() that takes an integer n and return the nth Fibonacci number.
// solution

function fib(n) {
    if (n < 2) return n;

    return fib(n - 1) + fib(n - 2);
}
console.log(fib(9))