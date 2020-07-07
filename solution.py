"""
Q1. Write a timer function to be used as a decorator to time the execution of the following function - 

def waste_time():
    x=0
    for i in range(0,1000):
        x+=i
"""

# Solution

import time 
   
def timer(w_t_func): 

    def timer1(): 
        t1 = time.time() 
        w_t_func() 
        t2 = time.time() 
        print("Output of Question 1")
        print("Execution Time : ",t2-t1) 
  
    return timer1 
   
@timer
def waste_time():
    x=0
    for i in range(0,1000):
        x+=i
        
waste_time() 



"""
Q2. Write a function to check whether the string is a palindrome. The function should take a string as input. If found to be a palindrome, print “is palindrome” else print “not palindrome”.
Sample input - “noon”
Sample output- “is palindrome”
"""

#Solution

def palindrome():
    s=input("Enter a string to check whether it is palindrome or not:")
    for i in range(len(s)//2):
        if s[i]==s[len(s)-i-1]:
            continue
        else:
            print("Output of Question 2")
            print("not palindrome")            
    else:
        print("Output of Question 2")
        print("is palindrome")
palindrome()

"""
Q3. Write a function that will take a sentence as input in the form of a string. Remove all but the first occurrence of every duplicate word in the sentence. Return the modified sentence.
Sample input - “I write code. I love to code.”
Same output- “I write code. I love to.” 
"""

#Solution

def duplicate():
    s=input("Enter a string:")
    fin_li=[]
    for i in s.split():
        if s.count(i)>1 and (i not in fin_li):
            fin_li.append(i) 
        elif s.count(i)==1:
            fin_li.append(i)
    return ' '.join(fin_li)
    
print("Output of Question 3")   
print(duplicate())

"""
Q4. Given a string consisting of uppercase, lowercase and numeric characters - sort the three kinds of characters separately and return the sorted string. Sorting should be done such that if the jth character in the string contains a numeric value then even after sorting, it should contain a numeric value only. Write a function that takes the string as input and returns the sorted string.
Sample input - cC3bB2aA1
Sample output- aA1bB2cC3 
"""

#Solution

def sort_string():
    s=input()
    u=[]
    l=[]
    n=[]
    fin=""
    for i in s:
        if i.islower():
            l.append(i)
        elif i.isupper():
            u.append(i)
        else:
            n.append(i)
    u.sort()
    l.sort()
    n.sort()
    for i in s:
        if i.islower():
            fin+=l[0]
            l.pop(0)
        elif i.isupper():
            fin+=u[0]
            u.pop(0)
        else:
            fin+=n[0]
            n.pop(0)
    return fin
print("Output of Question 4")
print(sort_string())



"""
Ques5.) Write a function that will take a string as input and return a new string without consonants.
Sample input - “abc”
Same output = “a”
"""
# Solution
def remove_consonant(s):
    new_str=''
    for i in s:
        if i in "aeiou":
            new_str+=i
    return new_str
print("Output of Question 5")
print(remove_consonant(input("Enter a string")))

'''
Ques6.) Given a list L and integer K, find the maximum for each and every contiguous subarray of size K. Write a function that takes the list as input and returns the output as a list.
Sample input - [8, 5, 10, 7, 9, 4, 15, 12, 90, 13] , K = 4
Sample output - [10, 10, 10, 15, 15, 90, 90]'''
#Solution
def max_from_every_k_subarray(l,k):
    output=[]
    for i in range(len(l)-k+1):
        output.append(max(l[i:i+k]))
    return(output)
l=[int(x) for x in input("Enter a list of number separated by space").split()]
k=int(input("Enter a number"))
print("Output of Question 6")
print(max_from_every_k_subarray(l,k))

'''Ques7.)
Given a number (greater than 2), print two prime numbers whose sum will be equal to the given number, else print -1 if no such number exists. '''
#Solution
def prime(num):
    if num ==2 or num == 3:
        return True
    elif (num**2-1)%24==0:
        return True
    else:
        return False
    
def func(n):
    for i in range(2,n+1):
        n1=n-i
        if prime(i) and prime(n1):
            return(i,n1)
    else:
        return "-1"
print("Output of Question 7")
print(func(int(input("Enter a number"))))










'''
Ques9.) Write a function that takes a path to a txt file as input and returns a list containing the number of words and sentences in the file. 
Sample input - some txt file containing 10 lines and 100 words
Sample output - [100,10]'''
# Solution
def func(path):
    l=[]
    with open(path,'r') as f:
        txt1=f.read()
        txt2=txt1   
    txt1=txt1.split()
    txt2=txt2.split(".")
    l.append(len(txt1))
    l.append(len(txt2)-1)
    return l
print("Output of Question 9")
print(func(input("Enter text file path")))


