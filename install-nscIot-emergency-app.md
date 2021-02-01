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
   
   if GPIO.input(BtnPin1):     # if port BtnPin1 == 1  
      print('Broadcasting off\r')
      requests.post('http://localhost:8091/nscIotService/media/live/end')  
   else: 
      print('Broadcasting on\r')
      requests.post('http://localhost:8091/nscIotService/media/live/start')
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
   sudo nano /etc/rc.local
   ```

   Add following line at the end of configuration file. Before ```exit 0``` tag
   ```text
   ....

   sudo python3 /home/pi/nscIotService-emergency-button/nsc-emergency-button.py &
   exit 0
   ```
- **Reboot the Pi to test it:**
   ```text
   sudo reboot
   ```
