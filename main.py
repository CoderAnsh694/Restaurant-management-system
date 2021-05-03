from tkinter import *
from tkinter import messagebox

def total():
	try:
		total_list.delete(0)
		total = sum(total_prices)
		total_list.insert(END, total)
	except:
		total = sum(total_prices)
		total_list.insert(END, total)


def select():
	item = clicked.get()
	index = items.index(item)
	price = prices[index]
	total_prices.append(int(price))
	item_selected.append(item)
	item_list.insert(END, item)
	price_list.insert(END, price)


def get_items():
	with open('database/menu.txt') as file:
		for line in file:
			item, price = line.split("::")
			items.append(item)
			prices.append(price)


def add_item():

	def add():
		file = open('database/menu.txt', 'a')
		item = name_entry.get()
		price = price_entry.get()
		file.write(f'{item}::{price}\n')
		messagebox.showinfo('', 'Item added successfully')
		items.append(item)
		prices.append(price)
		drop.config(*items)

	root2 = Tk()
	root2.geometry('300x400')
	root2.resizable(False, False)

	name_label = Label(root2, text = 'Item Name: ')
	name_label.pack()
	name_label.place(x = 20, y = 40)

	name_entry = Entry(root2, width = 30)
	name_entry.pack()
	name_entry.place(x = 20, y = 60)

	price_label = Label(root2, text = 'Price: ')
	price_label.pack()
	price_label.place(x = 20, y = 110)

	price_entry = Entry(root2, width = 30)
	price_entry.pack()
	price_entry.place(x = 20, y = 130)

	add_item = Button(root2, text = 'Add Item', command = add, width = 30)
	add_item.pack()
	add_item.place(x = 20, y = 160)



	root2.mainloop()

root = Tk()
root.geometry('350x490')
root.resizable(False, False)
root.title('Restaurant Managment System')

items = ['<Select item>']
prices = ['<Unknown Price>']
total_prices = []
get_items()

clicked = StringVar()
clicked.set(items[0])
drop = OptionMenu(root, clicked, *items)
drop.pack()
drop.place(x = 20, y = 30)
drop.config(width = 43)

select_button = Button(root, text = 'Select Item', width = 15, command = select)
select_button.pack()
select_button.place(x = 20, y = 70)

add_button = Button(root, text = 'Add Item', command = add_item, width = 15)
add_button.pack()
add_button.place(x = 207, y = 70)

item_list = Listbox(root, width = 35)
item_list.pack()
item_list.place(x = 20, y = 100)

price_list = Listbox(root, width = 13)
price_list.pack()
price_list.place(x = 241, y = 100)

total_label = Label(root, text = 'Total: ')
total_label.pack()
total_label.place(x = 200, y = 300)

total_list = Listbox(root, width = 13, height = 1)
total_list.pack()
total_list.place(x = 247, y = 300)

total_button = Button(root, text = 'Calculate Total', command = total)
total_button.pack()
total_button.place(x = 20, y = 300)


root.mainloop()