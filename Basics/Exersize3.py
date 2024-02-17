"""   
Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.

Python has two functions designed for accepting data directly from the user:

Python 2.x. -> raw_input()
Python 3.x. -> input()
raw_input():

raw_input() asks the user for a string of data and simply returns the string, the string data ended with a newline). 
It can also take an argument, which is displayed as a prompt before the user enters the data.

print raw_input('Input your name: ') 
prints out

Input your name: <user input data here>
To assign the user's name to a variable "x" you can use following command :

x = raw_input('Input your name: ') 
input():

In 3.x .raw_input() is renamed to input(). input() function reads a line from sys.
stdin and returns it with the trailing newline stripped.

To assign the user's name to a variable "y" you can use following command :

y = input('Input your name: ') 


"""

fname = input("Input your First Name :")

lname = input("Input your Last Name :")

print("Hello " + fname + "" + lname)