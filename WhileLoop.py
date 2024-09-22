
count =0

while count<5:
    print(count)
    count+=1
print("*********Example 2***********")

count =0
while count%2==0:
    print(count)
    count+=1

print("*********Example 3***********")
## Loop Control Statement
## break
## The break statement exits the loop permanently

for i in range(10):
    if i == 5:
        break
    print(i)

print("*********Example 4***********")
## Loop Control Statement
## continue
## The continue statement skips the current iteration and continues with next.

for i in range(10):
    if i == 5:
        continue
    print(i) 

print("*********Example 5***********")
## Pass
## The pass statement is a null operation; it does nothing

for i in range(5):
    if i==3:
        pass
    print(i)
