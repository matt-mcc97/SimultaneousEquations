import random
from math import gcd


def generate_answers(decimals=True, negatives=True):
    x_answer = 1
    y_answer = 1

    while x_answer == y_answer:
        x_answer = random.randint(1, 5)  # Generate random integer between 0 - 10
        y_answer = random.randint(1, 5)  # Generate random integer between 0 - 10


    make_x_bigger = random.randint(1, 5)
    make_y_bigger = random.randint(1, 5)
    
    if make_x_bigger == 5:
        x_answer += 4
        
    if make_y_bigger == 5:
        y_answer += 4

    if decimals:
        x_make_decimal = random.randint(1, 4)
        y_make_decimal = random.randint(1, 4)

        if x_make_decimal == 1:
            x_answer -= 0.5

        if y_make_decimal == 1:
            y_answer -= 0.5

    # This greats a 1 in 4 chance of each answer being a decimal

    if negatives:  # Decides whether to make x or y a negative answer
        x_negative = random.randint(1, 3)
        y_negative = random.randint(1, 3)

        if x_negative == 1:
            x_answer *= -1  # Make negative if true

        if y_negative == 1:
            y_answer *= -1  # Make negative if true

    # This creates a 1 in 3 chance of making x negative and a 1 in 3 chance of making y negative

    return x_answer, y_answer


def generate_coefficients(negative_coefficients=True):
    x1 = random.randint(2, 4)
    y1 = random.randint(2, 4)
    
    make_x_bigger = random.randint(1, 5)
    make_y_bigger = random.randint(1, 5)
    
    if make_x_bigger == 5:
        x1 += 4
        
    if make_y_bigger == 5:
        y1 += 4

    if negative_coefficients:
        x_negative = random.randint(1, 4)
        y_negative = random.randint(1, 4)

        if x_negative == 4:
            x1 *= -1

        if y_negative == 4:
            y1 *= -1

    # Creates a 1 in 4 chance of the coefficients being negative

    return x1, y1


def print_equations(x1, x2, y1, y2, x_answer, y_answer):
    answer_1 = x1 * x_answer + y1 * y_answer
    answer_2 = x2 * x_answer + y2 * y_answer

    if (answer_1).is_integer():
        answer_1 = int(answer_1)

    if (answer_2).is_integer():
        answer_2 = int(answer_2)

    # These 6 lines of code are for clean up of the output for the answers

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

    # This makes sure 1x is output as x and 1y is output as y

    if y1 < 0:
        print(f'{x1_output}x - {abs(y1)}y = {answer_1}')

    else:
        print(f'{x1_output}x + {y1_output}y = {answer_1}')

    if y2 < 0:
        print(f'{x2_output}x - {abs(y2)}y = {answer_2}')

    else:
        print(f'{x2_output}x + {y2_output}y = {answer_2}')

    # Printing each equation. The <0 check is to make sure negative coefficients are outputted nicely

    print(f'Answers: x = {x_answer}, y = {y_answer}')

    # Prints the answers for x and y


def generate_eqs_one_term_same(decimals=True, negatives=True, negative_coefficients=True):
    x_answer, y_answer = generate_answers(decimals=decimals, negatives=negatives)  # Creates the x and y answers

    x1, x2, y1, y2 = 0, 0, 0, 0  # Initialising the coefficients for while loop check

    while x1 == x2 or y1 == y2:  # This makes sure the two x and two y coefficients are not the same at the start.
        x1, y1 = generate_coefficients(negative_coefficients=negative_coefficients)
        x2, y2 = generate_coefficients(negative_coefficients=negative_coefficients)

    make_coefficient_same = random.randint(0, 1)

    if make_coefficient_same:
        x1 = x2

    else:
        y1 = y2

    # This randomly makes either the x or y coefficient the same

    equations_solveable = True

    if x1 / x2 == y1 / y2:  # This checks that Eq 1 is not a scalar multiple of Eq 2 and hence unsolveable
        equations_solveable = False

    if equations_solveable:
        print_equations(x1=x1, x2=x2, y1=y1, y2=y2, x_answer=x_answer, y_answer=y_answer)  # Prints the output

    return equations_solveable  # This output allows the for loop at the end to skip the equation and generate a new one


def generate_eqs_multiply_one(decimals=True, negatives=True, negative_coefficients=True):
    x_answer, y_answer = generate_answers(decimals=decimals, negatives=negatives)

    x1, x2, y1, y2 = 0, 0, 0, 0

    while x1 == x2 or y1 == y2:
        x1, y1 = generate_coefficients(
            negative_coefficients=negative_coefficients)  # Generates values for x coefficients
        x2, y2 = generate_coefficients(
            negative_coefficients=negative_coefficients)  # Generates values for y coefficients

    make_x_suitable = random.randint(0, 1)  # This decides whether to make x or y the suitable term

    list_chooser = random.randint(1, 4)
    if list_chooser == 1:
        suitable_coefficients = [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8)]
    else:
        suitable_coefficients = [(2, 4), (2, 6), (2, 8), (2, 10), (3, 6), (3, 9), (4, 8), (5, 10)]

    # Since there is roughly a 50% chance of one of the chosen pairs being a 1, this makes the likelyhood 1 in 4.

    list_selector = random.randint(0,
                                   len(suitable_coefficients) - 1)  # Chooses a random pair of coefficients fron the list

    if make_x_suitable:
        x1, x2 = suitable_coefficients[list_selector]  # assigns the tuple from the list to the x coefficients

    else:
        y1, y2 = suitable_coefficients[list_selector]  # assigns the tuple from the list to the y coefficients

    equations_solveable = True

    if x1 / x2 == y1 / y2:  # This checks that Eq 1 is not a scalar multiple of Eq 2 and hence unsolveable
        equations_solveable = False

    if equations_solveable:
        print_equations(x1=x1, x2=x2, y1=y1, y2=y2, x_answer=x_answer, y_answer=y_answer)  # Prints the output

    return equations_solveable  # This output allows the for loop at the end to skip the equation and generate a new one


def generate_eqs_multiply_two(decimals=True, negatives=True, negative_coefficients=True):
    x_answer, y_answer = generate_answers(decimals=decimals, negatives=negatives)  # Assigns x and y answers

    x1, x2, y1, y2 = 2, 2, 2, 2
    while gcd(x1, x2) != 1 or gcd(y1, y2) != 1:
        x1, y1 = generate_coefficients(negative_coefficients=negative_coefficients)
        x2, y2 = generate_coefficients(negative_coefficients=negative_coefficients)

    # This checks that the x and y coefficients are coprime before proceeding

    equations_solveable = True

    if x1 / x2 == y1 / y2:  # This checks that Eq 1 is not a scalar multiple of Eq 2 and hence unsolveable
        equations_solveable = False

    if equations_solveable:
        print_equations(x1=x1, x2=x2, y1=y1, y2=y2, x_answer=x_answer, y_answer=y_answer)  # Prints the output

    return equations_solveable  # This output allows the for loop at the end to skip the equation and generate a new one


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
            if equation_type in range(1, 4):
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
            output = generate_eqs_one_term_same(decimals=decimal_answers_check, negatives=negative_answers_check,
                                                negative_coefficients=negative_coefficients_check)
            print("")
            if output == False:
                i -= 1

        elif equation_type == 2:
            output = generate_eqs_multiply_one(decimals=decimal_answers_check, negatives=negative_answers_check,
                                               negative_coefficients=negative_coefficients_check)
            print("")
            if output == False:
                i -= 1

        else:
            output = generate_eqs_multiply_two(decimals=decimal_answers_check, negatives=negative_answers_check,
                                               negative_coefficients=negative_coefficients_check)
            print("")
            if output == False:
                i -= 1
