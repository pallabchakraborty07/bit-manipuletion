arr=[]
n=int(input("enter the array size"))
while n:
    number=int(input("enter array element" ))
    arr.append(number)
    n=n-1
result=0
for element in arr:
    result=result^element
print(result)
