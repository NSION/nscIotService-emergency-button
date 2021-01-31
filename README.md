# nscIotService-emergency-button
"This repository is under development" - nscIotService API example.

This software repository is intended to familiarize usage of the nscIotService API services. As an example functionality is to route analog button signal input to the nscIotService API. The example implementation is based on Raspberry Pi 4 platform [GPIO pinouts](https://www.raspberrypi.org/documentation/usage/gpio/) and an application is programmed by Python3 language. All of the components are running on Raspberry Pi 4 computer.

Deployment specific repository of [nscIotService-docker](https://github.com/NSION/nscIotService-docker). Covering instruction to install nscIotService into Raspberry Pi 4 platform.
## Workflow: GPIO pinouts to API
<img src="https://github.com/NSION/nscIotService-emergency-button/blob/main/nscIotService-API-example1.png" width="800" height="480">

### API Reference implementation "nsc-emergency-button.py" application
- [Installation instructions of "nsc-emergency-button" application](https://github.com/NSION/nscIotService-emergency-button/blob/main/install-nscIot-emergency-app.md)

## API specifications:
### NSC3 IOT client API specification:
nscIotService API service is located on edge computer. The IotClient API is designed to offer management interface for an external application like Car dashboard application where the corresponding dashboard UI could control basic functionalities regarding media broadcasting operations.
RestAPI is responding at localhost:809x port of IOT client server.

| **Path** | **Request params** | **Response** | **Description** |
| :--- |     :---      |   :---  |       :---  |
| POST /media/live/start | { incidentNumber: STRING // task id, patrolId: STRING // patrol id } | text/plain 200: "Started live" 400: "Bad params"  | Start live streaming |
| POST /media/video POST /media/clip | { incidentNumber: STRING // task id, patrolId: STRING // patrol id, fullPath: STRING // path to image on disk, timeStampStart: LONG // epoch time in milliseconds, timeStampEnd: LONG // epoch time in milliseconds }     | 200: "Send clip {fullPath}", 400: "Bad params" / "Upload buffer full" | Video clip send  |
| POST /media/image | { incidentNumber: STRING // task id, patrolId: STRING // patrol id, fullPath: STRING // path to image on disk captured, TimeStamp: LONG // epoch time in milliseconds } | 200: "Send image {fullPath}", 400: "Bad params" / "Upload buffer full"  | Single image send  |
| POST /inputsource/select/{id} | id (from input source/list)     | 200: ok  | Select input source  |
| POST /media/live/end | -     | text/plain 200: "End live"  | End live streaming  |
| GET /inputsource/list | -    | 200: ok APPLICATION_JSON: { "sources": [{"id":"xx", "type":"yyy", "name":"zzz", "description":"kkkk"} ]}  | Retrieve list of available sources  |
| GET /status/streaming | - | { liveStreaming: "active" / "inactive", connectionStatus: "connected" / "disconnected"}  | Live streaming status  |
| GET /status/uploadStatus | - | { tasksInQueue: INTEGER }  | Upload task status, number of tasks in upload queue  |
| GET /status/buffer | - | 200: ok APPLICATION_JSON { "bufferFillPercentage":0}  | Retrieve upload buffer status  |

As example: Curl command to start and stop streaming:

Start: ```curl -X POST http://localhost:8091/nscIotService/media/live/start```

Stop: ```curl -X POST http://localhost:8091/nscIotService/media/live/end```

As example: wget command to get status of broadcasting:

```wget -qO- http://localhost:8091/nscIotService/status/streaming```


