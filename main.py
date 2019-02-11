from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

draw_line( 300, 300, 100, 700, screen, color)
draw_line( 300, 300, 100, 600, screen, color)
draw_line( 300, 300, 100, 500, screen, color)
draw_line( 300, 300, 100, 400, screen, color)
draw_line( 300, 300, 100, 300, screen, color)
draw_line( 300, 300, 100, 200, screen, color)
draw_line( 300, 300, 100, 100, screen, color)
draw_line( 300, 300, 100, -100, screen, color)



draw_line( 300, 300, 300, 700, screen, color)
draw_line( 300, 300, 500, 700, screen, color)
draw_line( 300, 300, 500, 600, screen, color)
draw_line( 300, 300, 500, 500, screen, color)
draw_line( 300, 300, 500, 400, screen, color)
draw_line( 300, 300, 500, 300, screen, color)
draw_line( 300, 300, 500, 200, screen, color)
draw_line( 300, 300, 500, 100, screen, color)
draw_line( 300, 300, 500, -100, screen, color)
draw_line( 300, 300, 300, 100, screen, color)

display(screen)
save_extension(screen, 'img.png')
