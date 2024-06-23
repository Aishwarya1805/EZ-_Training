'''Pangram is a sentence containing every letter in the English alphabet. Given a string, 
find all characters that are missing from the string, Le., the characters that can make 
the string a Pangram We need to print output in alphabetic order.
For example,
Input: welcome to geeksforgeeks
Output: abdhijnpquvxyz '''

def findmissing(string):
  alp="abcdefghijklmnopqrstuvwxyz"
  string=string.lower()
  missing=[]
  for i in alp:
    if i not in string:
      missing.append(i)
    sorted_op=sorted(missing)
  return missing
string="welcome to bitm"
print(*findmissing(string))
print(''.join(string))

