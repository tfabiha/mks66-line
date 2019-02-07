from display import *

def draw_line( x0, y0, x1, y1, screen, color ):

    if (x1 - x0) == 0:
        slope = 1000000
    else:
        slope = (y1 - y0) * 1.0 / (x1 - x0)

    print( slope )
    
    if 0 <= slope <= 1:
        draw_o1( x0, y0, x1, y1, screen, color )
    elif slope > 1:
        draw_o2( x0, y0, x1, y1, screen, color )
    elif -1 <= slope <= 0:
        draw_o8( x0, y0, x1, y1, screen, color )
        
def draw_o1( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0

    A = y1 - y0
    B = x0 - x1 # - ( x1 - x0 )
    d = 2*A + B

    while x <= x1:
        plot(screen, color, x, y)
        
        if d > 0:
            y += 1
            d += 2*B

        x += 1
        d += 2*A

def draw_o2( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0

    A = y1 - y0
    B = x0 - x1
    d = A + 2*B

    while y <= y1:
        plot(screen, color, x, y)

        if d < 0:
            x += 1
            d += 2*A

        y += 1
        d += 2*B
            
def draw_o8( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0

    A = y1 - y0
    B = x0 - x1 # - ( x1 - x0 )
    d = 2*A - B

    while x <= x1:
        plot(screen, color, x, y)
        
        if d < 0:
            y -=1
            d -= 2*B

        x += 1
        d += 2*A
