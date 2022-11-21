n=int(input())
if n==0:
    print("0")
num = []
while n!=0:
    n,m=divmod(n,3)
    num.append(str(m))
print(''.join(reversed(num)))

