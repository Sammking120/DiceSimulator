import random


def roll_dice(amount: int =2 ):
    if amount<= 0:
        raise ValueError
    
    rolls: list[int] =[]
    for i in range(amount):
        random_roll =int(random.randint(1,6))
        rolls.append(random_roll)
    #print("Total sum is: " ,sum(rolls)) 
    return rolls

def main():
    while True:
        try:
            user_input: str = input("How many dice would you like to roll? ")

            if user_input.lower() == 'exit':
                print('Thanks for Playing')
                break
            else:
                print(*roll_dice(int(user_input)),sep=', ' )
                total=roll_dice(int(user_input))
                print("The total sum of the output is: ", sum(total))
                
        except ValueError:
            print('Please enter a valid number')


if __name__== '__main__':
    main()