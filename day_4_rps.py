import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input('type 0 for rock | 1 for paper | 2 for scissors: '))

computer_choice = random.randint(0,2)

if user_choice == 0:
    print(f'user chose: {rock}')
elif user_choice == 1:
    print(f'user chose: {paper}')
elif user_choice == 2:
    print(f'user chose: {scissors}')
else:
    print('error')

if computer_choice == 0:
    print(f'computer chose: {rock}')
elif computer_choice == 1:
    print(f'computer chose: {paper}')
elif computer_choice == 2:
    print(f'computer chose: {scissors}')
else:
    print('error')


if computer_choice == user_choice:
    print('It is a tie - well played.')
elif computer_choice == 0 and user_choice == 2:
    print('Computer wins')
elif computer_choice == 2 and user_choice == 0:
    print('User wins')
elif computer_choice > user_choice:
    print('Computer wins')
elif user_choice > computer_choice:
    print('User wins')
else:
    print('error')