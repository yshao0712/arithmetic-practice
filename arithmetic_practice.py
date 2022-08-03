import random
from fpdf import FPDF

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

def generate_page(path,type,q_num):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 14)

    answers = FPDF()
    answers.add_page()
    answers.set_font("Arial", size = 14)

    for i in range(q_num):
        number = str(i + 1)
        if type == "multiplication":
            problem, answer = generate_multiplication()
        elif type == "addition":
            problem, answer = generate_addition()
        pdf.cell(200, 10, txt = number + ". " + problem,
            ln = 1, align = 'L')
        answers.cell(200, 10, txt = number + ". " + str(answer),
            ln = 1, align = 'L')

    pdf.output(name = path + "problems.pdf", dest = "F")
    answers.output(name = path + "answers.pdf", dest = "F")
