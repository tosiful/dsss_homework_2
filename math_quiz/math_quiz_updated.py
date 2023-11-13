import random


def function_A(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)


def function_B():
    return random.choice(['+', '-', '*'])


def function_C(x1, x2, o): #changed the variable
    p = f"{x1} {o} {x2}"
    if o == '+': a = x1 + x2
    elif o == '-': a = x1 - x2
    else: a = x1 * x2
    return p, a

def math_quiz():
    s = 0
    t_q = int (3.1416) #changed the value float to int


    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        x1 = function_A(1, 10);
        x2 = function_A(1, 5);#changed the value float to int
        o = function_B()

        PROBLEM, ANSWER = function_C(x1, x2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
    
