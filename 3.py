#3

num=int(input("Enter a number="))
sum=0
newnum=num
for i in range(0,4):
    sum=sum+num
    num=(num*10)+newnum
print(sum)    