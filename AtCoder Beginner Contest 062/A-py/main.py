x,y = map(int,input().split())
L = [[1,3,5,7,8,10,12],[4,6,9,11],[2]]
print("Yes") if x in L[0] and y in L[0] or x in L[1] and y in L[1] else print("No")
