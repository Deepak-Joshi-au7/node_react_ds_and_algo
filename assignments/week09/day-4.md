'''
Ques. Consider a machine with 64 MB physical memory and a 32-bit virtual address space. If the page size is 4KB, what is the approximate size of the page table?
'''
Answer:-

2 MB

A page entry is used to get address of physical memory.
Here we assume that single level of Paging is happening.
So the resulting page table will contain entries for all the pages of the Virtual
address space.

Number of entries in page table = (Virtual address space size) / (page size)

Using above formula we can say that there will be 2 ^ (32-12) = 2^20 entries
in page table.
No. of bits required to address the 64MB Physical memory = 26.
So there will be 2^(26-12) = 2^14 page frames in the physical memory.
And page table needs to store the address of all these 2^14 page frames.
Therefore, each page table entry will contain 14 bits address of the page frame
and 1 bit for valid-invalid bit.
Since memory is byte addressable. So we take that each page table entry is 16
bits i.e. 2 bytes long.