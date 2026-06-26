from openai import OpenAI
import random
from fractions import Fraction

def check_division_answer(user_input, correct_numerator, correct_denominator):
    correct = Fraction(correct_numerator, correct_denominator)
    try:
        user_frac = Fraction(user_input)
    except ValueError:
        return False 
    except ZeroDivisionError:
        return False
    return user_frac == correct

def transform(inp, typ, errmsg,retry):
    try:
        inp = typ(inp)
    except ValueError:
        if retry == 1:
            inp = None
        else:
            print(errmsg)
            raise SystemExit






def elementary_school_easy_question_generator(choose_operation_elementary_easy):
    operation_list_elementary_easy = ["adding", "subtracting"]
    if choose_operation_elementary_easy == "1":
        operation_list_elementary_easy = ["adding"]
    elif choose_operation_elementary_easy == "2":
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
        num1 = random.randint(10, 20)
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
    if choose_operation_elementary_medium.lower() == "1":
        operation_list_elementary_medium = ["adding"]
    elif choose_operation_elementary_medium.lower() == "2":
        operation_list_elementary_medium = ["subtracting"]
    elif choose_operation_elementary_medium.lower() == "3":
        operation_list_elementary_medium = ["multiplying"]
    elif choose_operation_elementary_medium.lower() == "4":
        operation_list_elementary_medium = ["dividing"]
    elif choose_operation_elementary_medium.lower() == "5":
        operation_list_elementary_medium = ["exponentiating"]
    else :
        pass
##medium-question-generator
    operation = random.choice(operation_list_elementary_medium)
    if operation == "adding":
        num1 = round(random.uniform(1, 100),2)
        num2 = round(random.uniform(1, 100),2)
        answer = num1 + num2
    elif operation == "subtracting":
        num1 = round(random.uniform(1, 100),2)
        num2 = round(random.uniform(1, 100),2)
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
    tips = {
    "adding": "(2 decimal places)",
    "subtracting": "(2 decimal places)",
    "multiplying": "",
    "dividing": "enter division either as a fraction a/b or as a decimal",
    "exponentiating": "",
    }[operation]
    elementary_user_medium = input(f"What is {num1} {symbol} {num2}? {tips} ")
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

#ai is currently not in use, but it will be used in the future
def ai(x):
    client = OpenAI(
        api_key="placeholder_api_key",  ## ur API key
        base_url="placeholder_base_url" ## ur base url
    )
    response = client.chat.completions.create(
        model="placeholder",  ## ur model name
        messages=[
            #{"role": "user", "content": "placeholder_content"}
        ],
        reasoning_effort="none",
        max_tokens=100
    )
    return response.choices[0].message.content



def main():
    school_level = input(
        "choice of difficulty (in numbers!) \n"
        "1. elementary school \n"
        "2. middle school(placeholder) \n"
        "3. high school(placeholder) \n"
        "4. collage(placeholder) \n"
        "5. university(placeholder) \n"
    )

    try:
        school_level = int(school_level)
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        raise SystemExit(1)

    if school_level < 1 or school_level > 5:
        print("Invalid input. Please enter a number between 1 and 5.")
        raise SystemExit(1)

    if school_level == 1:
        difficulty_elementary = input(
            "u have choose the difficulti : elementary school \n"
            "choice of difficulty (in numbers!) \n"
            "1. easy \n"
            "2. medium \n"
            "3. hard(placeholder) \n"
        )
        try:
            difficulty_elementary = int(difficulty_elementary)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")
            raise SystemExit(1)
        if difficulty_elementary == 1 :
            choose_operation_elementary_easy = input(
                "choose the operation (CR for random operation) \n"
                "1. adding \n"
                "2. subtracting \n"
            )
            elementary_school_easy_question_generator(choose_operation_elementary_easy)
        elif difficulty_elementary == 2 :
            choose_operation_elementary_medium = input(
                "choose the operation (CR for random operation) \n"
                "1. adding \n"
                "2. subtracting \n"
                "3. multiplying \n"
                "4. dividing \n"
                "5. exponentiating \n"
            )
            elementary_school_medium_question_generator(choose_operation_elementary_medium)
        else:
            print("not complete yet")
            raise SystemExit(0)
    else:
        print("not complete yet")
        raise SystemExit(0)


if __name__ == "__main__":
    main()