#Write a function to find the factorial of a number
#if given number is 3 then it should work like 3*2*1 = 6
#input = 3
#expected output = 6f

def factorial(num):
    fact = 1
    if(num == 0 or num == 1):
        return fact
    for i in range(1,num+1):
        fact *= i
    return fact

print(factorial(1))

print('-*'*70)
a,b,c = 2,3,5
print(a)
print(b)
print(c)
print('-*'*70)

def sqr_cube(num):
    return num*num, num*num*num

print(type(sqr_cube(5)))

square, root = sqr_cube(5)
print("Square",square)
print("Root",root)

print('-*'*70)

def info_print(**kwargs):
    print(kwargs['name'])

info_print(age = 12, name =  "naveen")

print('-*'*70)

