#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output


# In[2]:


from random import randint


# In[3]:


block=['0',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']


# In[4]:


def display(block):
    clear_output()
    print(block[1]+' | '+block[2]+'| '+block[3])
    print('--|'+'--|'+'--')
    print(block[4]+' | '+block[5]+'| '+block[6])
    print('--|'+'--|'+'--')
    print(block[7]+' | '+block[8]+'| '+block[9])


# In[5]:


def ask():
    ans='x'
    cp=4
    while ans not in ['Y','N']:
        ans=input("Do you want to continue playing? Press Y or N : ")
    while (cp not in [1,2]) and (ans =='Y'):
        cp=int(input(" Press 1 to play with computer,\n Press 2 to play with Player2 "))
    return [ans,cp]


# In[6]:


def player1(block,l):
    gameon=True
    print("PLAYER 1")
    choice=input("Enter the position number of your choice from 1-9 : ")
    if choice.isdigit()==False:
        print("Enter an INTEGER NUMBER between 1-9")
        return player1(block,l)
    elif int(choice) not in range (1,10):
        print("Enter number between 1-9 : ")
        return player1(block,l)
    else:
        choice=int(choice)
        if choice not in l:
            block[choice]='O'
            l.append(choice)
            print('Used positions : {}'.format(l))
            return [block,l]
        else:
            print("Enter some other not consumed position ")
            return player1(block,l)
        
    
        
    


# In[7]:


def player2(block,l):
    print("PLAYER 2")
    choice=input("Enter the position number of your choice from 1-9 : ")
    if choice.isdigit()==False:
        print("Enter an INTEGER NUMBER between 1-9")
        return player2(block,l)
    elif int(choice) not in range (1,10):
        print("Enter number between 1-9 : ")
        return player2(block,l)
    else:
        choice=int(choice)
        if choice not in l:
            block[choice]='X'
            l.append(choice)
            print('Used positions : {}'.format(l))
            return [block,l]
        else:
            print("Enter some other not consumed position ")
            return player2(block,l)
        
    
        
    


# In[8]:


def comp(block,l):
    print("COMPUTER : ")
    choice=randint(1,9)
    while choice in l:
        choice= randint(1,9)
    block[choice]='X'
    l.append(choice)
    print('Used positions : {}'.format(l))
    return [block,l]
        


# In[9]:


def win(block):
    if block[1]==block[2]==block[3] in ['O','X']:
        if block[1]=='O':
            print("Player 1 wins")
        else:
            print("Player 2 wins")
        return True
    elif block[4]==block[5]==block[6] in ['O','X']:
        if block[4]=='O':
            print("Player 1 wins")
        else:
            print("Player 2 wins")
        return True
    elif block[7]==block[8]==block[9] in['O','X'] :
            if block[7]=='O':
                print("Player 1 wins")
            else:
                print("Player 2 wins")
            return True
    elif block[1]==block[4]==block[7] in ['X','O']:
            if block[1]=='O':
                print("Player 1 wins")
            else:
                print("Player 2 wins")
            return True
    elif block[2]==block[5]==block[8] in ['O','X']:
            if block[2]=='O':
                print("Player 1 wins")
            else:
                print("Player 2 wins")
            return True
            
    elif block[3]==block[6]==block[9]in ['O','X']:
            if block[3]=='O':
                print("Player 1 wins")
            else:
                print("Player 2 wins")
            return True
    elif block[1]==block[5]==block[9]in ['O','X']:
            if block[1]=='O':
                print("Player 1 wins")
            else:
                print("Player 2 wins")
            return True
    elif block[3]==block[5]==block[7]in ['O','X']:
            if block[3]=='O':
                print("Player 1 wins")
            else:
                print("Player 2 wins")
            return True
    else:
        return False


# In[10]:


def exit():
    print("THE PROGRAM HAS ENDED! THANKS FOR PLAYING :)")


# In[11]:


def start(block):
    a=1
    o=1
    l=[]
    ans=[]
    ans=ask()
    while ans[0]=='Y':
        while o<10:
            if ans[1]==2:
                display(block)
                if win(block)==False:
                    if a==1:
                        x=player1(block,l)
                        block=x[0]
                        l=x[1]
                        a=1-a
                    elif a==0:
                        x=player2(block,l)
                        block=x[0]
                        l=x[1]
                        a=1-a
                    o=o+1
                else:
                    exit()
                    o=10
            elif ans[1]==1:
                display(block)
                if win(block)==False:
                    if a==1:
                        x=player1(block,l)
                        block=x[0]
                        l=x[1]
                        a=1-a
                    elif a==0:
                        x=comp(block,l)
                        block=x[0]
                        l=x[1]
                        a=1-a
                    o=o+1
                else:
                    exit()
                    o=10
        else:
            if win(block)==False:
                display(block)
                print("DRAW!")
                exit()
            break
    else:
            print("OKHAY BYE!")
        


# In[12]:


start(block)


# In[ ]:





# In[ ]:




