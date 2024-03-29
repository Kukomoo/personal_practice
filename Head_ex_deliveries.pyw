#GUI for data entry and appending to file deliveries.txt in a specific format

from tkinter import *
def save_data():
	fileD = open("deliveries.txt", "a") #opens the file and appends
	fileD.write("Depot:\n")
	fileD.write("%s\n" % depot.get())
	fileD.write("Description:\n")
	fileD.write("%s\n" % description.get())
	fileD.write("Address:\n")
	fileD.write("%s\n" % address.get(1.0, END))
	depot.delete(0, END)
	description.delete(0, END)
	address.delete("1.0", END) #to erase allowing for new entry

app = Tk()
app.title('Head-Ex Deliveries')
Label(app, text = "Depot:").pack()
depot = Entry(app)
depot.pack()
Label(app, text = "Description:").pack()
description = Entry(app)
description.pack()
Label(app, text = "Address:").pack()
address = Text(app)
address.pack()
Button(app, text = "Save", command = save_data).pack()
app.mainloop()
