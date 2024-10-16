#Programme for the "21 number game"
import random

def start():#To start the game
    print("Welcome to the 21 Number game\n")
    print('The rules are:')
    print('1.You can only enter upto 3 numbers and they have to be positive numbers\n2.You have to enter consecutive numbers\n3.if you get 21 in your turn you lose\n')

    print('Enter F to take first chance\nEnter S to take second chance')#asking user for first or second chance
    ch = input('>>> ')
    n_list = list()#creating an empty list for storing the numbers
    if ch == 'F':
        while True:
            #user's turn

            n = int(input("How many numbers do you want to enter?\n>>> "))
            
            if n>0 and n<=3:#checking if the number is between 0 to 3
                comp = 4 - n #the number of values computer is going to give
            else:
                print("Wrong!!\nYou violated rule 1")
                lose()
            
            print("Enter the values")

            for i in range(n):
                number = int(input(">>> "))
                n_list.append(number)#adding the numbers into the list

            
            rule2(n_list)
            consecutive(n_list,n+1)#To check if the numbers are consecutive
            last_number = n_list[-1]#last number added in the list
            check(last_number)

            #Now computer's turn

            for j in range(comp):
                n_list.append(last_number+j+1)
            last_number = n_list[-1]
            print("The input(s) computer gave are:",n_list[-comp::])
            if check1(last_number) == True:
                lose()
            


    elif ch == 'S':
        while True:
            #computer's turn

            comp = random.randint(1,3)
            last_number = lastno(n_list)
            if check1(last_number) == True:
                won()
            
            for i in range(comp):
                n_list.append(last_number+i+1)
            
            print("The input(s) computer gave are:",n_list[-comp::])
            last_number = n_list[-1]
            if check1(last_number) == True:
                lose()
          

            #Now user's turn

            n = int(input("How many numbers do you want to enter?\n>>> "))
            
            if n<0 or n>3:#checking if the number is between 0 to 3
                print("\nWrong!!\nYou violated rule 1")
                lose()
            
            print("Enter the values")

            for i in range(n):
                number = int(input(">>> "))
                n_list.append(number)#adding the numbers into the list

            consecutive(n_list,n+1)#To check if the numbers are consecutive
            last_number = n_list[-1]#last number added in the list
            check(last_number)
    else:
        print("\nWrong Input!!\n")
        lose()


def rule2(n_list):
    if n_list[0] != 1:
        print("Wrong!!\nYou violated rule 2")
        lose()
def won():
    print("\n\nCONGRATULATIONS!!!\nYOU WON\nTHANK YOU FOR PLAYING\nExiting...")
    exit(0)

def lose():
    print('\n\nYOU LOSE!!\nBETTER LUCK NEXT TIME')
    exit(0)

def check(l):
    if l == 21:
        lose()

def check1(l):
    if l == 20:
        return True
    else:
        return False
def consecutive(n_list,n):
    for i in range(1,len(n_list)):
        if n_list[i]-n_list[i-1] != 1:
            print("\nWrong!!\nYou violated rule 2")
            lose()

def lastno(n_list):
    if n_list == []:
        last_number = 0
    else:
        last_number = n_list[-1]
    return last_number

def main():
    while True:
        print ("Player 2 is Computer.")
        print("Do you want to play the 21 number game? (yes / no)")
        inp1 = input('>>> ')
        if inp1 =='yes':
            start()
        else:
            print ("Do you want quit the game?(yes / no)")
            inp2 = input('>>> ')
            if inp2 == "yes":
                print ("You are quitting the game...")
                exit(0)
            elif inp2 == "no":
                print ("Continuing...")
            else:
                print ("Wrong choice")
main()
