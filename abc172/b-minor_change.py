s=list(input())
t=list(input())
ans = 0
for i, _s in enumerate(s):
    if s[i] != t[i]:
        ans+=1
print(ans)