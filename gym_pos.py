from transactions import *
items = ["WORKOUT", "WEIGHTS", "BIKES"]
prices = [35.0, 10.0, 8.0]
running = True
while running:
	option = 1
	for choice in items:
		print(str(option) + ". " + choice)
		option += 1
	print(str(option) + ". Quit")
	choice = int(input("Choose an option: "))
	if choice == option:
		running = Falsw
	else:
		credit_card = input("Credit card number: ")
		save_transactions(prices[choice - 1], credit_card, items[choice - 1]
