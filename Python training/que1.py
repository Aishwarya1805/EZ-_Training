''' There is a ant on your balcony. It wants to leave the rail so sometimes it moves right and sometimes It moves left until it gets
 exhausted Given an integer array A of 112 N
 which consists of integer 1 and 1 only representing ant's moves. Where I means ant noved unit distance towards the right side 
and 1 means it moved unst distance towards the left.
 Your task is to find and return the integer value representing how many times the ant reaches back to original starting position.
Note: Assume 1-based indexing Assume that the railing extends Infinitely on the either sides Input Formati
input1: An integer value & representing the numben of moves made by the ant. 
Input2: An Integer array A consisting of the ant's moves towards either side'''

n=int(input())
arr=list(map(int,input().split()))
count=0
for i in range(n):
  if(sum(arr[i:i+1])==0):
    count=count+1
print(count)
