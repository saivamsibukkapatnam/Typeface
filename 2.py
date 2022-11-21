s1,s2=input().split(",")

x=s2[len(s2)-1]
count=0
for i in s1:
    if(i == x):
        count=count+1
print(count)
