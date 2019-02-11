from display import *

def draw_line( x0, y0, x1, y1, screen, color ):

    # set x1 to be greater than x0
    if (x1 < x0):
        draw_line(x1, y1, x0, y0, screen, color )
        return;

    # find the slope
    if (x1 - x0) == 0:
        if y1 > y0:
            slope = 1000000
        else:
            slope = -1000000
    else:
        slope = (y1 - y0) * 1.0 / (x1 - x0)

    print( slope )

    # variables constant through any octant
    x = x0
    y = y0
    A = y1 - y0
    B = x0 - x1
    
    if 0 <= slope <= 1: # 1st and 5th octants
        draw_o1( x, y, x1, y1, A, B, screen, color )
    elif slope > 1: # 2nd and 6th octants
        draw_o2( x, y, x1, y1, A, B, screen, color )
    elif -1 <= slope <= 0: # 4th and 8th octants
        draw_o8( x, y, x1, y1, A, B, screen, color )
    else: # 3rd and 7th octants
        draw_o7( x, y, x1, y1, A, B, screen, color )
        
def draw_o1( x, y, x1, y1, A, B, screen, color ):

    d = 2*A + B

    while x <= x1:
        plot(screen, color, x, y)
        
        if d > 0:
            y += 1
            d += 2*B

        x += 1
        d += 2*A

def draw_o2( x, y, x1, y1, A, B, screen, color ):

    d = A + 2*B

    while y <= y1:
        plot(screen, color, x, y)

        if d < 0:
            x += 1
            d += 2*A

        y += 1
        d += 2*B
            
def draw_o8( x, y, x1, y1, A, B, screen, color ):

    d = 2*A - B

    while x <= x1:
        plot(screen, color, x, y)
        
        if d < 0:
            y -= 1
            d -= 2*B
            
        x += 1
        d += 2*A
            
def draw_o7( x, y, x1, y1, A, B, screen, color ):

    d = A - 2*B

    while y >= y1:
        plot(screen, color, x, y)
        
        if d > 0:
            x += 1
            d += 2*A

        y -=1
        d -= 2*B

def something( org_x, org_y, top_x, top_y, screen):

    counter = 100
    while( counter > 0):#org_x != top_x, org_y != top_y ):
        
        draw_line(top_x - top_y + org_y, top_y - top_x + org_x,
                  top_x + top_y - org_y, top_y + top_x - org_x,
                  screen, [(top_x + 50) % 255, (top_y + 70) % 255, (top_x + top_y + 20) % 255])

        top_x -= 5
        org_y -= 5
        counter -= 1
