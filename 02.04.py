
import re

def check_email():
    user_input = input("Введите email\n")
    match_result = re.match('[\w.-]+@[\w.-]+\.\w+', user_input)
    if match_result:
        print("Cпасибо")
    else:
        print("sosi")


check_email()


def check_first():
    [
