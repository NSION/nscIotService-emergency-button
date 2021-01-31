# nscIotService-emergency-button
"This repository is under development" - nscIotService API example.

This software repository is intended to familiarize usage of the nscIotService API services. As an example functionality is to route analog button signal input to the nscIotService API. The example implementation is based on Raspberry Pi 4 platform [GPIO pinouts](https://www.raspberrypi.org/documentation/usage/gpio/) and an application is programmed by Python3 language. All of the components are running on Raspberry Pi 4 computer.

Deployment specific repository of [nscIotService-docker](https://github.com/NSION/nscIotService-docker). Covering instruction to install nscIotService into Raspberry Pi 4 platform.
## Workflow: GPIO pinouts to API
<img src="https://github.com/NSION/nscIotService-emergency-button/blob/main/nscIotService-API-example1.png" width="800" height="480">

## API specifications:
### NSC3 IOT client API specification:
nscIotService API service is located on edge computer. The IotClient API is designed to offer management interface for an external application like Car dashboard application where the corresponding dashboard UI could control basic functionalities regarding media broadcasting operations.
RestAPI is responding at localhost:809x port of IOT client server.

| Path | Request params | Response | Description |
| :--- |     :---:      |   :---:  |       ---:  |
|```POST /media/live/start``` | ```{
incidentNumber: STRING, // task id
patrolId: STRING, // patrol id
}```      | ```text/plain
200: "Started live"
400: "Bad params"```  | ```Start live streaming```  |
| :--- |     :---:      |   :---:  |       ---:  |
| :--- |     :---:      |   :---:  |       ---:  |
| :--- |     :---:      |   :---:  |       ---:  |
| :--- |     :---:      |   :---:  |       ---:  |
| :--- |     :---:      |   :---:  |       ---:  |
| :--- |     :---:      |   :---:  |       ---:  |
| :--- |     :---:      |   :---:  |       ---:  |
| :--- |     :---:      |   :---:  |       ---:  |
| :--- |     :---:      |   :---:  |       ---:  |
| :--- |     :---:      |   :---:  |       ---:  |
| :--- |     :---:      |   :---:  |       ---:  |
| :--- |     :---:      |   :---:  |       ---:  |
| :--- |     :---:      |   :---:  |       ---:  |
| :--- |     :---:      |   :---:  |       ---:  |
