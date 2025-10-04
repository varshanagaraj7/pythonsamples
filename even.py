n=int(input("enter the size of an array:"))
evencount=0
oddcount=0
number=[]
print("enter the numbers:")
numbers=[int(input()) for i in range(n)]
for num in numbers:
    if num%2==0:
       evencount+=1
    else:
       oddcount+=1
print("even numbers count:",evencount)
print("odd numbers count:",oddcount)
