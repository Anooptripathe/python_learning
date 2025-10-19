from functools import reduce

f= lambda a,b:a+b
result=f(10,12)
print(result)

nums=[3,4,7,8,10,6]

even_nums=list(filter(lambda a:a%2==0,nums))
print(even_nums)

even_map=list(map(lambda n:n*2,even_nums))

sum=reduce(lambda a,b:a+b,even_map)
print(sum)