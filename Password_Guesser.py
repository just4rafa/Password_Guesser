import random
import pyautogui
import string

# chars = "abcdefghijklmnopqrstuvwxyz0123456789"
chars = string.printable
chars_list = list(chars)

password = pyautogui.password("Enter a password : ")
guess_password = ""
 
len_passwd = len(password)
nr_ev_loops = 0
nr_loops = 0

while(guess_password != password):
    nr_ev_loops += 1
    guess_password = random.choices(chars_list, k = len(password))

    print("<====================" + str(guess_password) + "====================>")
    if nr_ev_loops == len_passwd:
        nr_ev_loops = 0
        nr_loops +=1

    if (guess_password == list(password)):
        print("Your password is : " + "".join(guess_password) + " | Guessed in " + str(nr_loops) + " tries")
        break
