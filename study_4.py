t1 = (1,"hell0",True)
t2 = ()
print(t1,type(t1))
print(t2,type(t2))

#如果元组只有一个数据，需要加，
t3 = (1,)
print(t3,type(t3))

t4 = ((1,2,3),(4,5,6),"hah")
print(t4[1][1])

index = t4.index("hah")
print(index)
count = t4.count("hah")
print(count)
count = len(t4)
print(count)
