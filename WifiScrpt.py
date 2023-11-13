import os
import subprocess
import socket
import time

def check_internet(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.create_connection((host, port), timeout)
        return True
    except OSError:
        pass
    return False

def connect_to_wifi(ssid, password):
    # Format the command to connect to WiFi
    cmd = f"netsh wlan connect name={ssid} ssid={ssid} keyMaterial={password}"

    # Connect to WiFi using subprocess
    subprocess.run(cmd, shell=True)

def main():
    # Set your WiFi SSID and password
    wifi_ssid = "YourWiFiSSID"
    wifi_password = "YourWiFiPassword"

    while True:
        if not check_internet():
            print("Disconnected from WiFi. Reconnecting...")
            connect_to_wifi(wifi_ssid, wifi_password)
        else:
            print("Connected to WiFi.")

        # Check the connection every 10 seconds
        time.sleep(10)

if __name__ == "__main__":
    main()
