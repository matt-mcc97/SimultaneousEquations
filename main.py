import random
from math import gcd

def generate_answers(decimals = True, negatives = True):

    x_answer = random.randint(1, 10)   # Generate random integer between 0 - 10
    y_answer = random.randint(1, 10)   # Generate random integer between 0 - 10

    if decimals:
        x_make_decimal = random.randint(1, 4)
        y_make_decimal = random.randint(1, 4)

        if x_make_decimal == 4:
            x_answer -= 0.5

        if y_make_decimal == 4:
            y_answer -= 0.5

    if negatives:   # Decides whether to make x or y a negative answer
        x_negative = random.randint(0, 1)
        y_negative = random.randint(0, 1)

        if x_negative:
            x_answer *= -1  # Make negative if true

        if y_negative:
            y_answer *= -1  # Make negative if true

    return x_answer, y_answer

def generate_coefficients(negative_coefficients = True):
    x1 = random.randint(2, 8)
    y1 = random.randint(2, 8)

    if negative_coefficients:
        x_negative = random.randint(1, 4)
        y_negative = random.randint(1, 4)

        if x_negative == 4:
            x1 *= -1

        if y_negative == 4:
            y1 *= -1

    return x1, y1

def print_equations(x1, x2, y1, y2, x_answer, y_answer):
    answer_1 = x1 * x_answer + y1 * y_answer
    answer_2 = x2 * x_answer + y2 * y_answer

    if (answer_1).is_integer():
        answer_1 = int(answer_1)

    if (answer_2).is_integer():
        answer_2 = int(answer_2)

    x1_output = x1
    y1_output = y1
    x2_output = x2
    y2_output = y2

    if x1 == 1:
        x1_output = ""

    if y1 == 1:
        y1_output = ""

    if x2 == 1:
        x2_output = ""

    if y2 == 1:
        y2_output = ""

    if y1 < 0 or y2 < 0:
        print(f'{x1_output}x - {abs(y1)}y = {answer_1}')

    else:
        print(f'{x1_output}x + {y1_output}y = {answer_1}')

    if y2 < 0:
        print(f'{x2_output}x - {abs(y2)}y = {answer_2}')

    else:
        print(f'{x2_output}x + {y2_output}y = {answer_2}')

    print(f'Answers: x = {x_answer}, y = {y_answer}')



def generate_eqs_one_term_same(decimals = True, negatives = True, negative_coefficients = True):
    x_answer, y_answer = generate_answers(decimals = decimals, negatives = negatives)

    x1, x2, y1, y2 = 0, 0, 0, 0

    while x1 == x2 or y1 == y2:
        x1, y1 = generate_coefficients(negative_coefficients = negative_coefficients)
        x2, y2 = generate_coefficients(negative_coefficients = negative_coefficients)

    make_coefficient_same = random.randint(0,1)

    if make_coefficient_same:
        x1 = x2

    else:
        y1 = y2

    print_equations(x1=x1, x2=x2, y1=y1, y2=y2, x_answer=x_answer, y_answer=y_answer)

def generate_eqs_multiply_one(decimals = True, negatives = True, negative_coefficients = True):

    x_answer, y_answer = generate_answers(decimals = decimals, negatives = negatives)

    x1, x2, y1, y2 = 0, 0, 0, 0

    while x1 == x2 or y1 == y2:
        x1, y1 = generate_coefficients(negative_coefficients=negative_coefficients)
        x2, y2 = generate_coefficients(negative_coefficients=negative_coefficients)

    make_x_suitable = random.randint(0,1)

    list_chooser = random.randint(1, 4)
    if list_chooser == 1:
        suitable_coefficients = [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8)]
    else:
        suitable_coefficients = [(2, 4), (2, 6), (2, 8), (2, 10), (3, 6), (3, 9), (4, 8), (5, 10)]

    list_selector = random.randint(0,len(suitable_coefficients)-1)

    if make_x_suitable:
        x1, x2 = suitable_coefficients[list_selector]

    else:
        y1, y2 = suitable_coefficients[list_selector]

    equations_solveable = True

    if x1/x2 == y1/y2:
        equations_solveable = False

    if equations_solveable:
        print_equations(x1=x1, x2=x2, y1=y1, y2=y2, x_answer=x_answer, y_answer=y_answer)

    return equations_solveable

def generate_eqs_multiply_two(decimals  = True, negatives = True, negative_coefficients = True):
    x_answer, y_answer = generate_answers(decimals=decimals, negatives=negatives)

    x1, x2, y1, y2 = 2, 2, 2, 2
    while gcd(x1, x2) != 1 or gcd(y1, y2) != 1:
        x1, y1 = generate_coefficients(negative_coefficients=negative_coefficients)
        x2, y2 = generate_coefficients(negative_coefficients=negative_coefficients)

    equations_solveable = True

    if equations_solveable:
        print_equations(x1=x1, x2=x2, y1=y1, y2=y2, x_answer=x_answer, y_answer=y_answer)

    return equations_solveable


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print("What type of simultaneous equations do you want to generate?")
    print("1 - Same term in both equations")
    print("2 - Multiply one equation")
    print("3 - Multiply two equations")

    equation_type = 0
    while True:
        try:
            equation_type = int(input("Input your choice: "))
            if equation_type in range(1,4):
                break
            print("That is not a valid choice.")

        except ValueError:
            print("That is not a valid choice.")

    print("Do you want negative answers?")

    negative_answers_check = False
    while True:
        negative_answers_check_yn = ((input("Input your choice [Y/n]: ")))[0].lower()
        if negative_answers_check_yn == "y" or negative_answers_check_yn == "n":
            if negative_answers_check_yn == "y":
                negative_answers_check = True
            break

        print("Invalid choice. Please try again.")


    print("Do you want decimal answers?")
    decimal_answers_check = False
    while True:
        decimal_answers_check_yn = ((input("Input your choice [Y/n]: ")))[0].lower()
        if decimal_answers_check_yn == "y" or decimal_answers_check_yn == "n":
            if decimal_answers_check_yn == "y":
                decimal_answers_check = True
            break

        print("Invalid choice. Please try again.")

    print("Do you want negative coefficients?")
    negative_coefficients_check = False
    while True:
        negative_coefficients_check_yn = ((input("Input your choice [Y/n]: ")))[0].lower()
        if negative_coefficients_check_yn == "y" or negative_coefficients_check_yn == "n":
            if negative_coefficients_check_yn == "y":
                negative_coefficients_check = True
            break

        print("Invalid choice. Please try again.")

    print("How many equations do you want to generate? [1 - 10]")
    number_of_equations = 1
    while True:
        number_of_equations = int(input("Input your choice: "))
        if number_of_equations in range(1, 11):
            break

        print("Choose a valid integer between 1 and 10.")

    for i in range(0, number_of_equations):

        if equation_type == 1:
            output = generate_eqs_one_term_same(decimals=decimal_answers_check, negatives=negative_answers_check, negative_coefficients=negative_coefficients_check)
            print("")
            if output == False:
                 i -= 1

        elif equation_type == 2:
            output = generate_eqs_multiply_one(decimals=decimal_answers_check, negatives=negative_answers_check, negative_coefficients=negative_coefficients_check)
            print("")
            if output == False:
                 i -= 1

        else:
            output = generate_eqs_multiply_two(decimals=decimal_answers_check, negatives=negative_answers_check, negative_coefficients=negative_coefficients_check)
            print("")
            if output == False:
                 i -= 1
