from array import *

arr=array('i',[])

n=int(input("Enter length of array"))

for i in range(n):
    x=int(input("Enter next element of array"))
    arr.append(x)

search=int(input("Enter  element to be searched"))

ind=0

for ele in arr:
    if ele==search:
        print(f"Element is present as {ind}")
        break
    ind+=1  
