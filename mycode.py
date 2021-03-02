
import os
import warnings
warnings.filterwarnings('ignore')


for FILE in os.listdir('.'):
  #  print(FILE)
    if not FILE.endswith(".txt") :
        continue
    with open(FILE, 'r') as ifp:
	    lines = ifp.readlines()

   # print(lines)

    info=list(map(int,lines[0].strip().split()))
    d,n,s,v,f=info[0],info[1],info[2],info[3],info[4]
    streets={}
    path={}

    path1={}
    intcnt={}
    stcnt={}
    stname={}
    for i in range(n):
        path[i]=[]
        intcnt[str(i)]=0
        stcnt[str(i)]=0
        stname[str(i)]=[]

    for i in range(s):
        street=list(map(str,lines[1+i].strip().split()))
        streets[street[2]]=int(street[3])

        path[int(street[0])].append(int(street[1]))

        path1[street[2]]=[street[0],street[1]]

        stcnt[street[1]]+=1
        stname[street[1]].append(street[2])
   
    root={}
    solution=[]
  
    for i in range(v):
        root[i]=[]
    cars=[]    
    for j in range(v) :
        pt=list(map(str,lines[s+1+j].strip().split()))
        root[i]=pt[1:]
        total_time=0
        car=[]
        for i in pt[1:] :
            car.append(path1[i][1])

    print(len(car))
    for i in range(len(car)):
        print(car[i])
        print(stcnt[str(car[i])])
        for j in stname[str(car[i])]:
            print(j,1)
    
    


        



    
        


	# Convert content to data structures
	# #Books, #Libraries, #Days 
	