print('Calculator')
a=float(input())
sign=input()
b=float(input())

if sign=='+':
    res=a+b
elif sign=='-':
    res=a-b
elif sign=='*':
    res=a*b
elif sign=='/':
    if b!=0:
        res=a/b
    else:
        res='Error'
else:
    res='Unknown cooperation'
print(res)
