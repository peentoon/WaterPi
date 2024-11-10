# Install the OS

Download Raspberry Pi OS installer from https://www.raspberrypi.com/software/

Select Raspberry OS Lite 32

Customize settings via advanced options menu (CTRL+SHIFT+X to access it):
- Give it a name
- Configure WiFi
- Define main user and its password
- Activate SSH

Flash on SD Card.

Insert it into Raspberry PI and boot.

# Connect to the Raspberry PI from Windows

// TODO: Assign static IP to the device

Find IP of Raspberry Pi in your Network:
- either by logging into the web interface and your router and scrolling the list of connected devices
- or from the Command Prompt, using `arp -a` before and after turning on the Pi, to find the newly added IP.
- or via arp-scan (https://github.com/royhills/arp-scan) `arp-scan --localnet`
 
Install PuTTY from https://www.putty.org/

Open putty and configure a new session:
- Host Name (or IP Address): <IP of the PI>
- Port: 22
- Saved Sessions: give it a name and click Save

Connect to the newly created session (Click the session name -> Load -> Open).

Login with the user defined at OS creation.

All next steps will be done from the SSH session in the Pi.

# Update Raspberry OS Lite
```
sudo apt update -y && sudo apt upgrade -y
```
# Setup Flask

Install pip to manage a virtual environment:
```
sudo apt install pip
```

Make a project directory, create a virtual env and install Flask there:
```
mkdir waterpi-backend
cd waterpi-backend
python -m venv pythonenv
. pythonenv/bin/activate
pip install Flask
```





