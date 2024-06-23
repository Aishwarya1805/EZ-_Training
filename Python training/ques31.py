'''Smallest Number
Prince participated in three Olympiads at school and received marks for all of them. 
He is interested in finding out the lowest mark he obtained among the three 
Olympiads. Write a program to find the minimum mark.
Example:
Input: 50 66 23
Output: Smallest number is 23'''

def smallest(arr):
  smallest=arr[0]
  for i in range(len(arr)):
    if(smallest < arr[i]):
      continue
    else:
      smallest=arr[i]
  return smallest
arr=list(map(int,input().split()))
print(smallest(arr))
 