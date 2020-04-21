n = int(input('enter #'))
sq=str(n**2)
l=''
for i in range(len(sq)//2):
    l=l+str(sq[i])
p=''
for i in range((len(sq)//2),len(sq)):
    p=p+str(sq[i])
if int(l)+int(p)==n:
    print('kaprekar number')
else:
    print("not")