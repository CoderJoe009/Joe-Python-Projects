import random

def main():
    level = get_level()
    score = generate_problems(level)
    print("Score: ",score)

def get_level():
    while True:
        level = input("Level: ")
        if level in ['1', '2', '3']:
            return int(level)

def generate_problems(level):
    score = 0
    for _ in range(10):
        equation,answer = generate_integer(level)
        attempts = 0
        while attempts < 3:
            user_answer = input(equation)
            if user_answer.isdigit():
                user_answer = int(user_answer)
                if user_answer == answer:
                    score += 1
                    break
                else:
                    print('EEE')
            else:
                print('EEE')
            attempts += 1
        else:
            print(answer)
    return score

def generate_integer(level):
    if level == 1:
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
    elif level == 2:
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
    else:  # level 3
        num1 = random.randint(100, 999)
        num2 = random.randint(100, 999)
    operators =  ['+', '-', '*', '/']
    operator = random.choice(operators)
    equation = f"{num1} {operator} {num2} = "
    answer = eval(f"{num1} {operator} {num2}")
    return equation, answer

if __name__ == "__main__":
    main()