s=input("enter a string")
rev=''
i=-1

while i>=-len(s):
    rev+=s[i]
    i-=1
if s==rev:
    print("plindrome")
else:
    print("not a palindrome")