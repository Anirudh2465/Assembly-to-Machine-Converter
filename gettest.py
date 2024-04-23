def getindex(L):
    D={}

    count=0
    for i in range(len(L)):
        if L[i][0]=='(':
            D["@"+L[i][1:len(L[i])-1]]=i-count
            count+=1

    return D

