# main.py -- put your code here!
imu = pyb.I2C(2, pyb.I2C.MASTER)
imu.init(pyb.I2C.MASTER, baudrate=100000)
imureader.accelquickstart(imu)
imureader.maginit(imu)
num_leds = 29
LED_strip = WS2812(spi_bus = 2, led_count = num_leds)
rgb_data = [(1, 0, 0)]*num_leds
LED_strip.show(rgb_data)
gps = pyb.UART(6, 9600, timeout=1000)
parser = MicropyGPS()

def once():
    ME_507_Project.gpstopixels(gps, parser, LED_strip, num_leds)
    
def thousand():
    for run in range(0, 1000):
        ME_507_Project.gpstopixels(gps, parser, LED_strip, num_leds)
        
def tenthousand():
    for run in range(0, 10000):
        ME_507_Project.gpstopixels(gps, parser, LED_strip, num_leds)

#for run in range(0, 100):
#    ME_507_Project.gpstopixels(gps, parser, LED_strip, num_leds)