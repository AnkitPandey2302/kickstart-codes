t=int(input())
i=1
while i<=t:
    n=input()
    ansl=[]
    for i in range(len(n)+1):
        te=n
        for j in range(10):
            no=int(te[:i]+str(j)+te[i:])
            #print(no)
            if no%9==0:
                ansl.append(no)
    #print(ansl)
    ansl.sort()
    ans=ansl[0]
    print("Case #",i,": ",ans,sep='')
    i+=1