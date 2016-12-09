# Neopixel Colors

"""RGB values for different colors"""
RED         = (1, 0, 0)
ORANGE      = (2, 1, 0)
YELLOW      = (1, 1, 0)
GREEN       = (0, 1, 0)
LIGHTBLUE   = (0, 1, 1)
BLUE        = (0, 0, 1)
PURPLE      = (1, 0, 1)
PINK        = (2, 0, 1)

# Direction Color Choice

""" Sets color of lights based off of direction """
def color(direction):
    
    """Red for North"""
    if (337.5 < direction <= 360 or 0 <= direction <=22.5):
        color = RED
    """Orange for Northeast"""
    elif 22.5 < direction <= 67.5:
        color = ORANGE
    """Yellow for East"""
    elif 67.5 < direction <= 112.5:
        color = YELLOW
    """Green for Southeast"""
    elif 112.5 < direction <= 157.5:
        color = GREEN
    """Light blue for South"""
    elif 157.5 < direction <= 202.5:
        color = LIGHTBLUE
    """Blue for Southwest"""
    elif 202.5 < direction <= 247.5:
        color = BLUE
    """Purple for West"""
    elif 247.5 < direction <= 292.5:
        color = PURPLE
    """Pink for Northwest"""
    elif 292.5 < direction <= 337.5:
        color = PINK
    """Message for error"""
    else:
        print("Error from direction function")

    return color

# Color Intensity

""" Sets intensity of lights based off of velocity """
def intensity(velocity):
    
    """Get magnitude for light intensity"""
    light_scale = int(velocity/.36)
    if light_scale > 125:
        light_scale = 126
    else:
        print("Error from intensity function")
    
    """Apply light intensity to color"""
    color = tuple([light_scale*x for x in color])
    
    return color