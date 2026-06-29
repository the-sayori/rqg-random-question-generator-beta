from openai import OpenAI
import random
from fractions import Fraction

def check_division_answer(user_input, correct_numerator, correct_denominator):
    user_input = user_input.replace(" ", "")
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
            raise SystemExit(1)
    return(inp)


def list_of_operation(difficulty):
    operations = ["adding", "subtracting"]
    if difficulty == 1:
        operations.extend(["dividing","multiplying", "exponentiating"])
    else:
        pass
    return operations

def operation_determiner(difficulty,user_operation):
    operations = list_of_operation(difficulty)
    if user_operation.lower() in operations:
        operations = [user_operation.lower()]
        print("u have choose the operation", user_operation.lower())
    else:
        try:
            user_operation = int(user_operation)
            if 0<=user_operation-1<len(operations) :
                operations = [operations[user_operation-1]]
                print("u have choose the operation", operations[0])
            else:
                wrong_input = input("u have not choose a valid operation, y for choose again, n for random operation")
                if wrong_input.strip().lower() == "y":
                    return None
                else:
                    return list_of_operation(difficulty)
        except ValueError:
                if user_operation.lower() in ["", "none", "any", "random", "CR"]:
                    print("u have choose random operation")
                else:
                    wrong_input = input("u have not choose a valid operation, y for choose again, n for random operation")
                    if wrong_input.strip().lower() == "y":
                        return None
                    else:
                        return list_of_operation(difficulty)
    return operations

def operation_asking(difficulty):
    operations = list_of_operation(difficulty)
    print("choose the operation \n (enter either the number or the word, press CR or type random/none/any for random operation) ")
    for ind,op in enumerate (operations):
        print(ind+1, op)
    user_operation = input("").lower().strip()
    return user_operation


def school_1_easy_question_generator():
    operations = None
    while operations is None:
        user_operations = operation_asking(0)
        operations = operation_determiner(0, user_operations)
##easy-question-generator
    operation = random.choice(operations)
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
    user_answer = input(f"What is {num1} {symbol} {num2}? ").strip()
    user_answer = transform(user_answer, int, "invalid input, enter a number.", 0)
    if user_answer == answer:
        print("Correct!")
    else:
        print("Incorrect.the correct answer is:", answer)



def school_2_medium_question_generator():
    operations = None
    while operations is None:
        user_operations = operation_asking(1)
        operations = operation_determiner(1, user_operations)
##medium-question-generator
    operation = random.choice(operations)
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
    user_answer = input(f"What is {num1} {symbol} {num2}? {tips} ").strip()
    try:
        user_answer = float(user_answer)
    except ValueError:
        if operation == "dividing":
            if check_division_answer(user_answer.strip(), num1, num2):
                user_answer = answer
            else:
                print("Incorrect, the correct answer is:", answer)
                return
        else:
            print("Invalid input. Please enter a number.")
            return
    if abs(user_answer - answer) < 5e-3:
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
    difficulty_1 = input(
        "choice of difficulty (in numbers!) \n"
        "1. elementary school \n"
        "2. middle school(placeholder) \n"
        "3. high school(placeholder) \n"
        "4. college(placeholder) \n"
        "5. university(placeholder) \n"
    ).strip()
    difficulty_1 = transform(difficulty_1, int, "invalid input, please enter a number between 1 to 5.", 0)

    if difficulty_1 < 1 or difficulty_1 > 5:
        print("Invalid input. Please enter a number between 1 and 5.")
        raise SystemExit(1)

    if difficulty_1 == 1:
        difficulty = input(
            "u have chosen the difficulty : elementary school \n"
            "choice of difficulty (in numbers!) \n"
            "1. easy \n"
            "2. medium \n"
            "3. hard(placeholder) \n"
        ).strip()

        difficulty = transform(difficulty, int, "invalid input, please enter a number between 1 and 3", 0)
        if difficulty == 1 :
            school_1_easy_question_generator()
        elif difficulty == 2 :
            school_2_medium_question_generator()
        else:
            print("not complete yet")
            raise SystemExit(0)
    else:
        print("not complete yet")
        raise SystemExit(0)


if __name__ == "__main__":
    main()
