import serial
import time

# Nastavení sériové komunikace s Arduinem
ser = serial.Serial('COM3', baudrate=9600, timeout=1)
time.sleep(2)  # Čekání, než se Arduino inicializuje

def set_fan_speed(speed):
    if 0 <= speed <= 255:
        command = f"{speed}\n".encode('utf-8')  # Odeslat rychlost větráčku
        ser.write(command)
        time.sleep(0.1)  # Pauza, aby Arduino mělo čas zpracovat příkaz
        response = ser.readline().decode('utf-8').strip()
        print(response)  # Tisk zpětné vazby z Arduina
    else:
        print("Speed must be between 0 and 255")

# Test: Nastavení rychlosti větráčku na různé hodnoty
set_fan_speed(100)  # Nastavení střední rychlosti
time.sleep(5)       # Běh větráčku po dobu 5 sekund
set_fan_speed(200)  # Zvýšení rychlosti větráčku
time.sleep(5)
set_fan_speed(0)    # Zastavení větráčku

ser.close()  # Zavřít sériovou komunikaci

