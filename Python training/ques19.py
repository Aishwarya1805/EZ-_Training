'''extract the vowel which has max count'''
str=input()
first='a'
l=['a','e','i','o','u']
for i in str:
    if(i in l):
        first=i
        break
for i in str:
   if(i==first):
       print(i)
       break
                
