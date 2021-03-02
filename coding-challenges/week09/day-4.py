'''
Ques:- What are the valid deadlock prevention schemes?
'''
'''
Answer:-
There are four deadlock prevention conditions:
- Mutual exclusion condition means that no process will have exclusive access to a resource.
- The hold and wait or resource holding conditions may be removed by requiring the processes to request all the resources they will need before starting up (or before embarking upon a particular set of operations).
- The no preemption condition is difficult or impossible to avoid as a process has to be able to have a resource for a certain amount of time, or the processing outcome may be inconsistent or thrashing may occur.
- Circular wait condition avoids the circular waits include disabling interrupts during critical sections and using a hierarchy to determine a partial ordering of resources.
'''