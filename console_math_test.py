import random

def generate_addition():
    if random.randint(1,2) == 1:
        a = random.randint(10, 1000)
        b = random.randint(10, 1000)
        equation = str(a) + " + " + str(b) + " ="
        answer = a + b
    else:
        a = random.randint(10, 1000)
        b = random.randint(10, 1000)
        equation = str(a) + " - " + str(b) + " ="
        answer = a - b
    return(equation,answer)

def generate_multiplication():
    if random.randint(1,2) == 1:
        a = random.randint(10, 200)
        b = random.randint(10, 200)
        equation = str(a) + " • " + str(b) + " ="
        answer = a * b
    else:
        a = random.randint(1,50)
        b = random.randint(100, 1000)
        equation = str(a) + " • " + str(b) + " ="
        answer = a * b
    return(equation,answer)

def start_test(q_num):
    correct = 0
    for i in range(q_num):
        number = str(i + 1)
        ptype = random.choice(["addition", "multiplication"])
        if ptype == "multiplication":
            problem, answer = generate_multiplication()
        elif ptype == "addition":
            problem, answer = generate_addition()
        user_answer = input(number + ". " + problem + " ")
        if int(user_answer) == answer:
            print("Correct")
            correct += 1
        else:
            print("Incorrect")
    print(f"correct: {correct}/{q_num}\t percent: {100.0*correct/q_num}%")

if __name__ == '__main__':
    start_test(5)