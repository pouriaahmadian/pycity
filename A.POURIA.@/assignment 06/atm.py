p=3511
c=0
while c!=3 :
    r=int(input('enter psword:'))
    c+=1
    if r!=p:
        print('dobare talash kon')
        continue
    elif r==p:
        print('khosh omadi')
        break
