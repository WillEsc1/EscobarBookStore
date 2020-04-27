"""
William Escobar
Version 1.0
"""
from tkinter import *
import backend

def Display_Selected_Row(event):
    # Setting the "Selected_Tuple" var as a global var allows us to call it in the Delete_Command function below
    try:
        global Selected_Tuple
        index = displayBox.curselection()[0]
        Selected_Tuple = displayBox.get(index)

        # This will display information of the selected row in the text fields
        e1.delete(0,END)
        e1.insert(END, Selected_Tuple[1])

        e2.delete(0,END)
        e2.insert(END, Selected_Tuple[2])
        
        e3.delete(0,END)
        e3.insert(END, Selected_Tuple[3])
        
        e4.delete(0,END)
        e4.insert(END, Selected_Tuple[4])
    except IndexError:
        pass
    
def View_Command():
    displayBox.delete(0,END)
    for row in backend.View_All():
        displayBox.insert(END, row)

def Search_Command():
    displayBox.delete(0,END)
    for row in backend.Search_DB(titleText.get(), authorText.get(), yearText.get(), isbnText.get()):
        displayBox.insert(END, row)

def Entry_Command():
    backend.Add_Entry(titleText.get(), authorText.get(), yearText.get(), isbnText.get())

    # This will display the newly added row 
    displayBox.delete(0,END)
    displayBox.insert(END, (titleText.get(), authorText.get(), yearText.get(), isbnText.get()))

def Update_Command():
    backend.Update_Entry(Selected_Tuple[0], titleText.get(), authorText.get(), yearText.get(), isbnText.get())

def Delete_Command():
    backend.Delete_Entry(Selected_Tuple[0])

window = Tk()
window.wm_title("Escobar's Book Store")

# These are labels for the text boxes
l1 = Label(window, text = "Title")
l1.grid(row = 0, column = 0)

l2 = Label(window, text = "Author")
l2.grid(row = 0, column = 2)

l3 = Label(window, text = "Year")
l3.grid(row = 1, column = 0)

l4 = Label(window, text = "ISBN")
l4.grid(row = 1, column = 2)

# These are the actual text boxes that will display the data!
titleText = StringVar()
e1=Entry(window, textvariable=titleText)
e1.grid(row = 0, column = 1)

authorText = StringVar()
e2=Entry(window, textvariable=authorText)
e2.grid(row = 0, column = 3)

yearText = StringVar()
e3=Entry(window, textvariable=yearText)
e3.grid(row = 1, column = 1)

isbnText = StringVar()
e4=Entry(window, textvariable=isbnText)
e4.grid(row = 1, column = 3)

# This creates a display box where our database entries will be displayed
displayBox = Listbox(window, height = 10, width = 35)
displayBox.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

# This creates a scroll bar to allow the user to navigate the y axis of our display box
sb1=Scrollbar(window)

# To center the scroll bar we can set the rowspan = 6
sb1.grid(row = 2, column = 2, rowspan = 6)

# Command to move the view of the display up and down (y axis)
displayBox.configure(yscrollcommand = sb1.set)
sb1.configure(command = displayBox.yview)

displayBox.bind('<<ListboxSelect>>', Display_Selected_Row)

# This creates the button in our window. The width of the button is set to 12
# Do not use paranthesis as python will run the function
bViewAll = Button(window, text = "View All", width = 12, command = View_Command)
bViewAll.grid(row = 2, column = 3)

bSearch = Button(window, text = "Search Entry", width = 12, command = Search_Command)
bSearch.grid(row = 3, column = 3)

bAddEntry = Button(window, text = "Add Entry", width = 12, command = Entry_Command)
bAddEntry.grid(row = 4, column = 3)

bUpdate = Button(window, text = "Update Entry", width = 12, command = Update_Command)
bUpdate.grid(row = 5, column = 3)

bDelete = Button(window, text = "Delete Entry", width = 12, command = Delete_Command)
bDelete.grid(row = 6, column = 3)

bExit = Button(window, text = "Exit", width = 12, command = window.destroy)
bExit.grid(row = 7, column = 3)

window.mainloop()