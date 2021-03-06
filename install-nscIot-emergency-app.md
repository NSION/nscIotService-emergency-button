# NSC-IOT Emergency button app:

Installation instruction for "NSC-IOT Emergency button" Python app. 

### Prerequisites:

- [x] Raspberry Pi 4 with 4GB RAM
- [x] [nscIotService](https://github.com/NSION/nscIotService-docker/blob/main/Installation-nscIotService.md) is installed
- [x] Python3 installed on RPi. (enabled by default in RPi OS specific distros)

### Install Raspberry python development specific tools and libraries:

- **Log into RPi via ssh or local terminal as pi user:**

- **Update repository:**

   ```sudo apt-get update```

- **RPi python development kit:**

   ```sudo apt-get install python-dev```

- **RPi.GPIO:**

   ```sudo apt-get install python-rpi.gpio```
   
- **Installing pip for Python 3 **

   Ubuntu 18.04 ships with Python 3, as the default Python installation. Complete the following steps to install pip (pip3) for Python 3:

   Start by updating the package list using the following command:

   ```sudo apt update```
   
   Use the following command to install pip for Python 3:
   
   ```sudo apt install python3-pip```
   
   The command above will also install all the dependencies required for building Python modules.
   
   Install RPI GPIO PIP Module:
   
   ``` sudo pip3 install RPi.GPIO ```
   
   

### Download the repository:
   
   ```text
   cd~
   git clone https://github.com/NSION/nscIotService-emergency-button.git 
   ```
   Grant execute permission for shell scripts:
   ```text
   cd ~/nscIotService-emergency-button
   chmod u+x *.sh
   ```

### Define route between button and video stream:

- **List camera sources:**
   ```text
   cd ~/nscIotService-emergency-button
   ./nscIotService-inbound-streams.sh
   ```
   As an example printout:
   ```text
   *************************************************************
   List of rtsp url addresses configured per camera: 

   Camera1, Port:8091, RTSP URL:rtsp://user:passwd@192.168.1.213:88/videoMain 
   Camera2, Port:8092, RTSP URL:rtsp://user:passwd@192.168.1.214:88/videoMain 
   ```
- **Modify Python script:**
   ```text
   cd ~/nscIotService-emergency-button
   nano nsc-emergency-button.py
   ```
- **Define GPIO pin number of button as BCM layout format:**

   ``` BtnPin1 = 23    # pin23 --- button1 ```

   More details about [BCM GPIO pin layout](https://pinout.xyz/)

- **Define the corresponding port number:**

   As an example Camera1 > Port 8091

   ```text
   
  def switch(channel):
    if GPIO.input(BtnPin1):
        print('Broadcasting on\r')
        requests.post('http://localhost:8091/nscIotService/media/live/start')
    if not GPIO.input(BtnPin1):
        print('Broadcasting off\r')
        requests.post('http://localhost:8091/nscIotService/media/live/end')   
   ```
   Save changes ```<ctrl>``` button and X, "Y" Yes, and ENTER

### Test functionality:
- **Start app in debug mode:**
   
   ```text 
   sudo python3 nsc-emergency-button.py 
   ```
   Status of broadcasting is displayed on screen.

### Run a Program On Your Raspberry Pi At Startup:
- **Configure run level conf:** 
   ```text
   sudo chmod +x /etc/rc.local
   sudo nano /etc/rc.local
   ```

   Add following lines at the end of configuration file. Before the ```exit 0``` line.
   ```text
   ....
   sleep 30
   sudo python3 /home/pi/nscIotService-emergency-button/nsc-emergency-button.py &
   exit 0
   ```
- **Reboot the Pi to test it:**
   ```text
   sudo reboot
   ```
