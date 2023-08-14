# twingate
requirements https://gist.github.com/ekampf/3b26db03b30f7e7b1aa6162c81017675



I used Python to implement the Memory manger and below are my assumptions and notes:


1) MemoryManger class initiated with the size of the memory buffer
2) the Memory buffer implemented as dictionary that describes the memory status while the dictionary key is the buffer index and the value is the memory value.
3) I used Dictionary for memory buffer since it is very effective to ready bytes by index and no need to iterate on the whole memory to find the related  bytes.
4) Dictionary is effective in memory wise since no need to allocate memory for empty cells 


Functions:

_save_single_byte: get a single byte and save it in the first free index in the memory buffer

alloc : verifies that there is enough room to save it and for each byte save by "_save_single_byte" function 
        collects for each byte it index in the memory buffer  and returns it in save_block dictionary 

        

free: takes list of index and deletes them from memory buffer dictionary 


read: takes save_block and return the data stored 
