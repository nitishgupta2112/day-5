arr = list(map(int,input().split(",")))
# arr =(12,18,25,24,2,5,18,20,20,21)
def find_more_than_avg(arr):
    s=sum(arr)
    avg=s*0.1
    count = 0
    for i in arr:
        if(i>=avg):
            count+=1
    print(float(count*10))
def frequency(arr):
    l2=[]
    for i in range(0,25):
        c = arr.count(i)
        l2.append(c)
    print(*l2,sep=",")
def sort_marks(arr):
    s = sorted(arr)
    print(*s,sep=",")
find_more_than_avg(arr)
frequency(arr)
sort_marks(arr)
'''
freq=[]
for x in range(26):
    count=0
    for y in arr:
        if x==y:
            count+=1
    freq.append(count  )
        
'''