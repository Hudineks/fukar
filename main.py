import serial
import time

# Nastavení sériové komunikace s Flexy2 Air (nahraďte správným COM portem)
ser = serial.Serial('COM3', baudrate=115200, timeout=1)
time.sleep(2)  # Krátká pauza pro inicializaci zařízení

# Funkce pro zapnutí ventilátoru na plnou rychlost
def fan_on():
    ser.write(b'<F:255>\n')  # Odeslání příkazu pro plnou rychlost ventilátoru
    time.sleep(0.1)  # Krátká pauza pro zpracování
    response = ser.readline().decode('utf-8').strip()  # Čtení odpovědi
    print(f"Odpověď zařízení: {response}")

# Funkce pro vypnutí ventilátoru
def fan_off():
    ser.write(b'<F:0>\n')  # Odeslání příkazu pro vypnutí ventilátoru
    time.sleep(0.1)
    response = ser.readline().decode('utf-8').strip()
    print(f"Odpověď zařízení: {response}")

# Dvoupolohová regulace: přepínání mezi zapnutím a vypnutím ventilátoru
try:
    while True:
        command = input("Zadejte 'on' pro zapnutí ventilátoru nebo 'off' pro vypnutí: ").strip().lower()
        if command == 'on':
            fan_on()
        elif command == 'off':
            fan_off()
        else:
            print("Neplatný příkaz. Zadejte 'on' nebo 'off'.")
except KeyboardInterrupt:
    print("Program byl přerušen.")
finally:
    ser.close()  # Zavření sériové komunikace

