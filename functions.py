import math, time


def get_list_of_coordinates_for_arcs(start_x, start_y, end_x, end_y, step=5):
    ''' Calculate coordinates of arc which is part of circle with radius r1
    and coordinates of its center (circle_center_x, circle_center_y) 
    '''
    
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
           y1 = 2*start_y - y1
        coordinates_list.append([x1,y1])
        #canvas.create_oval(x1,y1,x1+1,y1+1)
        x += step
    if backwards:
        # rewrite coordinates_list backwards
        coordinates_list = coordinates_list[::-1]
    return coordinates_list
   
   
def move_circle_with_text_by_arc(root, canvas, settings, position1, position2, circle_array, text_array):
    """move the circle by the arc from one position to second position
       position is coordinates of upper left corner of the rectangle
       where the circle is located
    """

    # coordinates of position1 are coordinates of upper 
    # left of the circle on position1
    pos1 = [canvas.coords(circle_array[position1].circle_id)[0], canvas.coords(circle_array[position1].circle_id)[1]]
    # same for position2
    pos2 = [canvas.coords(circle_array[position2].circle_id)[0], canvas.coords(circle_array[position2].circle_id)[1]]
    # arc number is number of circle of position1
    list_arcs_coordinates_forward = get_list_of_coordinates_for_arcs(pos1[0], pos1[1], pos2[0], pos2[1])
    list_arcs_coordinates_backward = get_list_of_coordinates_for_arcs(pos2[0], pos2[1],pos1[0], pos1[1])
    
    for i in list_arcs_coordinates_forward:
        circle_array[position1].move(i[0], i[1])
        text_array[position1].move(i[0]+settings.CIRCLE_WIDTH//2, i[1]+settings.CIRCLE_HEIGHT//2)
        root.update()
        time.sleep(0.1)
    for j in list_arcs_coordinates_backward:
        circle_array[position2].move(j[0], j[1])
        text_array[position2].move(j[0]+settings.CIRCLE_WIDTH//2, j[1]+settings.CIRCLE_HEIGHT//2)
        root.update()
        time.sleep(0.1)
    
    # change objects positions in the list
    temp_circle = circle_array[position1]
    circle_array[position1] = circle_array[position2]
    circle_array[position2] = temp_circle
    
    temp_text = text_array[position1]
    text_array[position1] = text_array[position2]
    text_array[position2] = temp_text
    
def move_circle_with_text_up_down(root, settings, circleIndex, shiftY, circle_array, text_array):
    
    # get currecnt coordinates of upper left corner
    circleX = circle_array[circleIndex].x
    circleY = circle_array[circleIndex].y
        
    circle_array[circleIndex].move(circleX, circleY+shiftY)
    text_array[circleIndex].move(circleX+settings.CIRCLE_WIDTH//2, circleY+shiftY+settings.CIRCLE_HEIGHT//2)
    root.update()
    
def move_circle_to_init(root, settings, circleIndex, circle_array, text_array):
    
    circle_array[circleIndex].move(settings.getInitXCoord(circleIndex), settings.INIT_CIRCLE_Y)
    text_array[circleIndex].move(settings.getInitXCoord(circleIndex)+settings.CIRCLE_WIDTH//2, settings.INIT_CIRCLE_Y+settings.CIRCLE_HEIGHT//2)
    root.update()
