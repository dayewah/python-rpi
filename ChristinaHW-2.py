print('====Math Game For Angela by Christina====')

right=0
wrong=0

print('')
print("Question 1: 5 + 3")
answer=input()
print('You answered {0}'.format(answer))
if int(answer)==8:
    print('Correct!')
    right=right+1
else:
    print('Wrong! The answer is 8')
    wrong=wrong+1
    
print('')
print("Question 2: 7 + 3")
answer=input()
print('You answered {0}'.format(answer))
if int(answer)==10:
    print('Correct!')
    right=right+1
else:
    print('Wrong! The answer is 10')
    wrong=wrong+1
    
print('')
print("Question 3: 12 - 5")
answer=input()
print('You answered {0}'.format(answer))
if int(answer)==7:
    print('Correct!')
    right=right+1
else:
    print('Wrong! The answer is 7')
    wrong=wrong+1
    
print('')
print("Question 4: 23 - 5")
answer=input()
print('You answered {0}'.format(answer))
a=23 - 5
if int(answer)==a:
    print('Correct!')
    right=right+1
else:
    print('Wrong! The answer is {0}'.format(a))
    wrong=wrong+1
    
       
print('')
print('You got {0} right and {1} wrong'.format(right,wrong))
