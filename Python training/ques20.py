'''You work in the message encoding department of a national security agency. Every message
that is sent from or received in your office is encoded. you have a string containing , alpha numeric characters.
of N is squared and the squares are concatenated together to encode the original number.
Your task is to find and return an integer value representing the encoded value of the
number.
input1: An a string  representing the number and chracters 
Output :
Return an integer value representing the encoded value of the number
input format:
"hello 123 good morning"
output:
149
'''
def encode(s):
    res=[]
    for char in s:
        if char.isdigit():
            num=int(char)
            squa=num * num
            res.append(squa)
    return res
s=input()
encoded_numbers = encode(s)
print("".join(map(str, encoded_numbers)))



