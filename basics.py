your_age=input("Enter your age:")
years=int(your_age)
months=years*12
print(f" your age {years} , is equal to {months}.")

set
x={"nitin","vishal","lalit"}
y={"nitin","vishal"}

res=x.difference(y)
res2=x.intersection(y)
x.union(y)#
# intersection
print(res2)

if not 1 in[10,20] and 1<2:
    print(1)
else:
    print()

# if Else
# loop
# list comprehension

# it allows create a list from existing one and returns a new list

num =[1,2,3,4,5]
doubl=[]

for n in num:
    
    doubl.append(n*2)

print(doubl)

x=[n*2 for n in num]
print(x)

# map function
def doub(x):
    return x*2

x1=[5,6,87,8]
lis_double=[doub(x) for x in x1]
doubled=list(map(doub, x1))
doubled2=list(map(lambda x:x*2 , x1))
print(lis_double)
print(doubled)
print(doubled2)

# disctionary comp

# unpacking arguments

def mult(*args):
    print(args)
    total=1
    for arg in args:
        total=total*arg
    return total

print(mult(1,2,3,4))
print(mult(-1))


from os import name


list1 = [11, 5, 17, 18, 23, 50]
for ele in list1:
    if ele % 2 == 0:
        list1.remove(ele)
    
print("New list after removing all even numbers: ", list1)

del list1[1:5]
print(*list1)

#unpacking keyword arguments

def named(name,age):
    print(name,age)

details={"name":"Nitin","age":28}
named(**details)

def named(**kwargs):
    print(kwargs)

# details={"name":"Nitin","age":28}
# named(**details)

def print_nicely(**kwargs):
    named(**kwargs)
    for key,values in kwargs.items():
        print(f"{key}:{values}")
    
print_nicely(name="nitin", age=27)

#args and kwargs 

def both(*args,**kwargs):
    print(args)
    print(kwargs)


both(1,2,3, name="nitin", agr=26)


