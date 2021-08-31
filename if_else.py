
name = input("Enter the name:").lower()
vowels = ["i","u","o","a","e"]
num = [0,0,0,0,0]

for i in range(len(name)):
    for j in range(len(vowels)):
        if name[i] == vowels[j]:
            num[j]+=1
        



for i in range(len(vowels)):
    print(vowels[i],":",num[i])