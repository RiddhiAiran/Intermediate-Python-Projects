from tkinter import *

def convert():
    """
    Convert miles to kilometers and display the result on the GUI.
    Handles invalid input with an error message.
    """
    try:
        miles = float(user_input.get())
        kms = miles * 1.60934
        output_text.config(text=f"{round(kms,2)} Km")
    except ValueError:
        output_text.config(text="Invalid input!")

# Create the main window
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=350, height=150)
window.config(padx=30, pady=30)

# Input field for miles
user_input = Entry(width=10, font=('Arial', 15))
user_input.grid(column=1, row=0)

# Label for "Miles"
miles_label = Label(text="Miles", font=('Arial', 15))
miles_label.grid(column=2, row=0)

# Label for "is equals to"
equals_to_label = Label(text="is equal to", font=('Arial', 15))
equals_to_label.grid(column=0, row=1)

# Output label for displaying the result
output_text = Label(text="0.00 Km", font=('Arial', 15), fg="blue")
output_text.grid(column=1, row=1)

# Label for "Km"
km_label = Label(text="Km", font=('Arial', 15))
km_label.grid(column=2, row=1)

# Button to trigger conversion
convert_button = Button(text="Convert", command=convert, font=('Arial', 12))
convert_button.grid(column=1, row=2, pady=10)

# Run the Tkinter event loop
window.mainloop()
