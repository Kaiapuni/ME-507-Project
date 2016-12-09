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
    
#    Red for North
    if (337.5 < direction <= 360 or 0 <= direction <= 22.5):
        out = RED
#    Orange for Northeast
    elif 22.5 < direction <= 67.5: 
        out = ORANGE
#    Yellow for East
    elif 67.5 < direction <= 112.5:
        out = YELLOW
#    Green for Southeast
    elif 112.5 < direction <= 157.5:
        out = GREEN
#    Light blue for South
    elif 157.5 < direction <= 202.5:
        out = LIGHTBLUE
#    Blue for Southwest
    elif 202.5 < direction <= 247.5:
        out = BLUE
#    Purple for West
    elif 247.5 < direction <= 292.5:
        out = PURPLE
#    Pink for Northwest
    elif 292.5 < direction <= 337.5:
        out = PINK
#    Message for error
    else:
        print("Error from direction function")

    return out

# Color Intensity

""" Sets intensity of lights based off of velocity """
def intensity(velocity):
    
#    Get magnitude for light intensity
    light_scale = int(velocity/.36)
    if light_scale > 125:
        light_scale = 126
    else:
        print("Error from intensity function")
    
#    Apply light intensity to color
    color = tuple([light_scale*x for x in color])
    
    return color
    
def brightness(velocity):
    """ This function returns a single factor for later use. """
    
#    Get magnitude for light intensity
    light_scale = int(velocity/.36)
    if light_scale > 125:
        light_scale = 126
#    else:
#        return -1
    
    return light_scale
    
def merge(course, speed):
    """ This function returns RGB values ready for output to LEDs. """
    
    base = color(course)
    factor = brightness(speed)
    return tuple([factor*x for x in base])