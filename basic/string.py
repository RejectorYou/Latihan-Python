import os

os.system("cls")

#Python String

print("hello")
print('hello')

print("'Hello World'")
print('"Hello World"')

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = "Hello, World!"
print("\n\n")
print(a)
print("-Huruf ke 4 : ",a[3])
print("-Total Huruf: ",len(a))
print("\n\n")
print("free" in a)
if "Hello" in a:
    print("Yes, 'Hello' in Variable")
if "Free" not in a:
    print("No, 'free' not in Variable")

print("\n\n")

#Splicing String

b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])

print("\n\n")

#Modify String

a = "Hello, World!"
print(a.upper())
print(a.lower())
print(a.strip()) # returns "Hello, World!"
print(a.replace("H", "J"))
print(a.split(",")) # returns ['Hello', ' World!']

print("\n\n")

#Concatenate String

a="Hello"
b="World"

c=a+b
print(c)
c=a+" "+b
print(c)

print("\n\n")

#Format String

age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

print("\n\n")

#Escape Character

txt = "We are the so-called \"Vikings\" from the north."
print(txt)
print("We are the so-called \'Vikings\' from the north.")
print("We are the so-called \\Vikings\\ from the north.")
#print("We are the so-called \nVikings\n from the north.")
print("Hello\rWorld!")
print("Hello\tWorld!")
print("Hello\bWorld!")
print("Hello\fWorld!")
txt = "\110\145\154\154\157"
print(txt) 
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 

#String Method
"""
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
"""



