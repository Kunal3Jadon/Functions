from math import *
#1..WAP to merge two lists using function
def merge(l1,l2):
    l3=l1+l2
    print(l3)
l1=list(eval(input()))
l2=list(eval(input()))
merge(l1,l2)
#2..WAP to merge two dictionaries using function
def merg(d1,d2):
    d1.update(d2)
    print(d1)
n=int(input())
d1={}
for i in range(n):
    key=input()
    value=int(input())
    d1.update({key:value})
n1=int(input())
d2={}
for i in range(n1):
    key=input()
    value=int(input())
    d2.update({key:value})
merg(d1,d2)
#3..WAP to check whether no is strong number or not using function
def strong(n):
    s=n
    p=0
    while(n>0):
       rem=n%10
       p+=factorial(rem)
       n=n//10
    if s==p:
        print("strong number")
    else:
        print("not strong number")
n=int(input())
strong(n)
#4..WAP to check no is perfect no or not using function
def perfect(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    if s==n:
        print("perfect")
    else:
        print("not perfect")
n=int(input())
perfect(n)
#5..WAP to reverse a number using function
def reverse(n):
    s=0
    while(n>0):
        rem=n%10
        s=s*10+rem
        n=n//10
    print(s)
n=int(input())
reverse(n)
#6..WAP to reverse a string using function
def string(s):
    print(s[::-1])
s=input()
string(s)
#7..WAP to check string is palindrome or not using python
def palindrome(s):
    s1=s[::-1]
    if s==s1:
        print("string is palindrome")
    else:
        print("not palindrome")
s=input()
palindrome(s)
#8..WAP to print sum of elements of list using function
def list(l):
    s=0
    for i in l:
        s+=i
    print(s)
l=list(eval(input()))
list(l)
        
