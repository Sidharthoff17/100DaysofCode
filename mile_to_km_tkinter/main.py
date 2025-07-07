from tkinter import *

def verify_input():
    miles = miles_entry.get()
    try:
        miles_float = float(miles)
        km = miles_float * 1.609
        global kilometers_result
        kilometers_result.config(text=f"{km:.2f}")  # update label with result
    except ValueError:
        pass



window = Tk()
window.title("Miles to Kilometres converter")
window.minsize(width=200, height=100)
window.config(padx=100, pady=200)

# miles Label
my_label = Label(text="Miles", font=("Arial", 12, "bold"))
my_label.grid(column=3, row=0)
my_label.config(padx=50, pady=50)

#km Label
km_label = Label(text="Km", font=("Arial", 12, "bold"))
km_label.grid(column=3, row=1)
km_label.config(padx=50, pady=50)


# Kilometers result Label (initially empty)
kilometers_result = Label(text="0", font=("Arial", 12, "bold"))
kilometers_result.grid(column=2, row=1)


#miles entry
miles_entry = Entry(width=10)
miles_entry.grid(column= 2, row=0)


new_button = Button(text="CALCULATE", command= verify_input)
new_button.grid(column=2, row=2)











window.mainloop()