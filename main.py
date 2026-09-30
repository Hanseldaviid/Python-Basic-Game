import random

#Let's build a rock, paper, scissors
print("")



print("\n===Welcome to the game===")
print("= = = M E N U = = = ")
print("1) ROCK ")
print("2) PAPER ")
print("3) SCISSORS ")
print("4) EXIT")

victories_player = 0
victories_pc = 0

#Let's ask to the user for the option
print()


while True:
    while True:
        try:
            player_choice = int(input("Select the option user: (1-4) "))
            pc_choice = random.randint(1,3)   
            if 1 <= player_choice <= 4:
                break
            else:
                print("Please, enter only numbers: ")
        except ValueError:
                print("Insert valid digits")
                
    match player_choice:
        case 1: # ROCK
            match pc_choice:
                case 2: # PAPER
                    print("Paper kill rock. pc_choice win ")
                    victories_pc += 1
                case 3: # SCISSORS 
                    print("Scissors does not kill rock. player_choice win ")
                    victories_player += 1
                case 1:
                    print(" = = TIE! = = ")
                      
        case 2: # PAPER
            match pc_choice:
                case 1: # ROCK
                    print("Paper kills rock. player_choice win ")
                    victories_player += 1
                case 3: # SCISSORS
                    print("Scissors kills paper. pc_choice win ") 
                    victories_pc += 1
                case 2:
                    print(" = = TIE = = ")   
                       
        case 3: # SCISSORS
            match pc_choice: 
                case 1: # ROCK 
                    print("Rock kills scissors. pc_choice win ")
                    victories_pc += 1
                case 2: # PAPER 
                    print("Paper does not kill scissors. player_choice win ")
                    victories_player += 1  
                case 3:
                    print(" = = TIE = = ")   
                               
        case 4:
            if player_choice == 4:
                print("Exiting of the program...")
                break
        case _: 
            print("Invalid option") 
                     
        
print("\n")

print("Who ya got? ")

if victories_player > victories_pc:
    print("User has won the battle. Good job")
    print(" = = ")
    print(f"Amout of victories for the user: {victories_player}")
else:
    print("Pc has won the battle. Try it again") 
    print(" = = ")
    print(f"Amount of victories for the pc: {victories_pc}")    
    
print("Print final results: ") 
print(f"User victories: {victories_player}")
print(f"Pc victories: {victories_pc}")                       