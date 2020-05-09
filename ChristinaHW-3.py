from random import randint
print('====Math Game For Angela by Christina====')

right=0
wrong=0

while True:
    x=randint(1,20)
    y=randint(1,20)

    print('')
    print("Question: {0} - {1}".format(max(x,y), min(x,y)))
    answer=input()
    print('You answered {0}'.format(answer))
    a = max(x,y) - min(x,y)
    if int(answer)== a:
        print('Correct!')
        right=right+1
    else:
        print('Wrong! The answer is {0}'.format(a))
        wrong=wrong+1
        
    response=input('Do you want another question? [y/n]:')
    
    if response == 'y':
        continue
    elif response == 'n':
        break
    else:
        break
    
       
print('')
print('You got {0} right and {1} wrong'.format(right,wrong))
