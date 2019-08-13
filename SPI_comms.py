import pigpio

pi = pigpio.pi()
if not pi:
   end()
spi_h = pi.spi_open(0, 100000, 0)
(count, data) = pi.spi_xfer(spi_h, [0xFF, 0x0A, 0x01, 0x00])
print ("Bytes transferred: " + str(count))
print (list(data))