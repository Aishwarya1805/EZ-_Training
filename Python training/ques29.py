'''Peak Element Finder
Description: You are given an N- dimensional array arr[]. A peak element in the array 
is defined as an element whose value is greater than or equal to its neighboring 
elements (if they exist). Your task is to find the index of any peak element in the given 
array
Note: use 1-based indexing
Input:
An integer representing the number of elements in the array. N space-separated 
integers, denoting the elements of the array.
N space-separated integers ,denoting the elements of the array arr[]
Sample Input:
5
1 3 20 4 1
Sample Output:
3'''

def peak(n,arr):
  ans=0
  for i in range(1,n+1):
    if(arr[i]<arr[i-1] and arr[i]>arr[i+1]):
      ans=i
      break
  if (arr[-2]>arr[-1] and arr[-1]>ans):
    ans=len(arr)-1
  return ans
n=int(input())
arr=list(map(int,input().split()))
print(peak(n,arr))

