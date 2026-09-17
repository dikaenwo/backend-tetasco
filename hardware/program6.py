from gpiozero import LED, Button
from time import sleep

# Inisialisasi LED
led1 = LED(13)
led2 = LED(19)

# Inisialisasi Push Button
button1 = Button(5, pull_up=False)
button2 = Button(6, pull_up=False)


# Fungsi DEF 1
def def1():
    print("Hidrolik ke atas")
    print("Tekan Button 1 untuk mematikan")

    while True:
        if button1.is_pressed:
            led1.off()
            led2.off()
            sleep(0.1)

            # Lompat ke DEF 2
            def2()
            break

        else:
            led1.on()
            led2.off()


# Fungsi DEF 2
def def2():
    print("Hidrolik ke Bawah")
    print("Tekan Button 2 untuk mematikan")

    while True:
        if button2.is_pressed:
            led1.off()
            led2.off()
            sleep(0.1)

            # Kembali ke DEF 1
            def1()
            break

        else:
            led1.off()
            led2.on()


# Program utama
try:

    def1()

except KeyboardInterrupt:

    print("Program dihentikan")

finally:

    led1.off()
    led2.off()
