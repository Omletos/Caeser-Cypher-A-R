'''
  Name: 
  James Hargest College
  Programming Internal for 2.7 & 2.8 ~ 12 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''
from tkinter import *

# GUI setup
root = Tk()
root.title("Hello World")
root.geometry("300x250")

# Text input box
text_label = Label(root, text="Enter text to encrypt:")
text_label.pack()
text_box = Entry(root, width=40)
text_box.pack()

# Shift input box
shift_label = Label(root, text="Enter shift amount (0-25):")
shift_label.pack()
shift_box = Entry(root, width=20)
shift_box.pack()

# Output label
output_label = Label(root, text="Encrypted text:")
output_label.pack()
output_text = Text(root, width=40, height=4)
output_text.pack()