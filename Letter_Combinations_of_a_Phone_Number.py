s=""
l=["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
k=""
ans=[]
if len(s)==0:
    print(ans)
else:
    def f(k,ind):
        if len(s)==len(k):
            ans.append(k)
            return
        for j in l[int(s[ind])-2]:
            f(k=k+j, ind=ind+1)
f(k, 0)
print(ans)

