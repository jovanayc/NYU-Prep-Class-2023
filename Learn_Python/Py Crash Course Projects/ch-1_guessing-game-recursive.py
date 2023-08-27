#From ChatGPT -- Recursive
#Aug 16, 2023
import random

num_range_min = 0
num_range_max = 50

def get_computer_num():
    return random.randint(num_range_min, num_range_max)

def get_user_num():
    while True:
        try:
            user_n = int(input(f"I'm thinking of a number between 0 and 50 (integers only)! Try to guess the number I'm thinking of: "))
            if num_range_min <= user_n <= num_range_max:
                return user_n
            else:
                print(f"Invalid range entry. Please enter a number between {num_range_min} and {num_range_max}.")
        except ValueError:
            print("Invalid type entry. Make sure to enter an integer.")

def compare_numbers(computer_n, user_n):
    if user_n > computer_n:
        user_n = int(input("\nToo high! Guess again: "))
        compare_numbers(computer_n, user_n)
    elif user_n < computer_n:
        user_n = int(input("\nToo low! Guess again: "))
        compare_numbers(computer_n, user_n)
    else:
        print("Congratulations! You guessed the correct number.")

def main(): 
    print("\nMAIN FUNCTION")
    computer_num = get_computer_num()
    print(f"Computer number: {computer_num}")
    
    user_num = get_user_num()
    
    compare_numbers(computer_num, user_num)
    
    restart = input("\nWould you like to play again? (Yes/No): ").lower()
    if restart == 'yes':
        main()
    else:
        print("\nSee you next time!")

if __name__ == "__main__":
    main()
