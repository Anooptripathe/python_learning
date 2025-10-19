def person(name,age):
    print(name)
    print(age)

person(age=26,name='Anoop')  # keyword Arguments

# Varible length arguments
def sum(a,*b):  # *b act as tuple
    c=a
    for i in b:
        c=i+c
    print(c)
sum(5,8,9,13,51)

# keyword variable length argument
def person(name,**args): #  ** means variable length argument is available with keyword
    print(name)
    for i,j in args.items():
        print(i,j)

person(name='Anoop',age=26,city='Siwan',Profile='Xyz')


