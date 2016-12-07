# main.py -- put your code here!
imu = pyb.I2C(2, pyb.I2C.MASTER)
imu.init(pyb.I2C.MASTER, baudrate=100000)
imureader.accelquickstart(imu)
imureader.maginit(imu)
LED_strip = WS2812(spi_bus = 2, led_count = 29)
rgb_data = [(1, 0, 0)]*29
LED_strip.show(rgb_data)
gps = pyb.UART(6, 9600)