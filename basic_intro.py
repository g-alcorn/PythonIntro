# This is the beginning of my Python Intro tutorial
# Following https://www.youtube.com/watch?v=rfscVS0vtbw

# Hello World
print('Hello World')
# Backslash is escape character
print('Can you believe I don\'t need semicolons for this?')
# print('|\\')
# print('| \\')
# print('|  \\')
# print('|___\\')
# print('Yay, triangle!')

# Variables & Data types
# Basic - string, number, booleans
character_name = 'John'
character_age = 35

print('There was once a character named ' + character_name)
# Use str() to convert int to string for printing
print(character_name + ' was ' + str(character_age) + ' years old')
print('')

# Accessing character inside of a string
print('The final character of the variable is ' + character_name[3])

# Index function
print(str(character_name.index('J')) + ' is the index of the character \'J\' within the variable')

# Replace part of string
print(character_name.replace('hn', 'nny'))
