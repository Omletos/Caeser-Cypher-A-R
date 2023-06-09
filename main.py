'''
  Name: 
  James Hargest College
  Programming Internal for 2.7 & 2.8 ~ 12 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''
from tkinter import *

# Caesar cipher function
def caesar_cipher(text, shift):
    cipher_text = ""
    for char in text:
        if char.isalpha():
            # Shift the letter by the given amount
            new_char_code = ord(char) + shift
            if char.isupper():
                if new_char_code > ord('Z'):
                    new_char_code -= 26
                elif new_char_code < ord('A'):
                    new_char_code += 26
            elif char.islower():
                if new_char_code > ord('z'):
                    new_char_code -= 26
                elif new_char_code < ord('a'):
                    new_char_code += 26
            # Append the shifted letter to the cipher text
            cipher_text += chr(new_char_code)
        else:
            # Append non-alphabetic characters as-is
            cipher_text += char
    return cipher_text

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
shift_label = Label(root, text="Select shift amount:")
shift_label.pack()
shift_var = IntVar()
shift_dropdown = OptionMenu(root, shift_var, *[i for i in range(26)])
shift_dropdown.pack()
shift_dropdown.config(width=20)

# Output label
output_label = Label(root, text="Encrypted text:")
output_label.pack()
output_text = Text(root, width=40, height=4)
output_text.pack()

# Encrypt Function
def encrypt():
    text = text_box.get()
    shift = int(shift_box.get())
    cipher_text = caesar_cipher(text, shift)
    output_text.delete('1.0', END)  # clear previous output
    output_text.insert(END, cipher_text)

#Encrypt Button
encrypt_button = Button(root, text="Encrypt", command=encrypt, bg='#ff0000', fg='#ffffff', activebackground='#db0000', activeforeground= '#d4d4d4')
encrypt_button.pack()



root.mainloop()