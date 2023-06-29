import tkinter as tk

# Declaration of global variable
temp_Val = "Celsius"

# getting drop down value
def store_temp(set_temp):
	global temp_Val
	temp_Val = set_temp

# Conversion of temperature
def call_convert(rlabel1, inputn):
	temp = inputn.get()
	
	if temp_Val == 'Celsius':
		
		# Conversion of celsius temperature to fahrenheit
		f = float((float(temp) * 9 / 5) + 32)
		rlabel1.config(text ="%.1f Fahrenheit" % f)
		
		
	if temp_Val == 'Fahrenheit':
		
		# Conversion of fahrenheit temperature
		# to celsius
		c = float((float(temp) - 32) * 5 / 9)
		rlabel1.config(text ="%.1f Celsius" % c)
		
	return


# creating Tk window
root = tk.Tk()

# setting geometry of tk window
root.geometry('540x150+600+200')

# Using title() to display a message in the
# dialogue box of the message in the title bar
root.title('Temperature Converter')
root.minsize(540, 150)
root.maxsize(540, 150)
# Lay out widgets
root.grid_columnconfigure(1, weight = 1)
root.grid_rowconfigure(1, weight = 1)
root.config(bg="black")
inputNumber = tk.StringVar()
var = tk.StringVar()

# label and entry field
input_label = tk.Label(root, text ="Enter temperature:", bg="gray", font=("times of India",18,'bold'), fg="black")
input_entry = tk.Entry(root, textvariable = inputNumber, font=("times of India",15,'bold'),bd=3 )
input_label.grid(row = 1)
input_entry.grid(row = 1, column = 1)
result_label = tk.Label(root, bg="gray", font=("times of India",18,'bold'), fg="black")
result_label.grid(row = 3, columnspan = 4)

# drop down setup
dropDownList = ["Celsius", "Fahrenheit"]
drop_down = tk.OptionMenu(root, var, *dropDownList,
						command = store_temp)
var.set(dropDownList[0])
drop_down.grid(row = 1, column = 2)

# button widget

result_button = tk.Button(root, text ="Convert",
						command =lambda: call_convert(result_label,inputNumber), bg="gray", fg="black", bd=3
                 ,highlightbackground="dimgray", width=8, height=1,activeforeground="steelblue"
                 ,activebackground="white", font=("Times of roman",15,"bold"))
result_button.grid(row = 2, columnspan = 2)

# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
root.mainloop()
