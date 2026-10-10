'''n = int(input())
if n%3==0 and n%5==0:
    print("both divisible")
elif n%5==0:
    print("only divisible by 5")
elif n%3==0:
     print("only divisible by 3")
else:
    print("not divisible by either 5 or 3")'''



'''''n= int(input())
if n==2:
    print(" 28 or 29 days")
elif n==4 or n==6 or n==9 or n==11:
    print("30 days")
elif n>=1 and n<=12:
    print("31 days")
else:
    print("invalid month")'''''




# For loop:
'''for i in range(10):
    print(f"iteration:{i+1}")
    a=(input())
    print(a)'''


'''# sequence range
for i in range(22,11,-4):
    print(i,end=" ")
'''


#for loops:
'''n=int(input())       #123
c=0                  #c=0
for i in str(n):     # i in str(123)
     c=c+1           #0=0+1=1
print(c)             #123
                     #3
'''

# sum of digit(for loop)
'''n=input()
s=0
for i in n:
    s=s+int(i)    
print(s)
'''

#factiorial of nmber:
'''n=int(input())
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)   
'''

# print 5 table:
'''n =int(input())
for i in range (1,11):
    print("%d x %2d = %2d"%(n,i,n*i))
'''

# check prime number or not

'''n=int(input())
c=0
for i in range(1,n+1):
   if n%i==0:
      c=c+1 
if c==2:
    print("prime number")
else:
    print("not a primenumber")
'''

# While loop:

'''i=1
while i<=10:
    print(i)
    i=i+1
'''

'''i=1
while i:
    print(i,end=" ")
    i=i+1
'''

# reverse order:
'''i=5                            #5
while i>=1:                    # 5>=1
    print(i)                   #print(5)
    i=i-1                      #i=5-1
                               #5 4 3 2 1
'''
'''i=10
while i>=1:
       print(i,end=" ")
       i=i-1
'''
'''while True:
    print(5,end=" ")
'''
'''i=1
while True:
    print(i)
    if i==10:
        break
    i=i+1
'''

# number jumbling:
'''n=int(input())               #123
rev=0                           # rev=0
while n!=0:                     #while 123!=0
       a=n%10                    #a=123%10
      rev=rev*10+a              #rev=rev*10+a
      n=n//10                   #n=23//10
print(rev)                      # rev
                                #321
'''


# Palindrome:
'''n=int(input())
tem=n
rev=0
while n!=0:
        d=n%10
        rev=rev*10+d
        n=n//10
if rev==tem:
        print("palindrome")
else:
    print("not a palindrome")
'''

# check prime number using while loop:
'''n=int(input())
i=1
c=0
while i<=n:
      if n%i==0:
          c=c+1
      i=i+1
if c==2:
    print("prime number")
else:
    print("not a prime number")
'''
# check perfect number:
'''n=int(input())
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if n==sum:
    print("perfect number")
else:
    print("not a perfect number")
'''
       
# check perfect number(while loop):
'''n=int(input())
i=1
sum=0
while i<n:
       if n%i==0:
           sum=sum+i
       i=i+1
if n==sum:
    print("perfect number")
else:
    print("not a perfect number")
'''

# fibnacci series(for loop):
'''a=0
b=1
for i in range(5):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
'''
# fibnacci series(while loop):
'''i=1
n=int(input())
a=0
b=1
while i<=n:
    print(a,end=" ")
    a,b=b,a+b
    i=i+1
'''
# count even and odd digits in a 6 digit number:
'''n=int(input())
even=0
odd=0
while n>0:
    d=n%10
    if d%2==0:
        even=even+1
    else:
         odd=odd+1
    n=n//10
print("even:",even)
print("odd:",odd)
'''                 


# print columuns and rows:
'''for i in range(1,5):
    for j in range(4):
        print("*",end=" ")
    print()
 '''
# increasing star:
'''for i in range(4):
    for j in range(i+1):
        print("*",end=" ")
    print()   
'''
#Decreasing stars:
'''for i in range(6):
    for j in range(6-i):
        print("*",end=" ")
    print()    
'''
#reverse stars:
'''n=5
for i in range(1,n):
    for s in range(n-i):
        print(" ",end="  ")
    for j in range(i):
        print("*",end="  ")
    print()    
'''


# rows stars:
'''for i in range(1,5):
    for j in range(4):
        print("*",end=" ")
    print()    
'''
# pyrmid star:
'''n=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="  ")
    for  s in range(2*i-1):
        print("*",end="  ")
    print()
'''

# reverse pyrmid
'''n=int(input())
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="  ")
    for  s in range(2*i-1):
        print("*",end="  ")
    print()
'''

# using only single loop:
'''n=7
for i in range(1,n+1):
      print(" "*(n-i)+"*"*(2*i-1))
'''

#both in one frame:
'''n=7
for i in range(1,n+1):
      print(" "*(n-i)+"*"*(2*i-1))
for j in range(n-1,0,-1):
       print(" "*(n-j)+"*"*(2*j-1))
             
'''

#both triangle are mixing:
'''n=4
for i in range(1,n+1):
    for j in range(i):
          print("*",end=" ")
    for k in range(2*(n-i)):
          print(" ",end=" ")
    for k in range(i):
          print("*",end=" ")
    print()
'''

# print numbers:
'''for i in range(1,5):
    for j in range(1,6):
        print(j,end=" ")
    print()
'''
# print numbers:
'''for i in range(1,5):
    for j in range(1,6):
        print(j,end=" ")
    print()
'''
#print numbers :
'''n=int(input())
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
'''
# print number:
'''n=int(input())
for i in range(1,5):
    for j in range(n-1,0,-1):
        print(j,end=" ")
    print()
'''
#print number:
'''n=7
for i in range(1,5):
    for j in range(1,i-1):
        print(j,end=" ")
    print()
'''
# print repeated number triangle:
'''n=5
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()    
'''
#  print increasing number triangle:
'''n=5
for i in range(1,n+1):
       for j in range(1,i+1):
           print(j,end=" ")
       print()    
'''
#  print inverted number triangle:
'''n=7
for i in range(1,n):
       for j in range(1,n-i):
           print(j,end=" ")
       print()    
'''
# reverse number triangle:
'''n=5
for i in range(1,n+1):
       for j in range(i,n+1):
           print(j,end=" ")
       print()   

'''
#floyd's:
'''n=int(input())
num=1
for i in range(1,n+1):
       for j in range(1,i+1):
           print(num,end=" ")
           num +=1
     print()

'''
# use break:
'''for i in range(1,11):
       print(i)
       if i==9:
        break
else:
       print("Loop completed Sucessfully")

'''
# use continue:
'''for i in range(1,11):
       print(i)
       if i==9:
        continue
else:
       print("Loop completed Sucessfully")
'''
# print name:
'''for i in range(5):
       print("vijji")
       if i==3:
             continue
else:
       print("pooji")
'''
# use break :
'''for i in range(5):
       print("vijji")
       if i==3:
             break
else:
       print("pooji")
'''
# print P:
'''print("@  @ @ @ @")
print("@           @")
print("@ @ @ @ @ ")
print("@")
print("@")
print("@")
print("@")
'''
# print v:
'''
print(" @       @")
print(" @      @ ")
print(" @     @")
print("  @   @   ")
print("    @")
'''

#else statement used with Lopps:
'''count = 0
while count< 10:
       print(f"Current count: {count}")
       count =count+1
else:
       print("Loop completed Sucessfully")
'''
#else statement used with Lopps:
'''count = 0
while count< 10:
       print(f"Current count: {count}")
       count =count+1
       if count>5:
              break
else:
       print("Loop completed Sucessfully")
'''
# print Square:
'''n=7
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
             print("*",end="")
        else:
            print(end=" ")
    print()
'''
# print square model2:
'''n=int(input())
for i in range(1,n+1):
     for j in range(1,n+1):
         if i==1 or j==1 or i==n or j==n:
             print("*",end=" ")
         else:
             print(" ",end=" ")
     print()   
'''                                             
# print  alloy triangle:
'''n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or i==n or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
# print  alloy reverse triangle:
'''n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==n or j==n or i+j==n+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
# print  alloy square with diagonals model:
'''n=int(input())
for i in range(1,n+1):
     for j in range(1,n+1):
         if i==1 or j==1 or i==n or j==n or i+j==n+1 or i==j:
             print("*",end=" ")
         else:
             print(" ",end=" ")
     print()   
'''
#print names with triangles:-
'''n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==n or j==n or i+j==n+1:
            print("v",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#String:-
'''s= 'vijaya lakshmi'
print(s[0])
print(s[13])
'''
# reverse name:
'''s= 'vijaya lakshmi'
print(s[0])
print(s[-13])
'''
#half name using slice:-
'''s= 'vijaya lakshmi'
print(s[0:6])
'''
#String full name:-
'''s= 'vijaya lakshmi'
print(s[0])
print(s[2])
print(s[3])
print(s[4])
print(s[5])
print(s[6])
print(s[7])
print(s[8])
print(s[9])
print(s[10])
print(s[11])
print(s[12])
print(s[13])
print(s[0:13])
print(s[0:6])
print(s[7:14])
print(s[0:7_14])
'''
# string format :-(start,st0p,step):
'''s='vijaya lakshmi'
print(s[0:14:2])
'''
#string format :-(start,st0p,step):
'''s='vijaya lakshmi'
print(s[-7:])
'''
#string format :-(start,st0p,step):
'''s='vijaya lakshmi'
print(s[-7:-1])
'''
#reverse string:-
'''s='python programming'
print(s[14:7:-1])
s='python programming'
print(s[6:2:-1])
'''
# print invidual(loop in string):-
'''s='python'
for i in s:
    print(i)

# print
s="python"
n=len(s)
for i in range(n):
    print(s[i],end=" ")
'''
# find character:
'''n=input()
count=0
for i in n:
     count=count+1
print("length of string:",count)     
'''
# print tax:
'''s=float(input())
if s<=150000:
    print("tax=",0)
elif s<=300000:
    r=(s-150000)*0.10
    print("tax=",r)
elif s<=500000:
    r=(s-300000)*0.20
    print("tax=",r)
else:
    r=(s-500000)*0.30
    print("tax=",r)
'''
#print vowels:
'''s=input()
vowel=0
consonants=0
for i in s:
    if i.isalpha():
       if i in("AEIOUaeiou"):
            vowel=vowel+1
            print("Vowels:",vowel)
       else:     
             consonants=consonants+1
             print("Consonants=",consonants)
'''
# print tax:
'''s=float(input())
if s<=150000:
    print("tax=",0)
elif s<=300000:
    r=(s-150000)*0.10
    print("tax=",r)
elif s<=500000:
    r=(s-300000)*0.20
    print("tax=",r)
else:
    r=(s-500000)*0.30
    print("tax=",r)
'''
# print palindrome between two numbers:-
'''start=int(input())
end=int(input())
for i in range(start,end+1):
     n=i
     rev=0
     while i!=0:
        d=i%10
        rev=rev*10+d
        i=i//10
     if n==rev:
        print(n,end=" ")
                                                                                     
'''
#  arm strong number:-
'''n=int(input())
tem=n
p=len(str(n))
s=0
while n!=0:
    d=n%10
    s=s+d**p
    n=n//10
if s==tem:
    print("armstrong")
else:
    print("no armstrong")
'''

#  arm strong number using for loop:
'''n=int(input())
p=len(str(n))
for i in range(n,n+1):
     tem=i
     s=0
     while i!=0:
        d=i%10
        s=s+d**p
        i=i//10
    if s==tem:
         print(tem)                                                         

'''
# count even numbers:-
'''n=input()
count=0
for digit in n:
    d = int(digit)
    if d % 2 == 0:
        count +=1
if count == 0:
    print(-1)
else:
    print(count)
'''
#factorial:-
'''import math
L=int(input())
R=int(input())
fact = [math.factorial(i) for i in range(10)]
result = []
for num in range (L, R, +1):
    digit_sum = sum(fact[int(digit)] for digit in str(num))
    if digit_sum == num:
        result.append(str(num))
if result:
    print(" ".join(result))
else:
    print("No Special Numbers")
'''
# strings:-
'''s="Sree"
print(s.isalpha())
'''
'''s="123"
print(s.isdigit())
'''
'''s="Sree123"
print(s.isalnum())
'''
'''s="SREE"
print(s.isupper())
'''
'''s="sree"
print(s.islower())
'''
'''s="sree"
print(s.startswith(s))
'''
'''s="sree"
print(s.endswith('e'))
'''
#count alpha numbers special character:-
'''s=input()
count=0
d=0
sp=0
for i in s:
    if i.isalpha():
        count+=1
    elif i.isdigit():
        d+=1
    else:
        sp+=1
print("alpha:",count)
print("digit:",d)
print("special character:",sp)
'''
#count upper, lower,sp:-
'''s="AabcR"
c=0
u=0
l=0
sp=0
for i in s:
    if i.isalpha():
        c+=1
    if i.isupper():
        u+=1
    else:
        l+=1
print("alpha:",c)
print("upper:",u)
print("lower:",l)
'''
# find numbers:-
'''s="vijji is very popular person"
print(s.find("very"))
print(s.find("very",13,15))
print(s.replace("popular","high level"))
'''
# strip:-
'''s="     vijji is very popular person    "
print(s.lstrip())
'''
#joined method:-
'''s="vijji is very popular person"
print("-".join(s))
'''
#joined upper:-
'''s="vijji is very popular person"
print(s.upper())
'''
# title
'''s="vijji is very popular person"
print(s.title())
'''
# captilize:-
'''s="vijji is very popular person"
print(s.capitalize())
'''
#split:-
'''s="vijji is very popular person"
print(s.split())
'''
#partition:-
'''s="vijji is very popular person"
print(s.partition("popular"))
'''
# print numerical & ord &chr:-
'''print(ord("A"))
print(chr(24))
'''
# print numerical:-
'''n=input()
for i in range(65,91):
    print(i,"--->",chr(i))
'''
# lists:-
'''n=[1,"g",2.4,"true"]
print(n[1])
'''
#slice:-
'''s=[10,20,30,40,50,60]
print(s[4:7])
print(s[3:0:-1])
print(s[1:4])
print(s[3:0:-1])
'''
#add + two list:-
'''s=[1,2,3]
p=[4,5,6]
h=s+p
print(h)
'''
#update list value:-
'''p=[1,'g',0,'p']
p[1:3]=[50]
print(p)
'''
#len():-
'''s=input()
print(len(s))
'''
# list function:-
'''s=[10,20,30,40]
print(max(s))
print(min(s))
print(sum(s))
print(any(s))
print(all(s))
print(len(s))
print(sorted(s))
print(list (reversed(s)))
'''
#list method:-
'''s=[10,20,30,40,50]
s.append(1)
print(s)
'''
#insert method():-
'''s=[10,20,30,40,50]
s.insert(2,"vijji")
print(s)
'''
#index method():-
'''s=[10,20,30,40,50,20,567,20]
print(s.index(20))
print(s.index(20,2,7))
print(s.index(20,6))
'''
#remove():-
'''s=[10,20,30,40,50,20,567,20]
s.remove(20)
print(s)
s.remove(20)
print(s)
s.remove(40)
print(s)
s.remove(567)
print(s)
'''
#pop():-
'''s=[10,20,30,40,50,20,567,20]
print(s.index(20))
print(s.index(20))
'''
#extend:-
'''s=[10,20,30]
s.extend([20])
print(s)
'''
# reverse method():-
'''s=[10,20,30,40,50,20]
s.reverse()
print(s)
'''
#sort method():-
'''s=[10,20,30,40,50,20]
s.sort()
print(s)
'''
# clear method:-
'''s=[10,20,30,40,50,20]
s.clear()
print(s)
'''
#list deep copy()method:-
'''s=[10,20,30]
k=s.copy()
k[0]="H"
print(k)
'''
#list copy()method:-
'''s=[10,20,30]
k=s.copy()
k[0]="H"
print(k)
print(s)
'''
#cloning lists pop():-
'''s=[10,20,30]
s.pop()
print(s)
'''
# single input:-
'''s=[10,20,30]
for i in s:
    print(i,end=" ")
'''
#single input using while loop:-
'''s=[10,20,30]
n=len(s)
i=0
while i<n:
      print(s[i],end=" ")
      i=i+1
'''
# max :-
'''s=[10,30,15,8,70,50]
max=s[0]
for i in s:
    if i>max:
        max=i
print(max)
'''
#min:-
'''s=[10,30,15,8,70,50]
min=s[0]
for i in s:
    if i<min:
        min=i
print(min)
'''
#sum:-
'''s=[1,2,3,4,5]
v=0
for i in s:
    v=v+i
print(v)
'''
#enumerate:-
'''s=[10,20,30,40]
for i,j in enumerate(s):
        print(i,j)
'''
# for loop:-
'''s=[1,2,3,4,5]
n=len(s)
for i in range(n):
        print(s[i])
'''
# range in emumerate:-
'''s=[1,2,3,4,5]
n=len(s)
for i in range(n):
        print(i,s[i])
'''
# square :-
'''s=[1,2,3,4,5]
for i in s:
        print(i**2,end=" ")
'''
# square using list:-
'''s=[1,2,3,4,5]
res=[]
for i in s:
        n=i**2
        res.append(n)
print(res)
'''
# cube using list:-
'''s=[1,2,3,4,5]
res=[]
for i in s:
        n=i**3
        res.append(n)
print(res)
'''
# List comprehensions:-
'''s=[1,2,3,4,5]
res=[i**2 for i in s]
print(res)
'''
# print list even numbers(for loop):-
'''s=[1,3,4,5,8,9,10,11]
res=[]
for i in s:
        if i%2==0:
                res.append(i)
        
print(res)
'''
# List comprehensions even numbers:-
'''
s=[1,2,3,4,5]
res=[i for i in s if i%2==0]
print(res)
'''

# List comprehensions postive  numbers:-
'''s=[1,-2,3,-4,5]
res=[i for i in s if i>0]
print(res)
'''
# print list numbers:-
'''s=int(input())
n=[]
for i in range(s):
        v=int(input())
        n.append(v)
print(n)
'''        
# rotate right &left:-
'''s=[1, 2 ,3, 4 ,5, 6]
p=int(input())
lr=s[p:]+s[:p]
rs=s[-p:]+s[:-p]
print(lr)
print(rs)
'''
# strong number:-
'''n=int(input())
temp=n
s=0
while n:
    d=n%10
    fact=1
    for i in range(1,d+1):
        fact=fact*1
        s=s+fact
    n=n//10
if s==temp:
    print("strong number"
else:
    print("not a strong number")
'''
#find nth prime number:-
'''s=int(input())
c=0
n=1
while c < s:
      n+=1
      for i in range(2,n):
         if n%i==0:
             break
      else:
           c+=1
print(n)
'''
# tuple:
'''s=(10,20,30,40,50)
for i in s:
    print(i)
'''
# while
'''s=(10,20,30,40)
i=0
m=len(s)
while i<m:
    print(s[i])
    i=i+1
'''
# tuple:
'''s=(10,20,30,40,50)
for i in range(len(s)):
    print(s[i],end=" ")
'''
'''s=(10,20,30,40,50)
for i,j in enumerate(s):
    print(i,j)
'''

'''s=(10,20,30,40,50)
for i,j in range (len(s)):
            print(s)

'''
# ANagram :-
'''s1=input()
s2=input()
if sorted(s1)== sorted(s2):
    print("Anagram")
else:
    print("Not an Anagram")
'''
# Anagaram condition:2
'''s1=input()
s2=input()
if len(s1)==len(s2):
    for i in s1:
       if i not in s2:
         print("Not an anagram")
         break
else:
    print("anagram")
'''
# print target and indices values:-
'''s=[10,2,4,5,6]
n=len(s)
target=9
for i in range(n):
    for j in range(i+1,n):
        if s[i]+s[j]==target:
            print(i,j)
        break
'''
# tuple:-
'''s=(10,20,"H",(40,60,(12,13,14),70,80,90),50)
print(s[3])
print(s[3][2])
print(s[3][0])
print(s[3][1])
print(s)
'''
# model 2 tuple un packing:-
'''s=(10,20,"H",(40,60,(12,13,14),70,80,90),50)
print(s)
d=(28,24)
s=(10,20,"H",(40,60,(12,13,14),*d,70,80,90),50)
print(s)
'''
# print invidual:-
'''s=(10,20,"H",40,60,12,13,14,70,80,90,50)
print(*s)
'''
#packing process tuple:-
'''s,*d=10,20,"H"              # input1=first value
print(s)                    # add * input = middile value
print(d)                    # input 3 = last value
'''
#model 2:-
'''s,*d,h=10,20,"H",30,40
print(s)
print(d)
print(h)
'''
# dispossible variable (ignore variable):-
'''s,*_,h=10,20,30,40
print(s)
print(h)
'''
# print even tuple :-
'''s=(10,20,13,17,19,50,70)
list=[]
for i in s:
    if i%2==0:
        list.append(i)
print(tuple(list))
'''
# print maximum values:-
'''s=[10,5,8,7,9,10]
n=len(s)
max=0
for i in range(n):
    for j in range(i+1,n):
         d=s[i]-s[j]
         if d>max:
             max=d
print(max)
'''
#tuple using new tuple:-
'''s=(10,12,13,17,20,40)
t=()
for i in s:
    if i%2==0:
        t=t+(i,)
print(t)
'''
# tuple comphension:-
'''s=(10,12,13,4,7,9,11)
d=tuple(i for i in s if i%2==0)
print(d)
'''
# set of data types:-
'''s=set()
print(s)
'''
'''s={10,20,30}
print(s)
'''
'''d=set("vijju")
print(d)
'''
# creating set:-
'''s=set()
print(type(s))
s={10,20,30}
print(s)
d=set("vijju")
print(d)
'''
#Acessing elemnt:-
'''s={10,28,28,24}
for i in s:
     print(i)
'''
#Acessing element sum:-
'''s={10,22,24,24,28}
sum=0
for i in s:
     sum=sum+i
print(sum)
'''
# find the length:-
'''s={10,20,30,40}
sum=0
for i in s:
    sum=sum+1
print(sum)
'''
# add the element:-
'''s={10,30,"P",50}
s.add(22)
print(s)
'''
# remove element:-
'''s={10,30,"P",50}
s.remove("P")
print(s)
'''
# discard element method:-
'''s={10,30,"P",50}
s.remove("P")
s.discard("V")
print(s)
'''
#Update method:-
'''s={10,30,"P",50}
s.update([28,24])
print(s)
'''
# using pop():-
'''s={10,30,"P",50}
print(s.pop())
print(s)
'''
# using copy():-
'''s={10,30,"P",50}
h=s.copy()
print(h)
'''
# using
'''a=int(input())
s=set()
for i in range(a):
    v=int(input())
    s.add(v)
print(s)
'''
#union:-
'''s1={10,20,30,40}
s2={50,60,70}
s3=s1.union (s2)
print(s3)
'''
#intersection:-
'''s1={10,20}
s2={30,40}
s3=s1.intersection (s2)
print(s3)
'''
#intersection_update():-
'''s1={10,20}
s2={30,40,10}
s1.intersection_update(s2)
print(s1)
'''
#Difference:-
'''s1={10,20,30,40}
s2={50,60,70,90}
s3=s1.difference(s2)
print(s3)
'''
#Difference_update:-
'''s1={10,20,30,40}
s2={50,60,70,90}
s1.difference(s2)
print(s1)
'''

# dictinoary{}:-
'''d={}
print(type(d))
s={"P","28","10","v"}
print(s)
'''
#
'''d={}
print(type(d))
s={"P":"28","10":"v"}
print(s)
'''
# dictionary using set:-
'''d={}
print(type(d))
s={"P":{28},"10":"v"}
print(s)
'''
# KEYS must be unique:-
'''s={1:10,2:"v"}
print(s)
'''


#using this dictionary :-
'''d={"name":["vijju","usha"],"rollno":[412]}
print(d["name"])
print(d["rollno"])
'''
# nested dictionary:-
'''d={"name":{"f":"vijju","s":"usha"},
   "rollno":{1:412,2:103}}
print(d["name"])
print(d["name"]["f"])
'''
# from keys:-
'''f=["v","i","j","j","u"]
s=50
r=dict.fromkeys(f,s)
print(r)
'''
# another model get():-
'''f={"v":10,"i":20,"j":30,"j":40,"u":50}
print(f.get("r"))
'''
# get()
'''f={"v":10,"i":20,"j":30,"j":40,"u":50}
print(f.get("v"))
'''
#key(),value(),item():-
'''f={"v":10,"i":20,"j":30,"j":40,"u":50}
k=f.keys()
v=f.values()
i=f.items()
print(k)
print(v)
print(i)
'''
##### looping dictionary:-
'''f={"v":10,"i":20,"j":30,"j":40,"u":50}
for i in f:
    print(i,end=" ")
'''
# another model:-
'''f={"v":10,"i":20,"j":30,"j":40,"u":50}
for i in f.keys():
    print(i)
'''
#print only values:-
'''f={"v":10,"i":20,"j":30,"j":40,"u":50}
for i in f.items():
    print(i,end=" ")
'''
# dictionary in enumerates:-
'''f={"v":10,"i":20,"j":30,"j":40,"u":50}
for i,(j,k)in enumerate(f.items()):
    print(i,j,k)
'''
# add:-
'''f={"v":10,"i":20,"j":30,"j":40,"u":50}
c=0
for i in f.values():
    c=c+i
print(c)
'''
#print del():-
'''f={"v":10,"i":20,"j":30,"j":40,"u":50}
del(f["v"])
print(f)
'''
# clear all():-
'''f={"v":10,"i":20,"j":30,"j":40,"u":50}
f.clear()
print(f)
'''
# print dict :-
'''s="Engineering"
d={}
for i in s:
    if i in d:
        d[i]=d[i]+1
    else:
         d[i]=1
print(d)
'''
# error come excute:-
'''try:
    n=int(input())
    r=100/n
    print(r)
except:
    print("Errors occured")
print("After errors occured")
'''
# handling specific error :-
'''try:
    n=int(input())
    r=100/n
    print(r)
except ZeroDivisionError,ValueError:
    print("ZeroDivisionError or Value Error occured")
'''
# unknow error:-
'''try:
    n=int(input())
    d=int(input())
    r=n+d
    print(r)
except ZeroDivisionError,ValueError:
    print("ZeroDivisionError  Error occured")
except ValueError:
    print("ValueError Error occured")
except:
    print("Unknow Error")
else:
    print(" else block excuted only when no errors")
finally:
    print("Fanally Block Excuted always")
'''
#  usr pass word:-
'''d={}
for i in range (3):
    usr = input()
    pas = int(input())
    d[usr] = pas
usr_1= input()
pas_1 = int(input())
if usr_1 in d:
    if  d[usr_1] == pas_1:
        print("Match Found")
    else:
        print("pass not  match ")
else:
    print("User not match")
'''
#
'''def frist():
    print("hello")
frist()
'''
# Function:-
'''def add():
    x=int(input())
    y = int(input())
    print(x+y)
add()
'''
# def add()
'''def add(x,y):
    return x+y
    print(x+y)
print(add(5,6))
'''
#Function withoutparameters with return type:-
'''def add():
    x = 5
    y = 8
    return x + y
s=add()
print(s)
'''
#Function withparameters withoutreturn type:-
'''def add():
     x = int(input())
     y = int(input())
     print(x+y)
add()
'''
#
'''name = "Balu"
def data():
    name="Krishna"
    roll =123
    vlg ="Tiruvuru"
    print("hi "+name+" iam from "+vlg)
data()
'''
# def:-
def num(n):
    if n==1:
        return 1
    return n*num(n-1)
print(num(5))




