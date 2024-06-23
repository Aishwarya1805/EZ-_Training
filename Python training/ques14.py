'''Nearest Corner
Bruce is a newly hired employee at a company. The Office Management Department
has given him a desk number, which is stored in string S. He has also been handed a
string array A. containing all the N office desk numbers.
Array A also includes the symbol"-", which stands for the gap in the sitting
arrangement. Comer seats are those that are on either side of the gap. Your task is to
help Bruce find and retum an integer value. representing how far he is from the
nearest corner seat. Return 0, if he is in the corner seat.
Note:
There will always be at least one gap in the string array A
Desk number is always in a format of a number first followed by an English letter in
uppercase
Assume 0 - based indexing
Input Specification:
A string S. representing Bruce's newly assigned desk number.
Second line containing space seperated strings showing the seat positions and gaps
Sample input:
3C
1A 2B - 3C 4D
Sample Output:
0 '''

ip1=input("enter desk no")
ip2=input().split()
x=ip2.index(ip1)
z=float('inf')
for i in range(x+1,len(ip2)):
  if(ip2[i]=='-'):
    z=min(abs(i-x)-(1),z)

for i in range(x):
  if(ip2[i]=="-"):
    z=min(abs(i-x)-1,z)
print(z)
