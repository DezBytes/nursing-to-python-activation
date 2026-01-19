# The '370' Orb Frequency Script
import time

def orb_pulse(sequence):
    print("--- INITIATING HANDSHAKE ---")
    for digit in str(sequence):
        # We use % to create a cyclical frequency, like a pulse
        frequency = (int(digit) * 10) + 7 
        print(f"Pulsing at {frequency}Hz... Digit: {digit}")
        time.sleep(0.5) 
    print("--- DOWNLOAD COMPLETE ---")

# The code you saw on the phone/orb
orb_pulse(370)
