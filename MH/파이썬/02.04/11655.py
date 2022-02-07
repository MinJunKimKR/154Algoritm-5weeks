word = input()
ans = ""

for i in word:
    if i.isupper():
        if ord(i)+13 > 90:
            ans+=chr(65+(ord(i)+13)-90-1)
        else:
            ans+=chr(ord(i)+13)
    elif i.islower():
        if ord(i)+13 > 122:
            ans+=chr(97+(ord(i)+13)-122-1)
        else:
            ans+=chr(ord(i)+13)
    elif i.isdigit():
        ans+=i
    elif i.isspace():
        ans+=i
print(ans)