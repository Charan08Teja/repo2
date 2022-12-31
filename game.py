x='play'
y='quit'
z=str(input('input your choice '))
while z==x:
    a=['rock','paper','scissors']
    b=str(input('enter your choice '))
    import random
    c=random.choice(a)
    print('your choice=',b)
    print('computer choice=',c)
    if b=='rock' and c=='paper':
        print('you lost')
    elif b=='paper' and c=='scissors':
        print('you lost')
    elif b=='scissors' and c=='paper':
        print('you won')
    elif b=='rock' and c=='scissors':
        print('you won')
    elif b=='paper' and c=='rock':
        print('you won')
    elif b=='scissors' and c=='rock':
        print('you lost')
    elif b=='paper' and c=='paper':
        print('draw')
    elif b=='scissors' and c=='scissors':
        print('draw')
    elif b=='rock' and c=='rock':
        print('draw')
    print('PRESS P To PLAY AGAIN ')