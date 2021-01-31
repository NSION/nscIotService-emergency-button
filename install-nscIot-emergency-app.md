# NSC-IOT Emergency button app:

Installation instruction for "NSC-IOT Emergency button" Python app. 

### Prerequisites

- [x] Raspberry Pi 4 with 4GB RAM
- [x] [nscIotService](https://github.com/NSION/nscIotService-docker/blob/main/Installation-nscIotService.md) is installed
- [x] Python3 installed on RPi. (enabled by default in RPi OS specific distros)

### Install Raspberry python development specific tools and libraries 

- **Log into RPi via ssh or local terminal:**

- **Update repository:**

```sudo apt-get update```

- **RPi python development kit:**

```sudo apt-get install python-dev```

- **RPi.GPIO:**

```sudo apt-get install python-rpi.gpio```

### Download python code

```cd~ ```
```git clone https://github.com/NSION/nscIotService-emergency-button.git ```

### Define route between button and video stream

```cd nscIotService-emergency-button ```
```nano 
