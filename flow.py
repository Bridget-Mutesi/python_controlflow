#Write a function that uses while, if and continue statements 
#to print all the even numbers between 0 and 50. 
def even_numbers():
    z = 0
    while z<50:
        z+=1
        if z % 2!=0:
            continue
        print(z)

#Write a function that takes an integer argument and prints "Prime" 
#if the number is prime, and "Not prime" if the number is not prime. 
def find_prime(n):
    if n<=2:
        print("NOT PRIME")
    for i in range(2,n):
        if n%2==0:
            print("NOT PRIME")
        else:
            print("PRIME")

#Write a function that takes a list of integers as input and prints 
#the sum of all the even numbers in the list.
# def list_integers():
# num =[2,4,6,8,7,5]
def list_of_integers(num):
    sum = 0
    for i in num:
        if i%2==0:
            sum+=i
    print(sum)


#Write a function that takes any two integers as input,
#and prints the sum of all the numbers between the two 
#integers (inclusive) that are divisible by 3.
def divisible_by_three(n1,n2):
    sum = 0
    for x in range(n1,n2+1):
        if x%3==0:
            sum+=1
    print(sum)


