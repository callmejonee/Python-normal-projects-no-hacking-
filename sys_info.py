#محمد سامي منذور   <c> قاعة

import subprocess
import requests

class SystemInfo:
    def get_local_ip(self):
        """Get local IP using ipconfig (Windows)"""
        try:
            result = subprocess.check_output("ipconfig", shell=True).decode()
            for line in result.splitlines():
                if "IPv4" in line:
                    return line.split(":")[-1].strip()
            return "Local IP not found"
        except:
            return "Error: cannot get local IP"

    def get_public_ip(self):
        """Get public IP using requests"""
        try:
            return requests.get("https://api.ipify.org").text
        except:
            return "Error: cannot get public IP"

    def get_mac_address(self):
        """Get MAC address using getmac (Windows)"""
        try:
            result = subprocess.check_output("getmac", shell=True).decode()
            return result.split()[0]
        except:
            return "Error: cannot get MAC address"

    def get_wifi_password(self):
        """Get saved Wi-Fi names and passwords (Windows only)"""
        try:
            profiles_data = subprocess.check_output("netsh wlan show profiles", shell=True).decode()
            profiles = [line.split(":")[1].strip() for line in profiles_data.split("\n") if "All User Profile" in line]
            
            wifi_info = {}
            for name in profiles:
                try:
                    details = subprocess.check_output(
                        f'netsh wlan show profile "{name}" key=clear', shell=True
                    ).decode()
                    for line in details.split("\n"):
                        if "Key Content" in line:
                            wifi_info[name] = line.split(":")[1].strip()
                            break
                    else:
                        wifi_info[name] = "No password"
                except:
                    wifi_info[name] = "Error reading profile"
            return wifi_info
        except:
            return "Error: cannot get Wi-Fi info"


# ---- Task Section ----
if __name__ == "__main__":
    info = SystemInfo()
    print("Local IP:", info.get_local_ip())
    print("Public IP:", info.get_public_ip())
    print("MAC Address:", info.get_mac_address())
    print("Wi-Fi Passwords:")
    for name, pwd in info.get_wifi_password().items():
        print(f"  {name}: {pwd}")
