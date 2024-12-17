#gracie oxnam
#download and use DrawPanel

import DrawingPanel

panel = DrawingPanel.DrawingPanel (800,800)

panel.set_color("blue")
panel.draw_oval(100, 100, 30, 30)
panel.draw_oval(95, 95, 60, 60)
panel.draw_oval(86, 86, 120, 120)
panel.draw_oval(77, 77, 180, 180)
panel.draw_oval(68, 68, 240, 240)

def rect_stack(x=10, y = 10, w = 110, h=10):
    panel.set_color("red")
    for i in range(10):
        panel.draw_rect(x,y,w,h)
        y = y+10
        w = w-10
def star ():
    panel.draw_polygon(400, 50, 200, 60, 215, 70)
def rectangle():
    panel.set_color("black")
    panel.set_stroke(5)
    panel.draw_rect(400, 200, 100, 50)
    panel.fill_rect(400, 200, 100, 50, "blue")
    

rect_stack()
#star()
rectangle()



#panel.fill_rect(40, 100, 50, 80)
#panel.set_color("green")
#panel.draw_line(50, 50, 200, 250)
#pranel.fill_oval(150, 150, 50, 50, "blue")
