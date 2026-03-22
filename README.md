# axis-cameras
Experimenting with legacy Axis P12 MK II cameras and modular sensors.

## Current Setup 
* **Main Unit:** AXIS P12 MK II (PoE required).
* **Sensor:** 2.1mm 1/3" IR CUT.

---

## Connectivity Guide

### 1. Check if the Camera is Alive
Run this to see if the camera is sending data to your computer:
```bash
sudo tcpdump -i eno1 -n
```
*Look for `0.0.0.0` or `ac:cc:8e` in the output.*

### 2. Set Permanent Static IP (PC)
Run these commands to ensure your PC always has the correct IP (`192.168.0.10`) for the camera, even after a reboot:

```bash
# Create the connection profile
sudo nmcli con add type ethernet con-name axis-static ifname eno1 ip4 192.168.0.10/24

# Set to connect automatically
sudo nmcli con mod axis-static connection.autoconnect yes

# Activate the connection
sudo nmcli con up axis-static
```

### 3. Access the Camera
Open your browser and enter the address based on your firmware version:

* **Old Firmware (< 11.8):** `http://192.168.0.90` (Default)
* **New Firmware (≥ 11.8):** `http://169.254.X.X` (Auto-assigned)

> **Pro Tip:** Also `ip neighbor show dev eno1` could be used to find the camera's auto-assigned IP.

