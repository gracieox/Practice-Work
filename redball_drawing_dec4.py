#gracie oxnam
#ball movment

import DrawingPanel

ball = DrawingPanel.DrawingPanel (300,300)

start = 10
for i in range (20):
    panel.sleep(1000)
    ball.fill_rect(0,0,300,300, 'white')
    ball.fill_oval(start, start, 50,50, 'red')
    start = start+10
