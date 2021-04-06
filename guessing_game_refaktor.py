import random


def main(): 
    checking_guessed_numbers(100)
    checking_guessed_numbers(50)


def random_number(number):
    random_number = random.randint(1, number)
    return random_number


def get_random_numbers(num):
    random_numbers = random.sample(range(1, num), 10)
    return random_numbers


def get_user_input(max_num):
    return int(input(f"Enter an integer from 1 to {max_num}: "))


def checking_guessed_numbers(num):
    rand_numbers = get_random_numbers(num)
    print(rand_numbers)
    for index in range(len(rand_numbers)):
        guessed_number = 0
        while rand_numbers[index] != guessed_number:
            guessed_number = get_user_input(num-1)
            if guessed_number < rand_numbers[index]:
                print("guess is low")
            elif guessed_number > rand_numbers[index]:
                print("guess is high")
            else:
                break
        print("you guessed it!")


if __name__ == '__main__':
    main()