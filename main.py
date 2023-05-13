import random
import os
from art import logo


letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '!@#$%^&*()'
numbers = '0123456789'


print(logo)
while True:
	while True:
		while True:
			try:
				nr_letters = int(input("\nHow many letters would you like in your password?\n"))
				break
			except ValueError:
				print("Invalid input. Numbers only.")
		while True:
			try:
				nr_symbols = int(input(f"\nHow many symbols would you like?\n"))
				break
			except ValueError:
				print("Invalid input. Numbers only.")
		while True:
			try:
				nr_numbers = int(input(f"\nHow many numbers would you like?\n"))
				break
			except ValueError:
				print("Invalid input. Numbers only.")

		letter_string = ''.join(random.choice(letters) for _ in range(nr_letters))
		symbol_string = ''.join(random.choice(symbols) for _ in range(nr_symbols))
		number_string = ''.join(random.choice(numbers) for _ in range(nr_numbers))

		password = f"{letter_string}{symbol_string}{number_string}"
		char_list = list(password)
		random.shuffle(char_list)
		shuffled_password = ''.join(char_list)

		print(f"\nYour password is:\n{shuffled_password}")
		while True:
			play_again = input("\nDo you want to generate another password? (y/n): ").lower()
			if play_again == "y":
				os.system('cls' if os.name == 'nt' else 'clear')
				break
			elif play_again == "n":
				print("Goodbye.")
				exit()
			else:
				print("Invalid input. 'y' or 'n' only.")
		break