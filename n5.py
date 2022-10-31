s = input("Enter text: ").split()
count = 0
flag = False

for i in s:
    if i.isalpha():
        count += 1
    else:
        count = 0
    if count == 3:
        flag = True
        break
print(flag)
