import serial
import time

ser = serial.Serial('COM3', baudrate=9600, timeout=1)  # Nahraďte správným COM portem
time.sleep(2)  # Počkejte, až se zařízení inicializuje

while True:
    line = ser.readline().decode('utf-8').strip()
    if line:
        print(f"Received: {line}")  # Zobrazí data přijatá ze zařízení


import serial
import time

# Nastavení sériové komunikace s Flexy2 Air
ser = serial.Serial('COM3', baudrate=9600, timeout=1)
time.sleep(2)  # Čekání na inicializaci zařízení

# Funkce pro odesílání příkazů a čtení odpovědi
def send_command(command):
    ser.write(f"{command}\n".encode('utf-8'))  # Odeslat příkaz
    time.sleep(0.1)  # Pauza pro zpracování
    response = ser.readline().decode('utf-8').strip()  # Čtení odpovědi
    print(f"Response: {response}")

# Testovací příkazy
send_command('POWER_ON')  # Vyzkouší zapnutí zařízení
send_command('SET_SPEED 100')  # Vyzkouší nastavení rychlosti na 100
send_command('GET_STATUS')  # Zjistí aktuální stav zařízení

ser.close()






import serial
import time

# Nastavení sériové komunikace s Flexy2 Air
ser = serial.Serial('COM3', baudrate=9600, timeout=1)  # Nahraďte 'COM3' správným portem
time.sleep(2)  # Krátká pauza pro inicializaci zařízení

# Příklad funkce pro zapnutí Flexy2 Air
def turn_on_device():
    command = 'POWER_ON\n'  # Příkaz pro zapnutí zařízení, podle dokumentace zařízení
    ser.write(command.encode())  # Odeslat příkaz
    time.sleep(0.1)  # Pauza pro zpracování
    response = ser.readline().decode('utf-8').strip()  # Čtení odpovědi ze zařízení
    print(response)  # Výpis odpovědi

# Příklad funkce pro ovládání otáček (např. rychlost větráčku)
def set_speed(speed):
    command = f'SET_SPEED {speed}\n'  # Příkaz pro nastavení rychlosti
    ser.write(command.encode())  # Odeslat příkaz
    time.sleep(0.1)
    response = ser.readline().decode('utf-8').strip()
    print(response)

# Příklad použití
turn_on_device()
set_speed(100)  # Nastavení rychlosti na hodnotu 100

# Uzavření sériové komunikace
ser.close()


