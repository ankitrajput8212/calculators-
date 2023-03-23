import random

def print_random_color(text):
    # generate random color code
    color_code = "\033[38;5;" + str(random.randint(0, 255)) + "m"
    # print text with color
    print(color_code + text + "\033[0m")

while True:
    # main program
    print_random_color("Choose Any Option : ")
    print_random_color("1. ADDITION")
    print_random_color("2. SUBTRACTION")
    print_random_color("3. MULTIPLICATION")
    print_random_color("4. Division")
    print_random_color("5. EXIT")
    print_random_color("\nCreated by Karan")
    print_random_color("⊛✴✹❋❀✿✽❁✺✻✼✾")
    print_random_color("Hello Guys, I'm Karan & This is my First Project in Python, I Hope you Like it...!!!")
    print_random_color("\nConnect with me:\n")
    print_random_color("Instagram: https://www.instagram.com/kkumar04600/")
    print_random_color("Facebook: https://www.facebook.com/kkumar04600/")
    print_random_color("Github: https://github.com/kkumar046000\n")

    option = input("Enter Any Option: ")

    if option == "5":
        # user chose to exit
        print_random_color("Thank you for using the program. Goodbye!")
        break
    
    if option not in ["1", "2", "3", "4"]:
        print_random_color("Invalid input. Please enter a valid option (1-4).")
    else:
        a = int(input("Enter First Number: "))
        b = int(input("Enter the Second Number: "))
        if option == "1":
            sum = a + b
            print_random_color("Sum is " + str(sum))
        elif option == "2":
            sub = a - b
            print_random_color("Sub is " + str(sub))
        
elif option == "3":
            M = a * b
            print_random_color("Multiplication is " + str(M))
        elif option == "4":
            if b == 0:
                print_random_color("Cannot divide by zero.")
            else:
                D = a / b
                print_random_color("Division is " + str(D))
Footer
