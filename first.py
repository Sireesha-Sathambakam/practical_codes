# 1 . SWAP 2 NUMBERS WITH TEMP VARIABLE

n1 = 10
n2 = 20
temp = n1
n1 = n2 
n2 = temp
print("n1",n1,n2)

# 2 . swap 2 numbers without temp variable 

num1 = 10
num2 = 20
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print("num1",num1,num2)

# 3 . prime or not

num = int(input())
count = 0
for i in range(1,num+1):
    if num % i == 0:
        count += 1
if count == 2:
    print("its is a prime number")
else :
    print("it is not a prime number")

str = "hi hello welcome to big boss"
str1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
count = 0
for i in str:
    if i not in str1:
        count += 1
print (count)

a = [1,2,3,4,5,6,7,8,9,10]
b=[]
for i in a:
    if i % 2 == 0:
        b.append(i)
print(b)

n1 = int(input())
n2 = int(input())
prime = []
for i in range(n1,n2+1):
    if i > 1:
        is_prime = True
        for j in range(2,int(i ** 0.5)+1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime.append(i) 
print(prime)

num_1 = int(input())
num_2 = int(input())
prime = []
for i in range(num_1,num_2+1):
    c=0
    for j in range(2,(i//2+1)):
        if i % j == 0:
            c += 1
            break
    if c==0 and i!=1:
        prime.append(i)
print(prime)

# print("hello")
rows = int(input())
for i in range(1,rows+1):
    print("" * (rows-i),end="")
    print("*" * i)

for s in range(3):
    for q in range(4):
        print("*" ,end= "")
    print()