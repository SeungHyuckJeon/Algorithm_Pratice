def d():
    original=set(range(1,10001))
    constructor=set()
    
    for i in range(1,10001):
        for j in str(i):
            i+=int(j)
        constructor.add(i)
    
    selfnum=original-constructor
    
    for i in sorted(selfnum):
        print(i)
        
d()