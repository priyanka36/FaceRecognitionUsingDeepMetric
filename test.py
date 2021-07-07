matches=[True,False,True,False,True,False,False,True]

if True in matches:
    matchedIdxs = [i for (i, b) in enumerate(matches) if b]

    print(matchedIdxs)

    matches=[True,False,True,False,True,False,False,True]
    match=[]
    for (i, b) in enumerate(matches):
        if b:
            print(b)
            match +=[i]
            print(match)
        
data ={}
data= {"names": ["Priyanka","Priyanka" ,"Pratik","Meena","Meena","Meena","Priyanka" ,"Priyanka","Pratik"]}
counts={}
named =[]
for i in matchedIdxs:
    name = data["names"][i]
    counts[name] = counts.get(name,0)+1
    # import pdb;pdb.set_trace()
    print(name)
    print(counts)  
    named = max(counts, key=counts.get) 
    import pdb;pdb.set_trace()
    print(named)
named.append(named)    
