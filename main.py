from tkinter import Canvas, Tk, messagebox
import helpers
import utilities
from utilities import get_left, get_right
import helpers
import time
import keycodes

gui = Tk()
gui.title('My Terrarium')

# initialize canvas:
window_width = gui.winfo_screenwidth()
window_height = gui.winfo_screenheight()
background_color = 'white'
canvas = Canvas(gui, width=window_width, height=window_height, background=background_color)
canvas.pack()

####### Rules #######
def show_help_message():
   messagebox.showinfo('Game Instructions', 'Goal: maneuver the Totoro to the other side of the road\nUse arrow keys to move\nDo not hit the trucks\nDo not go off the screen\nAfter 5 succesful crosses, you win the game!')
show_help_message()
####### making the road (from downloaded internet picture) ########
utilities.make_image(canvas, 'Toon_Road_Texture2.png', position=(0, 0), scale=0.48)
####### rendering the commandable Totoro ########
helpers.make_creature(canvas, (window_width/2, window_height-135), size=25, tag='creature')
####### things to track later #######
counter = 0
quitting = False
collision = False
######## moving commandable Totoro in general ########
KEY_PRESS = '<Key>'
totoro_position_y = window_height-135
totoro_position_x = window_width/2
def move_creature(event):
    x_distance = 105
    y_distance = 120
    global totoro_position_y
    global totoro_position_x
    ## moving up, down, left, and right ##
    if event.keycode == keycodes.get_up_keycode():
        utilities.update_position_by_tag(canvas, tag='creature', x=0, y=-y_distance)
        totoro_position_y -= y_distance
    elif event.keycode == keycodes.get_down_keycode():
        utilities.update_position_by_tag(canvas, tag='creature', x=0, y=y_distance)
        totoro_position_y += y_distance
    elif event.keycode == keycodes.get_left_keycode():
        utilities.update_position_by_tag(canvas, tag='creature', x=-x_distance, y=0)
        totoro_position_x -= x_distance
    elif event.keycode == keycodes.get_right_keycode():
        utilities.update_position_by_tag(canvas, tag='creature', x=x_distance, y=0)
        totoro_position_x += x_distance
    ## if totoro goes out of bounds, GAME OVER ##
    if totoro_position_x > 1270 or totoro_position_x < 10 or totoro_position_y > window_height-135:
        global collision
        collision = True
    ## upon reaching the top, reset to begining position
    if totoro_position_y <= 0:
        utilities.delete_by_tag(canvas, 'creature')
        helpers.make_creature(canvas, (window_width/2, window_height-135), size=25, tag='creature')
        totoro_position_y = window_height-135
        totoro_position_x = window_width/2
        add_counter()

####### adding totoros (called aboove, after every crossing) #######
def add_counter():
   global counter
   counter=counter+1
   if counter == 1:
      helpers.make_creature(canvas, (50, window_height-135), size=20, primary_color='steelblue', tertiary_color='steelblue4', tag='creature1')
   if counter == 2:
      helpers.make_creature(canvas, (128, window_height-135), size=23, primary_color='lightblue', secondary_color='grey99', tag='creature2')
   if counter == 3:
      helpers.make_creature(canvas, (218, window_height-135), size=27, primary_color='lemonchiffon2', secondary_color='grey99', tertiary_color='lemonchiffon3', tag='creature3')
   if counter == 4:
      helpers.make_creature(canvas, (319, window_height-135), size=30, primary_color='lightgrey', secondary_color='azure', tertiary_color='grey70', tag='creature4')
   if counter == 5:
      helpers.make_creature(canvas, (431, window_height-135), size=32, tag='creature5')
      global quitting
      quitting = True    
        
canvas.bind(KEY_PRESS, move_creature)
canvas.focus_set()

######## rendering trucks (landscape objects / flipped trucks) #######
car_1 = helpers.make_landscape_object(canvas, (1320, 90), 100, color='lightgreen', tag='car1')
car_2 = helpers.make_flipped_truck(canvas, (-300, 110), 100, tag='car2')
car_3 = helpers.make_landscape_object(canvas, (980, 330), 100, color='grey', tag='car3')
car_4 = helpers.make_flipped_truck(canvas, (280, 340), 100, color='lemonchiffon', tag='car4')
car_5 = helpers.make_landscape_object(canvas, (460, 570), 100, color='lightblue', tag='car5')
car_6 = helpers.make_landscape_object(canvas, (2000, 90), 100, color='lightgreen', tag='car6')
car_7 = helpers.make_flipped_truck(canvas, (-800, 340), 100, color='lemonchiffon', tag='car7')
car_8 = helpers.make_landscape_object(canvas, (1800, 330), 100, color='grey', tag='car8')

####### detecting collisions ########
def is_it_overlapping(tag_1:str, tag_2:str):
    totoro_top = utilities.get_top(canvas, tag_1)
    totoro_bottom = utilities.get_bottom(canvas, tag_1)
    totoro_left = utilities.get_left(canvas, tag_1)
    totoro_right = utilities.get_right(canvas, tag_1)
    truck_top = utilities.get_top(canvas, tag_2)
    truck_bottom = utilities.get_bottom(canvas, tag_2)
    truck_left = utilities.get_left(canvas, tag_2)
    truck_right = utilities.get_right(canvas, tag_2)
    if ((totoro_right <= truck_right and totoro_right >= truck_left) and (totoro_top <= truck_top and totoro_bottom >= truck_bottom)) or ((totoro_left >= truck_left and totoro_left <= truck_right) and (totoro_top <= truck_top and totoro_bottom >= truck_bottom)):
        global collision
        collision = True

######## moving trucks #########
car_1_position = 1400
car_2_position = -300
car_3_position = 980
car_4_position = 320
car_5_position = 460
car_6_position = 2000
car_7_position = -800
car_8_position = 1800
speed = 20
frame_rate = 0.001
while True:
    car_1_position = car_1_position - speed*2
    utilities.update_position_by_tag(canvas, 'car1', x=-speed*2, y=0)
    gui.update()
    time.sleep(frame_rate)
    car_3_position = car_3_position - speed
    utilities.update_position_by_tag(canvas, 'car3', x=-speed, y=0)
    gui.update()
    time.sleep(frame_rate)
    car_5_position = car_5_position - speed*2
    utilities.update_position_by_tag(canvas, 'car5', x=-speed*2, y=0)
    gui.update()
    time.sleep(frame_rate)
    car_6_position = car_6_position - speed*2
    utilities.update_position_by_tag(canvas, 'car6', x=-speed*2, y=0)
    gui.update()
    time.sleep(frame_rate)
    car_8_position = car_8_position - speed
    utilities.update_position_by_tag(canvas, 'car8', x=-speed, y=0)
    gui.update()
    time.sleep(frame_rate)
    car_2_position = car_2_position + speed
    utilities.update_position_by_tag(canvas, 'car2', x=speed, y=0)
    gui.update()
    time.sleep(frame_rate)
    car_4_position = car_4_position + speed*2
    utilities.update_position_by_tag(canvas, 'car4', x=speed*2, y=0)
    gui.update()
    time.sleep(frame_rate)
    car_7_position = car_7_position + speed*2
    utilities.update_position_by_tag(canvas, 'car7', x=speed*2, y=0)
    gui.update()
    time.sleep(frame_rate)

####### collision happening? ######
    is_it_overlapping('creature', 'car1')
    is_it_overlapping('creature', 'car2')
    is_it_overlapping('creature', 'car3')
    is_it_overlapping('creature', 'car4')
    is_it_overlapping('creature', 'car5')
    is_it_overlapping('creature', 'car6')
    is_it_overlapping('creature', 'car7')
    is_it_overlapping('creature', 'car8')

####### making trucks loop back #######
    
    if car_1_position <= -400:
        utilities.update_position_by_tag(canvas, 'car1', x=1800, y=0)
        time.sleep(frame_rate)
        car_1_position = 1400
    if car_3_position <= -400:
        utilities.update_position_by_tag(canvas, 'car3', x=1800, y=0)
        time.sleep(frame_rate)
        car_3_position = 1400
    if car_5_position <= -400:
        utilities.update_position_by_tag(canvas, 'car5', x=1800, y=0)
        time.sleep(frame_rate)
        car_5_position = 1400
    if car_6_position <= -400:
        utilities.update_position_by_tag(canvas, 'car6', x=1800, y=0)
        time.sleep(frame_rate)
        car_6_position = 1400
    if car_8_position <= -400:
        utilities.update_position_by_tag(canvas, 'car8', x=1800, y=0)
        time.sleep(frame_rate)
        car_8_position = 1400
    if car_2_position >= 1500:
        utilities.update_position_by_tag(canvas, 'car2', x=-1800, y=0)
        time.sleep(frame_rate)
        car_2_position = -300
    if car_4_position >= 1500:
        utilities.update_position_by_tag(canvas, 'car4', x=-1800, y=0)
        time.sleep(frame_rate)
        car_4_position = -300
    if car_7_position >= 1500:
        utilities.update_position_by_tag(canvas, 'car7', x=-1800, y=0)
        time.sleep(frame_rate)
        car_7_position = -300

####### winning the game #######
    if quitting == True:
        helpers.make_rectangle(canvas, (225, 250), 850, 220, color='lemonchiffon')
        canvas.create_text(
            (650, 360), 
            text="YOU WIN!", 
            font=("moonhouse", 130),
            fill = 'black')
        break
    
####### losing the game #######
    if collision == True:
        collision = False
        helpers.make_rectangle(canvas, (200, 250), 900, 220, color='lemonchiffon', tag='rect')
        canvas.create_text(
            (650, 360), 
            text="GAME OVER", 
            font=("moonhouse", 110),
            tag='text')
        MOUSE_CLICK = '<Button-1>'
        helpers.make_rectangle(canvas, (350, 475), 600, 50, color='lemonchiffon', tag='rect')
        canvas.create_text(
            (650, 500), 
            text='Click anywhere to try again', 
            font=("moonhouse", 32),
            tag='text')
        def restart_game(event):
            global counter
            counter = 0
            global totoro_position_y
            global totoro_position_x
            totoro_position_y = window_height-135
            totoro_position_x = window_width/2
            utilities.delete_by_tag(canvas, 'creature')
            utilities.delete_by_tag(canvas, 'creature1')
            utilities.delete_by_tag(canvas, 'creature2')
            utilities.delete_by_tag(canvas, 'creature3')
            utilities.delete_by_tag(canvas, 'creature4')
            utilities.delete_by_tag(canvas, 'creature5')
            utilities.delete_by_tag(canvas, 'rect')
            utilities.delete_by_tag(canvas, 'text')
            helpers.make_creature(canvas, (window_width/2, window_height-135), size=25, tag='creature')
        canvas.bind(MOUSE_CLICK, restart_game)


# makes sure the canvas keeps running:
#canvas.mainloop()
