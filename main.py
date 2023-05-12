import random
import os

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '!@#$%^&*()'
numbers = '0123456789'

print('''

█▀█ ▄▀█ █▀ █▀ █░█░█ █▀█ █▀█ █▀▄
█▀▀ █▀█ ▄█ ▄█ ▀▄▀▄▀ █▄█ █▀▄ █▄▀

█▀▀ █▀▀ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀█ █▀█
█▄█ ██▄ █░▀█ ██▄ █▀▄ █▀█ ░█░ █▄█ █▀▄


▅▄▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▃▄▅

''')

while True:
	while True:
		while True:
			try:
				nr_letters = int(input("How many letters would you like in your password?\n"))
				break
			except ValueError:
				print("Invalid input.")
		while True:
			try:
				nr_symbols = int(input(f"How many symbols would you like?\n"))
				break
			except ValueError:
				print("Invalid input.")
		while True:
			try:
				nr_numbers = int(input(f"How many numbers would you like?\n"))
				break
			except ValueError:
				print("Invalid input.")

		letter_string = ''.join(random.choice(letters) for _ in range(nr_letters))
		symbol_string = ''.join(random.choice(symbols) for _ in range(nr_symbols))
		number_string = ''.join(random.choice(numbers) for _ in range(nr_numbers))

		password = f"{letter_string}{symbol_string}{number_string}"
		char_list = list(password)
		random.shuffle(char_list)
		shuffled_password = ''.join(char_list)

		print(f"Your password is:\n{shuffled_password}\n\n")
		while True:
			play_again = input("Do you want to generate another password? (y/n): ").lower()
			if play_again == "y":
				os.system('cls' if os.name == 'nt' else 'clear')
				break
			elif play_again == "n":
				print("Goodbye.")
				exit()
			else:
				print("Invalid input.")
		break