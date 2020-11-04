for j in range(5):
    i = 0
    while i <= 4 - i:
        led.plot(0 + j, 3 - (i - j))
        i += 1
    basic.pause(200)

def on_forever():
    pass
basic.forever(on_forever)
