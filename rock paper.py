import random
print("\n\t\t\t\t\t\t\tWALCOME TO THE GAME\n")
user_name=input("\n\nInput Your name: ")
g=int(input(f'\nHow much time you want to play: '))
r,pc,me,draw=1,0,0,0
while r<=g:
    Ran=['Rock','Paper','scissors']                                     
    p=random.choice(Ran)
    User_input=int(input("---------------------------------------------------------------------------------------\nRock=1\nPaper=2\nSijar=3\ncloise one: "))
    if p=='Rock'and User_input==2:
        print('\nyour choise\t:','Paper')
        print(f'System choise\t:{p}')   
        print('\n\tWin System',' \nTry ',r,' have ',g-r,'\n')
        pc=pc+1
    elif p=='Paper' and User_input==3:
        print('\nyour choise\t:','scissors')
        print(f'System choise\t:{p}')    
        print('\n\tWin system',' \nTry ',r,' have ',g-r,'\n')  
        pc=pc+1 
    elif p=='scissors' and User_input==1:
        print('\nyour choise\t:','Rock')
        print(f'System choise\t:{p}')     
        print('\n\tWin system',' \nTry ',r,' have ',g-r,'\n') 
        pc=pc+1  
    elif p=='Rock' and User_input==1:
        print('\nyour choise\t:','Rock')
        print(f'System choise\t:{p}')     
        print('\n\tDraw the match',' \nTry ',r,' have ',g-r,'\n') 
        draw=draw+1  
    elif p=='Paper' and User_input==2:
        print('\nyour choise\t:','Paper')
        print(f'System choise\t:{p}')   
        print('\n\tDraw the match',' \nTry ',r,' have ',g-r,'\n')   
        draw=draw+1    
    elif p=='scissors' and User_input==3:
        print('\nyour choise\t:','scissors')
        print(f'System choise\t:{p}')   
        print('\n\tDraw the match',' \nTry ',r,' have ',g-r,'\n')  
        draw=draw+1    
    else:
        if User_input==1:
            print('\nyour choise\t:','Rock')
        elif User_input==2:
            print('\nyour choise\t:','Paper')
        elif User_input==3:
            print('\nyour choise\t:','scissors')
        print(f'System choise\t:{p}')   
        print('\n\tWin You',user_name,'\n Try ',r,' have ',g-r,'\n')
        me=me+1  
    r=r+1
if pc<me:
    print('-------------------------------\n','You win',me,'time,','System win',pc,'time,','Draw the match',draw,'time.','\n-------------------------------')
    print('\n\n\t\t\tResult: Win you',user_name,'\n\n')
elif pc==me:
    print('-------------------------------\n','You win',me,'time,','System win',pc,'time,','Draw the match',draw,'time.','\n-------------------------------')  
    print("\n\n\t\t\tResult: Draw the match\n\n")
else:
    print('-------------------------------\n','You win',me,'time,','System win',pc,'time,','Draw the match',draw,'time.','\n-------------------------------')
    print('\n\n\t\t\tResult: Win system, you loser',user_name,'\n\n')