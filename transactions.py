def save_transactions(price, credit_card, description):
file = open("transactions.txt", "a")
file.write("%07%16s%16s\n"%(price * 100, credit_card, description))
file.close()
