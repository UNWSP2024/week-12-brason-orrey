import tkinter
import tkinter.messagebox

class LongDistanceChargeCalculator:
    def __init__(self):
        # Create main window
        self.main_window = tkinter.Tk()
        self.main_window.title("Long Distance Call Charge Calculator")

        # Create a variable to store selected rate category
        self.selected_rate_category = tkinter.StringVar()

        # Create label and radio buttons for rate categories
        self.rate_label = tkinter.Label(self.main_window, text = "Select Rate Category:")
        self.rate_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = 'w')

        self.daytime_radio = tkinter.Radiobutton(self.main_window, text = "Daytime (6:00 A.M. to 5:59 P.M.) - $0.02 per min",
                                                 variable = self.selected_rate_category, value = "Daytime")
        self.daytime_radio.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = 'w')

        self.evening_radio = tkinter.Radiobutton(self.main_window, text = "Evening (6:00 P.M. to 11:59 P.M.) - $0.12 per min",
                                                 variable = self.selected_rate_category, value = "Evening")
        self.evening_radio.grid(row = 2, column = 0, padx = 10, pady = 5, sticky = 'w')

        self.off_peak_radio = tkinter.Radiobutton(self.main_window, text = "Off-Peak (Midnight to 5:59 A.M.) - $0.05 per min",
                                                  variable = self.selected_rate_category, value = "Off-Peak")
        self.off_peak_radio.grid(row = 3, column = 0, padx = 10, pady = 5, sticky = 'w')

        # Create label and entry widget for number of minutes
        self.minutes_label = tkinter.Label(self.main_window, text = "Enter Number of Minutes:")
        self.minutes_label.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = 'w')

        self.minutes_entry = tkinter.Entry(self.main_window)
        self.minutes_entry.grid(row = 5, column = 0, padx = 10, pady = 5)

        # Create Calculate Charge button
        self.calculate_button = tkinter.Button(self.main_window, text = "Calculate Charge", command = self.calculate_charge)
        self.calculate_button.grid(row = 6, column = 0, pady = 10)

        # Create Quit Button
        self.quit_button = tkinter.Button(self.main_window, text = "Quit", command = self.main_window.destroy)
        self.quit_button.grid(row = 7, column = 0, pady = 10)

        tkinter.mainloop()

    def calculate_charge(self):
        # Get the rate category and number of minutes entered
        rate_category = self.selected_rate_category.get()
        try:
            minutes = float(self.minutes_entry.get())
            if minutes < 0:
                tkinter.messagebox.showerror("Invalid Input", "Please enter a positive number for minutes.")
                return
        except ValueError:
            tkinter.messagebox.showerror("Invalid Input", "Please enter a valid number for minutes.")
            return

        # Determine the rate per minute based on the selected category
        if rate_category == "Daytime":
            rate = 0.02
        elif rate_category == "Evening":
            rate = 0.12
        elif rate_category == "Off-Peak":
            rate = 0.05
        else:
            tkinter.messagebox.showerror("Invalid Selection", "Please select a valid rate category.")
            return

        # Calculate the charge
        charge = rate * minutes

        # Show the charge in an info dialog box
        tkinter.messagebox.showinfo("Call Charge", f"The charge for your call is: ${charge:.2f}")

long_distance_calculator = LongDistanceChargeCalculator()