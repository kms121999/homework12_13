

# Import tkinter modules
import tkinter
import tkinter.messagebox


# Set constants

# Output box text
OUT_TEMPLATE = "Your total charges = ${:.2f}"
OUT_NAME = "Total Charges"

# Input box text
SHOP_NAME = "Joe's Autotmotive"
PUSHBOX_DISPLAY = "Display Charges"
PUSHBOX_QUIT = "Quit"

# Service list - [Service, cost]
SERVICES_LIST = [
    ["Oil change", 30.00],
    ["Lube job", 20.00],
    ["Radiator flush", 40.00],
    ["Transmission flush", 100.00],
    ["Inspection", 35.00],
    ["Muffler replacement", 200.00],
    ["Tire rotation", 20.00],
    ]


class GUI:
    def __init__(self, options):
        # Create main window
        self.window = tkinter.Tk()

        # Create frames in window
        self.topFrame = tkinter.Frame(self.window)
        self.middleFrame = tkinter.Frame(self.window)
        self.bottomFrame = tkinter.Frame(self.window)

        # Create header label
        self.label = tkinter.Label(self.topFrame,
                                   text=SHOP_NAME,
                                   font = ("Arial", 24))
        # Pack the label
        self.label.pack()

        

        # List to contain all check buttons [ [selectedFlag, cost, buttonObject] ]
        self.checkButtons = []
        
        # Create a check buttons for each service
        for option in options: # option -> [name(str), cost(float)]
            
            # Add the variable and the cost to the option entry
            self.checkButtons.append([tkinter.IntVar(), option[1]])

            # Set the variable to 0
            self.checkButtons[-1][0].set(0)

            # Add the Checkbutton instance to the list
            self.checkButtons[-1].append( \
                tkinter.Checkbutton( \
                    self.middleFrame,
                    text = option[0] + " - ${:.2f}".format(option[1]),
                    variable = self.checkButtons[-1][0]
                    ) # End object init
                ) # End append call

            # Pack the checkButton object. Anchor west
            self.checkButtons[-1][2].pack(anchor='w')
            
        # Create display button
        self.buttonDisplay = tkinter.Button(self.bottomFrame,
                                            text = PUSHBOX_DISPLAY,
                                            command = self.displayResults,
                                            )

        # Create quit button
        self.buttonQuit = tkinter.Button(self.bottomFrame,
                                         text = PUSHBOX_QUIT,
                                         command = self.window.destroy
                                         )

        # Pack the buttons
        self.buttonDisplay.pack(side='left')
        self.buttonQuit.pack(side='left')

        # Pack the frames
        self.topFrame.pack(pady=(0, 25), padx='40')
        self.middleFrame.pack(pady='10')
        self.bottomFrame.pack(pady='20')

        # Start the tkinter's mainloop
        tkinter.mainloop()


    def displayResults(self):
        # Initialize accumulator
        total = 0

        # Check if which buttons have been pressed
        for button in self.checkButtons:
            if button[0].get() == 1:
                # If pressed, add cost to total
                total += button[1]

        # Create message box displaying the total
        tkinter.messagebox.showinfo(OUT_NAME, OUT_TEMPLATE.format(total))


# Create instance of the GUI
my_gui = GUI(SERVICES_LIST)


