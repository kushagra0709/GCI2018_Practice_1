for i in range(10):
    print("GCI is great")
a=input("Enter your name please: ")
print("Hello",a,"pleased to meet you!")
b=""
for j in range(-1,-len(a)-1,-1):
    b+=a[j]
print("Did you know that your name backwards is",b)