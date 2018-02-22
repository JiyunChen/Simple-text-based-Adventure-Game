#Name: Jiyun Chen
import numpy as np
import random
      
def menu():
    """this function is to show the main menu of the game """
    print "Welcome to the Pokemon World!"#describe the options
    print "What do you want to do?"
    print "1.Start your new adventure!"
    print "2.Continue your game!"
    print "3.Quit!"
    n=raw_input("Your choose:")#save the users choose
    print
    return(int(n))

def sub_menu():
    """this function is to show the sub menu when you are already in the game"""
    print "1.Go on adventure!"
    print "2.Check your Pokemons!"
    print "3.Save your game!"
    print "4.Quit"
    n=raw_input("Your choose:")#save the users choose
    print
    return(int(n))

class game_adventurer():#create the class of game_adventurer() for users
    def __init__(self):
        """get the initial attributes for users"""
        self.position=np.array([4,4])# the initial position on the map for users
        self.pokemon=[]# the pokemon users have
        self.map=np.chararray((9, 9))# define the context for the map
        self.map[:]="_"
        self.map[self.position[0],self.position[1]]="O"# O is the position where users are
        
    def show(self):
        """this function is to show the map for adventure"""
        print " ", " ",         # label the column axis
        for i in range(9):
            print str(i+1),
        print "\n ", " ",
        for i in range(9):
            print '=',          # print the cut-off line
        print
        i = 1
        for r in self.map:
            print str(i), "|",  # label the row axis and print cut-off line
            for x in r:
                print x,        # print the str-matrix
            print
            i += 1
        print "O is your position"# O is the position where users are
        print "\n ", "\n",
            
    def first_pokemon(self,p):
        """get the first pokemon for the user before the adventure"""
        if p=="1":#option for different pokemons
            self.pokemon.append('squirtle')
        elif p=="2":
            self.pokemon.append('bulbasaur')
        elif p=="3":
            self.pokemon.append('charmander')
        else:
            print "Please enter the number 1-3!"
        
    def move(self,n):
        """this function for showing the map when users try to move"""
        try:#avoid the index error
            if n=="A":#W for up, S for down, D for right, A for left
                self.position[1]-=1
            elif n=="D":
                self.position[1]+=1
            elif n=="W":
                self.position[0]-=1
            elif n=="S":
                self.position[0]+=1
            print "Your current position"
            self.map[:]="_"#the current map
            self.map[self.position[0],self.position[1]]="O"
        except IndexError:
            print "Do not move! You will go out of the map!"

class pokemon():#create the class for the pokemon that users may meet during the adventure
    def __init__(self):
        """get the attribute for the pokemon"""
        self.name=random.choice(['squirtle', 'bulbasaur', 'charmander', 'pikachu','ditto','vulpix','oddish','paras','zubat','mankey'])
        #name
        self.meet=np.random.randint(10)# the value for meet (use for the calculate the probability for meeting)
        self.capture=np.random.randint(10)#the value for catch(use for the calculate the probability for catching)
    def rate_meet(self):
        """shows that pokemon is met or not"""
        if self.meet > 8:
            return False
        else:
            return True
    def rate_capture(self):
        """shows that pokemon is caught or not"""
        if self.capture > 6:
            return False
        else:
            return True

def get_first_pokemon(user):
    """get the first pokemon for users"""
    p=raw_input("Which Pokemon you want to choose to be your first buddy?"+"\n"+"1.squirtle,2.bulbasaur,3.charmander"+"\n"+"Notes: Enter the number!"+"\n"+"Your choose:")
    print "\n","\n"
    print "Now start your adventure!!!"
    print "\n","\n"
    user.first_pokemon(p)

def choose_1(user):
    """when users choose 1.Go on adventure!"""
    n=raw_input("Where you want to go?(W for up, S for down, D for right, A for left)")
    user.move(n)#get the new map
    user.show()#display the map
    poke=pokemon()#object for the pokemon class
    if(n=="W" or n=="S" or n=="A" or n=="D"):
        if poke.rate_meet():#if we can meet the pokemon
            print "Wow! You meet the"+" "+poke.name
            catch=raw_input("You want to capture or not? (Y/N)")
            if catch=="Y":#if we can catch it
                if poke.rate_capture():
                    print "Congrats!!!! You catch"+" "+poke.name+"!!!!!"
                    user.pokemon.append(poke.name)#save this pokemon
                else:
                    print "What a pity"+" "+poke.name+"runs away!"+" "+"Try next time."
            elif catch=="N":
                print "Yeah! We run!"
            else:
                print "Please press Y or N. You miss this chance!"
        else:
            print "Oh, we don't meet Pokemon this time."
    else:
        print "Please enter W,S,A,D"

def choose_2(user):
    """when users choose 2.Continue your game!"""
    print "You have the pokemons:"
    print user.pokemon

def choose_3(user):
    """when users choose 3.Save your game!"""
    with open("record.txt","w") as out:#write the file to save the record
        out.write(str(user.position[0])+"\n"+str(user.position[1])+"\n")#save the position
        for index in user.pokemon:#save the all pokemons which are caught
            out.write(str(index)+"\n")
        print "You save the game sucessfully!"
        
def start_game(user):
    """when use choose to go the adventure """
    user.show()#show the map
    print "\n","\n"
    choose=sub_menu()#show the sub menu
    while choose!=4:
        try:#avoid the value error(user may enter the character not the number)
            if choose==1:
                choose_1(user)#run the choose_1() funciton
                print "\n","\n"
                choose=sub_menu()#show the sub menu and save the choice
            elif choose==2:
                choose_2(user)#run the choose_2() funciton
                print "\n","\n"
                choose=sub_menu()#show the sub menu and save the choice    
            elif choose==3:
                choose_3(user)#run the choose_3() funciton
                print "\n","\n"
                choose=sub_menu()#show the sub menu and save the choice
            else:
                print "Please enter the number 1-3"
                print
                choose=sub_menu()#show the sub menu and save the choice
        except ValueError:
            print "Please enter the number 1-3! Not the characters!"
            print
            choose=sub_menu()#show the sub menu and save the choice

def read_record(user):
    """when users choose 2.Continue your game!"""
    try:#avoid the IOError(there is no file called record.txt)
        with open("record.txt","r") as input:
            index=input.readlines()
            user.position[0]=index[0]#get the position
            user.position[1]=index[1]
            user.map[:]="_"
            user.map[user.position[0],user.position[1]]="O"#show the map
            po=index[2:]
            for i in po:#get the pokemon users already have
                user.pokemon.append(i[:(len(i)-1)])
            print "You have already read your record, continue your adventure!!"
            print "\n","\n"
            return True
    except IOError:
        print "You do not have the record, please start a new game"
        print
        return False

def main():
    user=game_adventurer()#get the object for game_adventurer class
    try:
        choose_1=menu()#show the main menu
        while(choose_1!=3):
            if(choose_1==1):#1.Start your new adventure!
                get_first_pokemon(user)#run the get_first_pokemon(user) function
                start_game(user)#run the start_game(user) function
                break
            elif(choose_1==2):#2.Continue your game!
                if (read_record(user)):#check have record.txt or not  
                    start_game(user)#run the start_game(user) function
                    break
                    break  
                else:
                    next
                    main()#run the main function again
                    break 
            else:
                print "Please enter the number 1-3"
                print
                main()#run the main function again
    except ValueError:
        print "Please enter the number 1-3! Not the characters!"
        print
        main()#run the main function again
    print "Goodbye!"
    
if __name__ == "__main__":
    main()    
        