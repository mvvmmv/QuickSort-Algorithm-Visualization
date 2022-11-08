import math
import time
import tkinter.messagebox
from elementCircle import ElementCircle


def get_list_of_coordinates_for_arcs(start_x, start_y, end_x, end_y, step=5):
    ''' Calculate coordinates of arc which is part of circle with radius r1
    and coordinates of its center (circle_center_x, circle_center_y)
    '''

    # If arc goes from left to right - the order of coordinates are forward
    # and the arc is placed above the circles.
    # Otherwise - the list is being re-written backwards
    # and Y coordinates is being changed so that the arc is mirrored to bottom.
    backwards = False
    if start_x > end_x:
        # replace start_x with end_x
        temp = start_x
        start_x = end_x
        end_x = temp
        backwards = True

    coordinates_list = []
    r = (end_x - start_x)//2
    r1 = math.sqrt(2*(r**2))
    circle_center_x = (end_x - start_x)//2 + start_x
    circle_center_y = math.sqrt(r1**2-r**2) + start_y
    x = start_x
    while x <= end_x:
        x1 = x
        y1 = int(-math.sqrt(r1**2-(x-circle_center_x)**2)+circle_center_y)
        if backwards:
            # Change Ys to be mirrored
            y1 = 2*start_y - y1
        coordinates_list.append([x1, y1])
        # canvas.create_oval(x1,y1,x1+1,y1+1)
        x += step
    if backwards:
        # rewrite coordinates_list backwards
        coordinates_list = coordinates_list[::-1]
    return coordinates_list


def replace_circles_with_text_by_arc(root, canvas, settings, position1,
                                     position2, circle_array, text_array):
    """Replacing circles in position 1 and position 2 with each other
       the forward and backward arcs.
       Position is the coordinates of upper left corner of the rectangle
       where the circle is located
    """

    # coordinates of position1 are coordinates of upper
    # left of the circle on position1
    pos1 = [canvas.coords(circle_array[position1].circle_id)[0],
            canvas.coords(circle_array[position1].circle_id)[1]]
    # same for position2
    pos2 = [canvas.coords(circle_array[position2].circle_id)[0],
            canvas.coords(circle_array[position2].circle_id)[1]]

    # arc number is number of circle of position1
    list_arcs_coordinates_forward = \
        get_list_of_coordinates_for_arcs(pos1[0], pos1[1], pos2[0], pos2[1])
    list_arcs_coordinates_backward = \
        get_list_of_coordinates_for_arcs(pos2[0], pos2[1], pos1[0], pos1[1])

    # Moving circles and texts along by the list of arcs coordinates
    for i in list_arcs_coordinates_forward:
        circle_array[position1].move(i[0], i[1])
        text_array[position1].move(i[0]+settings.CIRCLE_WIDTH//2,
                                   i[1]+settings.CIRCLE_HEIGHT//2)
        root.update()
        time.sleep(0.1)

    for j in list_arcs_coordinates_backward:
        circle_array[position2].move(j[0], j[1])
        text_array[position2].move(j[0]+settings.CIRCLE_WIDTH//2,
                                   j[1]+settings.CIRCLE_HEIGHT//2)
        root.update()
        time.sleep(0.1)

    # change objects positions in the list
    temp_circle = circle_array[position1]
    circle_array[position1] = circle_array[position2]
    circle_array[position2] = temp_circle

    temp_text = text_array[position1]
    text_array[position1] = text_array[position2]
    text_array[position2] = temp_text


def move_circle_with_text_up_down(root, settings, circleIndex,
                                  shiftY, circle_array, text_array):
    '''Moves circle from <circleIndex> position
    with its text up or down, depending on <shiftY> parameter'''

    # get current coordinates of upper left corner
    circleX = circle_array[circleIndex].x
    circleY = circle_array[circleIndex].y

    circle_array[circleIndex].move(circleX, circleY+shiftY)
    text_array[circleIndex].move(circleX+settings.CIRCLE_WIDTH//2,
                                 circleY+shiftY+settings.CIRCLE_HEIGHT//2)
    root.update()


def move_circle_to_init(root, settings, circleIndex, circle_array, text_array):
    '''Resets position of the circle with its text back to initial position'''

    circle_array[circleIndex].move(settings.getInitXCoord(circleIndex),
                                   settings.INIT_CIRCLE_Y)
    text_array[circleIndex].move(
        settings.getInitXCoord(circleIndex)+settings.CIRCLE_WIDTH//2,
        settings.INIT_CIRCLE_Y+settings.CIRCLE_HEIGHT//2)
    root.update()


def length_less_than_10(uInput):
    '''Validate length of user's input'''

    if len(uInput) > 10:
        tkinter.messagebox.showinfo(
            'Error', 'No more than 10 elements allowed')
        return False
    return True


def move_comparing_objects_up_down(root, settings, circle_instances, text_instances, circle1=None, circle2=None, shift=None):
    '''resets all circles locations to init and shift only circle1 and circle2
    If no input parameters - reset to initial position'''

    for index in range(0, len(circle_instances)):
        move_circle_to_init(
            root, settings, index, circle_instances, text_instances)

    if shift:
        move_circle_with_text_up_down(
            root, settings, circle1, shift, circle_instances, text_instances)
        move_circle_with_text_up_down(
            root, settings, circle2, shift, circle_instances, text_instances)


def circle_change_color(root, settings, circle=None, color=None):
    '''changes color of circle defined by index to <color>,
    rest of colors changes back to inintial
    If no input parameters - reset colors for all'''
    
    circle_instances = ElementCircle.instances

    for index in range(0, len(circle_instances)):
        circle_instances[index].set_color(settings.INIT_COLOR)

    for index in ElementCircle.pivots:
        circle_instances[index].set_color(settings.PIVOT_COLOR)

    if color:
        circle_instances[circle].set_color(color)

    root.update()
