t=int(input())
i=1
while i<=t:
    o=input()
    p=input()
    ans=len(p)-len(o)
    flag=False
    
    for e in o:
        #print(e,o)
        if e in p:
            p=p[p.find(e)+1:]
            #print(p)
        elif e not in p:
            #print(e,o,p)
            flag=True
            break
    if flag:
        ans="IMPOSSIBLE"
    print("Case #",i,": ",ans,sep='')
    i+=1