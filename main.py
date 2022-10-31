from tkinter import Canvas, Label, Tk, Text, messagebox, IntVar
from tkinter.ttk import Style, Button

import math
from time import sleep
import re

from elementCircle import ElementCircle
from textCircle import TextCircle
from settings import Settings
import functions

root = Tk()
root.title("QuickSort Algorithm")

settings = Settings()

def validation_of_user_input(uInput):
    ''' Validate user's input'''
        
    # Validate the input (digits, no more than 10 numbers)
    for element in uInput:
        if not element.isdigit():
            messagebox.showinfo(
                'Error', 'Each element of the array should be a number')
            return False
        
    if len(uInput) > 10:
        messagebox.showinfo(
            'Error', 'No more than 10 elements allowed')
        return False
    
    return True
        
def initialize():
            
    # Get user's input
    ui = usersInput.get("1.0", 'end-1c')
    
    # Getting rid of commas and spaces
    ui = re.split(' |,', ui)
    while '' in ui:
        ui.remove('')
        
    # If the input is valid
    if validation_of_user_input(ui):
        A = ui
        array_length = len(A)
        
        # new shift from the left of the window
        settings.SHIFT_X_NEW = settings.SHIFT_X + (10 - len(A))*settings.DISTANCE_BETWEEN_CIRCLES//2
        
        # create circle and text objects for each element of the array
        for index in range(0,array_length):
            ElementCircle(canvas, 
                          settings,
                          settings.getInitXCoord(index), 
                          settings.INIT_CIRCLE_Y,
                          settings.INIT_COLOR
                        )
            TextCircle(canvas, 
                       settings.getInitXCoord(index)+settings.CIRCLE_WIDTH//2,
                       settings.INIT_TEXT_Y, 
                       str(A[index]),
                       )
        quicksort(A, 0, len(A)-1)
        labelInfo.configure(text='QuickSort completed!')
    # else - reset everything
    else:
        messagebox.showinfo(
                'Info', 'Enter the array')
        reset()
        
def quicksort(array, startIndex, endIndex):
    
    #labelInfo.configure(text='Sorting array from %d to %d index' % (startIndex, endIndex))
    buttonNext.wait_variable(buttonVar)
    
    if startIndex >= endIndex:   
        
        labelInfo.configure(text="Can't sort from %d to %d" % (startIndex, endIndex))
        buttonNext.wait_variable(buttonVar)
        return
    
    else:
        pivotIndex = partition(array, startIndex, endIndex-1) 
        labelInfo.configure(text='Pivot element found - %d' % (pivotIndex))
        
        buttonNext.wait_variable(buttonVar)
        
        labelInfo.configure(text='Sort left part of the array: from %d to %d index' % (startIndex, pivotIndex-1))
        quicksort(array, startIndex, pivotIndex-1)
        buttonNext.wait_variable(buttonVar)
        
        labelInfo.configure(text='Sort right part of the array from %d to %d index' % (pivotIndex+1, endIndex))
        quicksort(array, pivotIndex+1, endIndex)
        buttonNext.wait_variable(buttonVar)
    
def partition(array, startIndex, endIndex):
    
    labelInfo.configure(text='Searching for Pivot element in array from %d to %d indexes' % (startIndex, endIndex+1))
    
    circle_instances = ElementCircle.instances
    text_instances = TextCircle.instances
    
    buttonNext.wait_variable(buttonVar)
    pivotIndex = startIndex
    
    # Change pivot color
    circle_change_color(pivotIndex, 'YELLOW')
    labelInfo.configure(text="Let's put for Pivot %d element" % pivotIndex)
    
    for i in range(startIndex, endIndex+1):
        buttonNext.wait_variable(buttonVar)
        
        labelInfo.configure(text="Let's compare %d and %d elements" % (i, endIndex+1))
        
        # Shift comparing elements up
        move_comparing_objects_up_down(i, endIndex+1, -settings.SHIFT)
        
        buttonNext.wait_variable(buttonVar)
        
        if array[i] <= array[endIndex+1]:
            
            # replacing element and pivot
            u = array[i]
            array[i] = array[pivotIndex]
            array[pivotIndex] = u
                    
            labelInfo.configure(text="Element %d less(or equal) than %d element. Replacing %d element with Pivot" % (i, endIndex+1, i))
            
            # Reset all elements positions before replacement
            move_comparing_objects_up_down()
            
            # Reset pivot color before replacement
            #circle_change_color()
    
            # Replacing circles
            functions.move_circle_with_text_by_arc(root, canvas, settings, pivotIndex, i, circle_instances, text_instances)
            
                        
            buttonNext.wait_variable(buttonVar)
            
            # taking next element for pivot
            pivotIndex += 1 
            
            circle_change_color(pivotIndex, 'YELLOW')
            labelInfo.configure(text="Let's put for Pivot %d element" % pivotIndex)
            
        # Reset all elements positions
        move_comparing_objects_up_down()
               
    buttonNext.wait_variable(buttonVar)  
    
    # Change pivot color
    circle_change_color(pivotIndex, 'YELLOW')   
    
    labelInfo.configure(text="End of search. Replacing Pivot %d with last element %d" % (pivotIndex, endIndex+1))
    
    # replacing pivot and end elements
    u = array[pivotIndex]
    array[pivotIndex] = array[endIndex+1]
    array[endIndex+1] = u
    buttonNext.wait_variable(buttonVar) 
    # Reset pivot color
    circle_change_color()  

    # Reset comparing elements positions
    move_comparing_objects_up_down() 
    
    functions.move_circle_with_text_by_arc(root, canvas, settings, pivotIndex, endIndex+1, circle_instances, text_instances)
    
    ElementCircle.pivots.append(pivotIndex)
    
    # Reset colors
    circle_change_color() 
    
    return pivotIndex

def move_comparing_objects_up_down(circle1=None, circle2=None, shift=None):
    '''resets all circles locations to init and shift only circle1 and circle2
    If no input parameters - reset to initial position'''
    
    circle_instances = ElementCircle.instances
    text_instances = TextCircle.instances
    
    for index in range(0,len(circle_instances)):
        functions.move_circle_to_init(root, settings, index, circle_instances,text_instances)
    
    if shift:
        functions.move_circle_with_text_up_down(root, settings, circle1, shift, circle_instances,text_instances)
        functions.move_circle_with_text_up_down(root, settings, circle2, shift, circle_instances,text_instances)
           
def circle_change_color(circle=None, color=None):
    '''changes color of circle defined by index to <color>,
    rest of colors changes back to inintial
    If no input parameters - reset colors for all'''
    
    circle_instances = ElementCircle.instances
    
    for index in range(0,len(circle_instances)):
        circle_instances[index].set_color(settings.INIT_COLOR)
    
    for index in ElementCircle.pivots:
        circle_instances[index].set_color(settings.PIVOT_COLOR)
    
    if color:    
        circle_instances[circle].set_color(color)
        
    root.update()

def reset():
    
    # Remove users's input
    usersInput.delete("1.0", "end")
    
    circle_instances = ElementCircle.instances
    text_instances = TextCircle.instances
    
    # Delete circle and text objects
    while circle_instances:
        del circle_instances[0]
        del text_instances[0]
        
    # Clear the label
    labelInfo.configure(text='') 
    
    # clear all lists
    ElementCircle.instances = []
    ElementCircle.pivots = []
    TextCircle.instances = []
    
    # Delete canvas   
    canvas.delete('all')
    
# Label for user instruction to put the array
usersInputLabel = Label(root, text='Enter the array:')
usersInputLabel.grid(row=0,column=1, pady=10)

# Field for user to put the array
usersInput = Text(root, height=1, width=25)
usersInput.grid(row=1,column=1, pady=5)

# Button to initialize the array
buttonInit = Button(root, text="Go", command=initialize)
buttonInit.grid(row=2,column=1, pady=5)

canvas = Canvas(root, width=settings.WIDTH, height=settings.HEIGHT)
canvas.grid(row=3, column=1)

# defining tkinter variables
buttonVar = IntVar()

# Label to show step description
labelInfo = Label(root, text=None)
labelInfo.grid(row=4, column=1, pady=5)

# Button to go to the next step
buttonNext = Button(root, text="Next step", command=lambda: buttonVar.set(1))
buttonNext.grid(row=5,column=1, pady=5)

# Button to reset all
buttonReset = Button(root, text="Reset", command=reset)
buttonReset.grid(row=6,column=1, pady=5)

# Button to quit
buttonQuit = Button(root, text="Quit", command=root.destroy)
buttonQuit.grid(row=7,column=1, pady=5)

root.mainloop()