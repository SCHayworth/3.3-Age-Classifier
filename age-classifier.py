# 3-3 Age Classifier Program
# Shaun Hayworth
# CIS 2
# 10-02-2019

# Prints an age category (infant, child, teenager, or adult) based on an age supplied by the user.

# Prompt the user for an age and store it in the age variable.
age = int(input('Input a person\'s age in years: '))

# Determine which category age fits into, and display the appropriate category onscreen.
if age <= 1:
  print('This person is an infant.')
elif age > 1 and age < 13:
  print('This person is a child.')
elif age >= 13 and age < 20:
  print('This person is a teenager.')
else:
  print('This person is an adult.')
