# Problem D
a=int(input(''))
b=input('')
b=b.split()
b=list(map(int, b))
c=sorted(b)
ans=[]
for i in range(a):
    ans.append('W')
for num in range(len(b)):
    for num in range(len(c-1)):
        if b[num]==c[num]:
            s=sum(c[0:num+1])
            if s<c[num+1]:
                ans[num]='L'
print(ans)