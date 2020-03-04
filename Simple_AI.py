AI_NAME='what kind of taco are you?'
level_verde=0
level_rojo=0
gender=None
age=None
username=input(print('Intruduce your user name'))
print ('Hello experiment',username,'Iam going to help you to know', AI_NAME)
r=input(print ('would you like some green sauce in your taco? (yes/no)'))
if (r=='yes'):
    level_verde = level_verde + 1
else:
    level_rojo=level_rojo+1
r=input(print ('would you like some meat in your taco? (yes/no)'))
if r=='yes':
    level_verde=level_verde+1
else:
    level_rojo=level_rojo+1
print ('would you like some cilantro in your taco? (yes/no)')
if r=='yes':
    level_verde=level_verde+1
else:
    level_rojo=level_rojo+1
age=input(print ('Introduce your Age'))
if(age!=''):
    level_rojo=level_rojo+1
else:
    print(age, 'does not exist in my data base')
gender=input(print ('Introduce your Gender (M or F)'))
if (gender!=''):
    if (gender=='m'):
        gender='Male'
        level_verde=level_verde+1
    if (gender=='f'):
        gender='Female'
        level_rojo=level_rojo+1
else:
    print(gender, 'does not exist in my data base')
if (gender!='' and age!=''):
    if (level_rojo<3 or level_verde<3):
        print('Well I can not work like this', username, 'Come again when you are decided')
        if (level_rojo>4):
            print('That is all', username, 'I think you are green taco')
        else:
            print('Thank you', username, 'I think you are red taco.')
