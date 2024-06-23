'''You are given a string containing words separated by spaces. Your task is to write a
function or program that reverses the order of words in the string.
Sample Input:
Hello World
Sample Output:
World Hello'''

def reversing(string):
  words=string.split()
  rev=words[::-1]
  return rev
string=input()
print(*reversing(string))
