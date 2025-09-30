history_file = "calculator with history/history.txt"
import re
# history_file = "history.txt"

def show_history():
    file = open(history_file,'r')
    lines = file.readlines()

    if len(lines) != 0:
        for line in reversed(lines):
            print(line.strip())
    else:
        print('No history found!')
    file.close()

def clear_history():
    file = open(history_file,'w')
    print('history cleared.')
    file.close()

def save_to_history(eq,result):
    file = open(history_file,'a')
    file.write(eq + " = " + str(result) + "\n")
    file.close()

def calculate(user_input):
    user_input = re.sub(r'([+\-*/])', r' \1 ', user_input)
    parts = user_input.split()
    if len(parts) != 3:
        print('Invalid input. Use format: Number , Operator , Number (e.g 8 + 8 ) = ')
        return
    num1 = float(parts[0])
    operand = parts[1]
    num2 = float(parts[2])
    
    if operand == "+":
        result = num1 + num2 
    elif operand == "-":
        result = num1 - num2
    elif operand == "*":
        result = num1 * num2
    elif operand == "/":
        if num2 == 0:
            print("Can't divide by zero")
            return
        result = num1 / num2
    else:
        print('Invalid operator. USE ONLY + - * /. ')
        return 
    
    if int(result) == result:
        result = int(result)
        
    print('Result: ', result)
    save_to_history(user_input , result)

def main():
    print("--------SIMPLE CALCULATOR (type history, clear , exit) = ")
    while True:
        user_input = input('Enter Calculator (+ - * / ) or command (history , clear , exit) = ')
        
        if user_input == "exit":
            print("Goodbye")
            break
        elif user_input == 'history':
            show_history()
        elif user_input == 'clear':
            clear_history()
        else:
            calculate(user_input)

main()