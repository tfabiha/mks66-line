from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

draw_line( 50, 50, 170, 300, screen, color)

display(screen)
save_extension(screen, 'img.png')
