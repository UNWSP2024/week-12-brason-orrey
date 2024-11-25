import tkinter
import tkinter.messagebox

# Oil Change - $30.00
# Lube Job - $20.00
# Radiator Flush - $40.00
# Transmission Fluid - $100.00
# Inspection - $35.00
# Muffler Replacement - $200.00
# Tire Rotation - $20.00

class Joes_automotive:
    def __init__(self):
        # Create main window
        self.main_window = tkinter.Tk()
        self.main_window.title("Joe's Automotive Cost Calculator")

        # Create variables for each checkbox
        self.oil_change_variable = tkinter.IntVar()
        self.lube_job_variable = tkinter.IntVar()
        self.radiator_flush_variable = tkinter.IntVar()
        self.transmission_fluid_variable = tkinter.IntVar()
        self.inspection_variable = tkinter.IntVar()
        self.muffler_replacement_variable = tkinter.IntVar()
        self.tire_rotation_variable = tkinter.IntVar()

        # Create and place checkbuttons with even spacing
        self.oil_change = tkinter.Checkbutton(
            self.main_window, text = "Oil Change ($30)",
            variable = self.oil_change_variable, onvalue = 30, offvalue = 0)
        self.oil_change.grid(row = 0, column = 0, sticky = 'w', padx = 10, pady = 5)


        self.lube_job = tkinter.Checkbutton(
            self.main_window, text = "Lube Job ($20)",
            variable = self.lube_job_variable, onvalue = 20, offvalue = 0)
        self.lube_job.grid(row = 1, column = 0, sticky = 'w', padx = 10, pady = 5)


        self.radiator_flush = tkinter.Checkbutton(
            self.main_window, text = "Radiator Flush ($40)",
            variable = self.radiator_flush_variable, onvalue = 40, offvalue = 0)
        self.radiator_flush.grid(row = 2, column = 0, sticky = 'w', padx = 10, pady = 5)


        self.transmission_fluid = tkinter.Checkbutton(
            self.main_window, text = "Transmission Fluid ($100)",
            variable = self.transmission_fluid_variable, onvalue = 100, offvalue = 0)
        self.transmission_fluid.grid(row = 3, column = 0, sticky = 'w', padx = 10, pady = 5)


        self.inspection = tkinter.Checkbutton(
            self.main_window, text = "Inspection ($35)",
            variable = self.inspection_variable, onvalue = 35, offvalue = 0)
        self.inspection.grid(row = 4, column = 0, sticky = 'w', padx = 10, pady = 5)


        self.muffler_replacement = tkinter.Checkbutton(
            self.main_window, text = "Muffler Replacement ($200)",
            variable = self.muffler_replacement_variable, onvalue = 200, offvalue = 0)
        self.muffler_replacement.grid(row = 5, column = 0, sticky = 'w', padx = 10, pady = 5)


        self.tire_rotation = tkinter.Checkbutton(
            self.main_window, text = "Tire Rotation ($20)",
            variable = self.tire_rotation_variable, onvalue = 20, offvalue = 0)
        self.tire_rotation.grid(row = 6, column = 0, sticky = 'w', padx = 10, pady = 5)

        # Create calculate button
        self.calculate_button = tkinter.Button(
            self.main_window, text = "Calculate Total", command = self.calculate_total)
        self.calculate_button.grid(row = 7, column =  0 , pady = 10)

        # Create quit button
        self.quit_button = tkinter.Button(
            self.main_window, text = "Quit", command = self.main_window.destroy)
        self.quit_button.grid(row = 8, column = 0, pady = 10)

        tkinter.mainloop()


    def calculate_total(self):
        # Calculate total
        total = (self.oil_change_variable.get() +
                 self.lube_job_variable.get() +
                 self.radiator_flush_variable.get() +
                 self.transmission_fluid_variable.get() +
                 self.inspection_variable.get() +
                 self.muffler_replacement_variable.get() +
                 self.tire_rotation_variable.get())
        # Messagebox with total
        tkinter.messagebox.showinfo("Joe's Automotive", f"Your Total: ${total}")

joes_automotive = Joes_automotive()
