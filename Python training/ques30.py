'''Number of toys
Akshay has a number of toys and he decided to donate some of them to an NGO. After 
the donation, he still has some toys left. Write a program to help Akshay to determine 
the number of remaining toys.
Example:
Input: 50 45
Output: The remaining number of toys = 5
Input: 60 6
Output: The remaining number of toys = 54'''
a=int(input())
b=int(input())
def toys(a,b):
  if(a<b):
    return b-a
  elif(a>b):
    return a-b
print(toys(a,b))