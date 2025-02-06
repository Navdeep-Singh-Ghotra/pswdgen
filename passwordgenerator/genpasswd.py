""" import string;
import random;

#  Get lenght of password
length = int(input('enter password lenghth :'))

# Get the combination of digits and special characters
print(''' Choose characterset for password from
      1. Digits
      2. Letters
      3. Special characters
      4. Exit
      ''')

characterList = ''

# Get characters for password
while(True):
    choice = int(input('pick a number'))
    if(choice == 1):
        characterList += string.ascii_letters
    elif(choice==2):
        characterList += string.digits
    elif(choice==3):
        characterList += string.punctuation
    elif(choice==4):
        break
    else:
        print("Invalid choice")
password = []

print(characterList)

#randomize the password

for i in range(length):
    randomchar = random.choice(characterList)
    password.append(randomchar)

print('lenght is :',length)
print("password is :", "".join(password)) """
