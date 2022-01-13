#2) Take a variable with a numeric grade and output the corresponding letter grade
x = 1 
while x > 0:
    x += 1
    Grade_input = int(input("Please input your numeric grade: "))
    if Grade_input < 50:
        print("You got a F")
    elif Grade_input >= 50 and Grade_input < 60:
        print("You got a D")
    elif Grade_input >= 60 and Grade_input < 70:
        print("You got a C") 
    elif Grade_input >= 70 and Grade_input < 80:
        print("You got a B")
    elif Grade_input >= 80 and Grade_input <= 100:
        print("You got an A")
    else:
        print("Please input your real grade")
