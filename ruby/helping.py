

f = open('tokens.txt', 'r')
ans=[]
for i in f:
    a=i.split(",")
    a = [x.strip() for x in a]
    for x in a:
        ans.append(x)

a=(set(ans))

f=[]
for i in a:
    print('regex: '+i )
    aux = str(input())
    f.append(''+i+"= r'"+aux+"'")

print("\n".join(f))

