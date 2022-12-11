# print('Hello World')
# int_list = [4, 8, -2, 10, 5]
# sum = 0
# for num in int_list:
#     sum += num
# print("Answer is : ", sum)

# mul = 9
# cntr = 1

# while cntr<= 10:
#     print(mul," * ",cntr," = ",mul*cntr)
#     cntr += 1

# a = 1
# b = 1
# print(id(a))
# print(id(b))

# List1 = [3,4,5]
# List2 = [3,4,5]
# print(id(List1))
# print(id(List2))


# print mixed string from a String
# str1 = 'Hello'
# str2 = 'World'
# rstr = ''

# if len(str1) == len(str2):
#     for i in range(len(str1)):
#         rstr += str1[i] + str2[i]
# print("result : ", rstr)


# num = int(input("Enter a number to check whether it is a even or odd \n"))
# if(num % 2 == 0):
#     print('Its..Even')
# else:
#     print("It's Odd")

#voting 
# age = int(input("Enter Your age\n"))
# if age >= 18:
#     print("I can vote")
# else:
#     print("I can't vote")

# numbers = [12, 75, 150, 180, 145, 525, 50]
# sum = 0

# for i in numbers:
#     sum += i

# print(sum)

# numbers = input("Enter 3 numbers\n").split()
# max = 0 
# for i in numbers:
#     if max < int(i):
#         max  = int(i)
# print(max)

numbers = [12, 75, 150, 180, 145, 525, 50]

# for i in numbers:
#     if i > 500:
#         break
#     elif i > 150:
#         continue
#     elif i % 5 == 0:
#         print(i)

print(numbers[-1:len(numbers)-3:-1])