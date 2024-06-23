'''finding gcd problem'''

def gcd(a,b):
  while b>0:
    a,b=b,a%b
  return a
def lcm(a,b):
  return a*b/gcd(a,b)
a=int(input())
b=int(input())
res_gcd=gcd(a,b)
res_lcm=lcm(a,b)
print(res_gcd)
print(res_lcm)


