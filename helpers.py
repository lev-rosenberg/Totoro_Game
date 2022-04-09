import utilities

######
from creature_helpers import make_oval, make_circle, body_mark #this is so that I could take my creature from hw3
######
def make_creature(canvas, center:tuple, size:int, tag:str, primary_color:str='darkgrey', secondary_color:str='lemonchiffon2', tertiary_color:str='grey'):

    # face: 
    make_circle(canvas, (center[0], center[1]-size*1.25), size*1.25, fill=primary_color, tag=tag)

    #body: 
    canvas.create_polygon(
        [(center[0]-size*1.75,center[1]-size*2),
         (center[0]-size*1.75,center[1]+size*2),
         (center[0]+size*1.75,center[1]+size*2),
         (center[0]+size*1.75,center[1]-size*2)],
        fill=primary_color,
        smooth=True,
        tag=tag)

    #inside body:
    canvas.create_polygon(
        [(center[0]-size*1.5,center[1]-size*1.15),
         (center[0]-size*1.5,center[1]+size*1.9),
         (center[0]+size*1.5,center[1]+size*1.9),
         (center[0]+size*1.5,center[1]-size*1.15)],
        fill=secondary_color,
        smooth=True,
        tag=tag)

  #arm flaps:
    canvas.create_polygon(
        [(center[0]+size*1.4,center[1]-size*0.4),
         (center[0]+size*0.9,center[1]+size*0.1),
         (center[0]+size*1.2,center[1]+size*0.2),
         (center[0]+size*1.7,center[1]-size*0.1)],
        fill=primary_color,
        smooth=True,
        tag=tag)

    canvas.create_polygon(
        [(center[0]-size*1.4,center[1]-size*0.4),
         (center[0]-size*0.9,center[1]+size*0.1),
         (center[0]-size*1.2,center[1]+size*0.2),
         (center[0]-size*1.7,center[1]-size*0.1)],
        fill=primary_color,
        smooth=True,
        tag=tag)
    
    #body marks (see helpers for function def):
    body_mark(canvas, center, size, primary_color, tag=tag)
    body_mark(canvas, (center[0]-size*0.8, center[1]+size*0.15), size, primary_color, tag=tag)
    body_mark(canvas, (center[0]+size*0.8, center[1]+size*0.15), size, primary_color, tag=tag)
    body_mark(canvas, (center[0]-size*0.35, center[1]+size*0.35), size, primary_color, tag=tag)
    body_mark(canvas, (center[0]+size*0.35, center[1]+size*0.35), size, primary_color, tag=tag)
    body_mark(canvas, (center[0]-size*1, center[1]+size*0.45), size, primary_color, tag=tag)
    body_mark(canvas, (center[0]+size*1, center[1]+size*0.45), size, primary_color, tag=tag)

    # eyes: 
    make_circle(canvas, (center[0]+size*0.5, center[1]-size*1.9), size*0.15, fill='white', outline='black', tag=tag)
    make_circle(canvas, (center[0]-size*0.5, center[1]-size*1.9), size*0.15, fill='white', outline='black', tag=tag)
    make_circle(canvas, (center[0]+size*0.47, center[1]-size*1.9), size*0.07, fill='black', tag=tag)
    make_circle(canvas, (center[0]-size*0.47, center[1]-size*1.9), size*0.07, fill='black', tag=tag)
    make_circle(canvas, (center[0]+size*0.49, center[1]-size*1.92), size*0.02, fill='white', tag=tag)
    make_circle(canvas, (center[0]-size*0.45, center[1]-size*1.92), size*0.02, fill='white', tag=tag)

    #ears: 
    make_oval(canvas, (center[0]+size*0.6, center[1]-size*2.6), size*0.17, size*0.4, fill=primary_color, tag=tag)
    make_oval(canvas, (center[0]-size*0.6, center[1]-size*2.6), size*0.17, size*0.4, fill=primary_color, tag=tag)

    #nose:
    canvas.create_polygon(
    [(center[0]+size*0.15,center[1]-size*1.9),
     (center[0],center[1]-size*1.8),
     (center[0]-size*0.15,center[1]-size*1.9)],
    fill='black',
    smooth=True,
    tag=tag)

    #whiskers left
    canvas.create_line(
    [(center[0]-size*1.7,center[1]-size*1.75),
     (center[0]-size*0.9, center[1]-size*1.75)],
    width=1,
    tag=tag)
    canvas.create_line(
    [(center[0]-size*1.65,center[1]-size*1.9),
     (center[0]-size*0.85, center[1]-size*1.8)],
    width=1,
    tag=tag)
    canvas.create_line(
    [(center[0]-size*1.6,center[1]-size*1.6),
     (center[0]-size*0.95, center[1]-size*1.65)],
    width=1,
    tag=tag)

    #whiskers right
    canvas.create_line(
    [(center[0]+size*1.7,center[1]-size*1.75),
     (center[0]+size*0.9, center[1]-size*1.75)],
    width=1,
    tag=tag)
    canvas.create_line(
    [(center[0]+size*1.65,center[1]-size*1.9),
     (center[0]+size*0.85, center[1]-size*1.8)],
    width=1,
    tag=tag)
    canvas.create_line(
    [(center[0]+size*1.6,center[1]-size*1.6),
     (center[0]+size*0.95, center[1]-size*1.65)],
    width=1,
    tag=tag)

    #mouth
    canvas.create_line(
    [(center[0]-size*0.04,center[1]-size*1.5),
     (center[0],center[1]-size*1.53),
     (center[0]+size*0.04,center[1]-size*1.5)],
    width=1,
    smooth=True,
    tag=tag)

    #feet
    canvas.create_polygon(
    [(center[0]-size*1.25,center[1]+size*1.25),
     (center[0]-size*0.8,center[1]+size*2),
     (center[0]-size*0.1,center[1]+size*1.9),
     (center[0]-size*0.5, center[1]+size*0.8)],
    fill=primary_color,
    smooth=True,
    tag=tag)
    canvas.create_polygon(
    [(center[0]+size*1.25,center[1]+size*1.25),
     (center[0]+size*0.8,center[1]+size*2),
     (center[0]+size*0.1,center[1]+size*1.9),
     (center[0]+size*0.5, center[1]+size*0.8)],
    fill=primary_color,
    smooth=True,
    tag=tag)

    #pads
    make_circle(canvas, (center[0]-size*0.48, center[1]+size*1.7), size*0.26, fill=tertiary_color, tag=tag)
    make_circle(canvas, (center[0]+size*0.48, center[1]+size*1.7), size*0.26, fill=tertiary_color, tag=tag)

    #toes
    make_circle(canvas, (center[0]-size*0.72, center[1]+size*1.63), size*0.05, fill='lightgrey', tag=tag)
    make_circle(canvas, (center[0]-size*0.63, center[1]+size*1.51), size*0.05, fill='lightgrey', tag=tag)
    make_circle(canvas, (center[0]-size*0.5, center[1]+size*1.46), size*0.05, fill='lightgrey', tag=tag)

    make_circle(canvas, (center[0]+size*0.72, center[1]+size*1.63), size*0.05, fill='lightgrey', tag=tag)
    make_circle(canvas, (center[0]+size*0.63, center[1]+size*1.51), size*0.05, fill='lightgrey', tag=tag)
    make_circle(canvas, (center[0]+size*0.5, center[1]+size*1.46), size*0.05, fill='lightgrey', tag=tag)

def make_rectangle(canvas, top_left, width, height, color="#3D9970", tag=None, outline='black', stroke_width=2):
    x, y = top_left
    return canvas.create_rectangle(
        [(x, y), (x + width, y + height)], 
        fill=color, 
        width=stroke_width,
        tags=tag,
        outline=outline)
def make_landscape_object(canvas, center:tuple, size:int, tag:str, color:str='white'):
    x = center[0]-size/2
    y = center[1]-size/2
    #truck wheels
    make_rectangle(canvas, (x+size*0.15, y+size*0.4), size*0.25, size*0.1, color='black', tag=tag)
    make_rectangle(canvas, (x+size*1.5, y+size*0.4), size*0.25, size*0.1, color='black', tag=tag)
    make_rectangle(canvas, (x-size*0.25, y+size*0.38), size*0.2, size*0.1, color='black', tag=tag)
    make_rectangle(canvas, (x-size*0.25, y-size*0.02), size*0.2, size*0.1, color='black', tag=tag)
    make_rectangle(canvas, (x+size*0.15, y-size*0.04), size*0.25, size*0.1, color='black', tag=tag)
    make_rectangle(canvas, (x+size*1.5, y-size*0.04), size*0.25, size*0.1, color='black', tag=tag)
    #truck body
    make_rectangle(canvas, (x-size*0.5, y + size*0.1), size*0.4, size*0.25, color=color, tag=tag)
    make_rectangle(canvas, (x-size*0.35, y + size*0.03), size*0.3, size*0.4, color=color, tag=tag)
    make_rectangle(canvas, (x, y), size*2, size*0.46, color=color, tag=tag)
def make_flipped_truck(canvas, center:tuple, size:int, tag:str, color:str='white'):
    x = center[0]+size/2
    y = center[1]+size/2
    #truck wheels
    make_rectangle(canvas, (x+size*0.15, y+size*0.4), size*0.25, size*0.1, color='black', tag=tag)
    make_rectangle(canvas, (x+size*1.5, y+size*0.4), size*0.25, size*0.1, color='black', tag=tag)
    make_rectangle(canvas, (x+size*2.1, y+size*0.38), size*0.15, size*0.1, color='black', tag=tag)
    make_rectangle(canvas, (x+size*2.1, y-size*0.02), size*0.15, size*0.1, color='black', tag=tag)
    make_rectangle(canvas, (x+size*0.15, y-size*0.04), size*0.25, size*0.1, color='black', tag=tag)
    make_rectangle(canvas, (x+size*1.5, y-size*0.04), size*0.25, size*0.1, color='black', tag=tag)
    #truck body
    make_rectangle(canvas, (x+size*2.15, y + size*0.1), size*0.4, size*0.25, color=color, tag=tag)
    make_rectangle(canvas, (x+size*2.05, y + size*0.03), size*0.3, size*0.4, color=color, tag=tag)
    make_rectangle(canvas, (x, y), size*2, size*0.46, color=color, tag=tag)
    


