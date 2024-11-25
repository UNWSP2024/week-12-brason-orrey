import tkinter
import tkinter.messagebox

class MPG_Calculator:
    def __init__(self):
        # Create window
        self.main_window = tkinter.Tk()
        self.main_window.title("MPG Calculator")

        # Create labels to left of entry
        self.miles_label = tkinter.Label(self.main_window, text="Miles:")
        self.miles_label.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "e")

        self.gallons_label = tkinter.Label(self.main_window, text = "Gallons:")
        self.gallons_label.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "e")

        # Entry for miles
        self.user_miles_input = tkinter.Entry(self.main_window)
        self.user_miles_input.grid(row = 0, column = 1, padx = 5, pady = 5)

        # Entry for gallons
        self.user_gallons_input = tkinter.Entry(self.main_window)
        self.user_gallons_input.grid(row = 1, column = 1, padx = 5, pady = 5)

        # Create Calculate Button
        self.calculate_button = tkinter.Button(self.main_window, text = "Calculate MPG", command = self.retrieve_entries)
        self.calculate_button.grid(row = 2, column = 0, columnspan = 2, padx = 5, pady = 5)

        self.quit_button = tkinter.Button(self.main_window, text = "Quit", command = self.main_window.destroy)
        self.quit_button.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 5)

        tkinter.mainloop()

    def retrieve_entries(self):
        # Retrieve and calculate MPG, handling possible errors
        try:
            user_miles = float(self.user_miles_input.get())
            user_gallons = float(self.user_gallons_input.get())
            mpg = user_miles / user_gallons

            tkinter.messagebox.showinfo("MPG Result", f"Miles: {user_miles}\nGallons: {user_gallons}\nMPG: {mpg:.2f}")
        except ValueError:
            tkinter.messagebox.showerror("Input Error", "Please enter valid numbers for miles and gallons.")
        except ZeroDivisionError:
            tkinter.messagebox.showerror("Calculation Error", "Gallons cannot be zero for MPG calculation.")

MPG_Calculator = MPG_Calculator()
