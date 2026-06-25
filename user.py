from openai import OpenAI
import random
from fractions import Fraction

def check_division_answer(user_input, correct_numerator, correct_denominator):
    correct = Fraction(correct_numerator, correct_denominator)
    try:
        user_frac = Fraction(user_input)
    except ValueError:
        return False 
    return user_frac == correct








def elementary_school_easy_question_generator(choose_operation_elementary_easy):
    operation_list_elementary_easy = ["adding", "subtracting"]
    if choose_operation_elementary_easy.lower() == "adding":
        operation_list_elementary_easy = ["adding"]
    elif choose_operation_elementary_easy.lower() == "subtracting":
        operation_list_elementary_easy = ["subtracting"]
    else :
        pass
##easy-question-generator
    operation = random.choice(operation_list_elementary_easy)
    if operation == "adding":
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        answer = num1 + num2
    elif operation == "subtracting":
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        answer = num1 - num2
##answer-determination-easy
    symbol = {
    "adding": "+",
    "subtracting": "-",
    }[operation]
    elementary_user_easy = input(f"What is {num1} {symbol} {num2}? ")
    try:
        elementary_user_easy = int(elementary_user_easy)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    if elementary_user_easy == answer:
        print("Correct!")
    else:
        print("Incorrect.the correct answer is:", answer)

def elementary_school_medium_question_generator(choose_operation_elementary_medium):
    operation_list_elementary_medium = ["adding", "subtracting", "multiplying", "dividing", "exponentiating"]
    if choose_operation_elementary_medium.lower() == "adding":
        operation_list_elementary_medium = ["adding"]
    elif choose_operation_elementary_medium.lower() == "subtracting":
        operation_list_elementary_medium = ["subtracting"]
    elif choose_operation_elementary_medium.lower() == "multiplying":
        operation_list_elementary_medium = ["multiplying"]
    elif choose_operation_elementary_medium.lower() == "dividing":
        operation_list_elementary_medium = ["dividing"]
    elif choose_operation_elementary_medium.lower() == "exponentiating":
        operation_list_elementary_medium = ["exponentiating"]
    else :
        pass
##medium-question-generator
    operation = random.choice(operation_list_elementary_medium)
    if operation == "adding":
        num1 = random.uniform(1, 100)
        num2 = random.uniform(1, 100)
        answer = num1 + num2
    elif operation == "subtracting":
        num1 = random.uniform(1, 100)
        num2 = random.uniform(1, 100)
        answer = num1 - num2
    elif operation == "multiplying":
        num1 = random.randint(1,100)
        num2 = random.randint(1,100)
        answer = num1 * num2
    elif operation == "dividing":
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        answer = num1 / num2
    elif operation == "exponentiating":
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 5)
        answer = num1 ** num2
##answer-determination-medium
    symbol = {
    "adding": "+",
    "subtracting": "-",
    "multiplying": "*",
    "dividing": "/",
    "exponentiating": "^",
    }[operation]
    elementary_user_medium = input(f"What is {num1} {symbol} {num2}? (4 decimal places apart from division) ")
    try:
        elementary_user_medium = float(elementary_user_medium)
    except ValueError:
        if operation == "dividing":
            if check_division_answer(elementary_user_medium.strip(), num1, num2):
                elementary_user_medium = answer
                pass
            else:
                elementary_user_medium=answer + 100
                pass
        else:
            print("Invalid input. Please enter a number.")
            return
    if abs(elementary_user_medium - answer) < 5e-3:
        print("Correct!")
    else:
        print("Incorrect, the correct answer is:", answer)

##ai is currently not in use, but it will be used in the future
def ai(x):
    client = OpenAI(
        api_key="placeholder_api_key",  ## ur API key
        base_url="placeholder_base_url" ## ur base url
    )

    response = client.chat.completions.create(
        model="placeholder",  ## ur model name
        messages=[
            {"role": "user", "content": "placeholder_content"}
        ],
        reasoning_effort="none",
        max_tokens=100
    )

    return response.choices[0].message.content


def main():
    school_level = input(
        "choice of difficulty (in numbers!) \n"
        "1. elementary_school \n"
    )

    try:
        school_level = int(school_level)
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 10.")
        raise SystemExit(1)

    if school_level < 1 or school_level > 10:
        print("Invalid input. Please enter a number between 1 and 10.")
        raise SystemExit(1)

    if school_level == 1:
        difficulty_elementary = input(
            "u have choose the difficulti : elementary school \n"
            "choice of difficulty (in numbers!) \n"
            "1. easy \n"
            "2. medium \n"
        )
        try:
            difficulty_elementary = int(difficulty_elementary)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 2.")
            raise SystemExit(1)
        if difficulty_elementary == 1 :
            choose_operation_elementary_easy = input(
                "choose the operation (in words, put nothing for random operation) \n"
                "1. adding \n"
                "2. subtracting \n"
            )
            elementary_school_easy_question_generator(choose_operation_elementary_easy)
        if difficulty_elementary == 2 :
            choose_operation_elementary_medium = input(
                "choose the operation (in words, put nothing for random operation) \n"
                "1. adding \n"
                "2. subtracting \n"
                "3. multiplying \n"
                "4. dividing \n"
                "5. exponentiating \n"
            )
            elementary_school_medium_question_generator(choose_operation_elementary_medium)


if __name__ == "__main__":
    main()