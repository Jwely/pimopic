# pimopic
## About
This is a simple home monitoring project for the raspberry pi. The initial idea is to use PIR motion sensors to monitor
an area for motion, take short videos of that motion when triggered, and email those videos with an alert. For a home, this
might just be a nice way to see who is at the door or monitor access to a specific area from anywhere you have access to 
your email with low bandwidth. A fun next step may be to run human face detection on pieces of the video and run them through facial recognition models for known individuals. In a public semi-urban setting it could extend to be a neat way to collect the data required to 
count the number of unique pedestrians who walk past a given sensor with a bit more machine learning 
(assuming the images are sufficiently high resolution, which is a big *maybe*).

## Purpose
Limited utility may exist in the end result, but the **purpose** of this project is to learn
how to program with sensor hardware on the raspberry pi. As a secondary purpose, the goal is to document useful tidbits for my father, an electrical engineer of the olden days who is also venturing into raspberry pi projects.  

A simple motion detector wired through the GPIO seems like a very 
approachable hardware task and the V2 camera module is extremely approachable from the python side.

## Hardware Components
* Raspberry Pi3 
* HC-SR501 Pyroelectric Infrared PIR Motion Sensor Detector Modules (spec sheet)[http://www.mpja.com/download/31227sc.pdf]
* Pi NoIR Camera Module V2
* bread board, wires, resistors, etc

## How to use!

### Clone repository to Pi3
Open a terminal in the home directory and use the following command to clone the repository. It would be best to fork it first, and then clone your own fork. My clone command looks like this:

`git clone https://github.com/Jwely/pimopic pimopic`

### Setup configuration
Firstly, this bot sends alerts through email, so you will want to set up an email account for the bot to use.
Then we want to add this information to a config file. You should probably set permissions on this file to protect it.
The config file is of json format, and `my_config.json` can be used as a template. It looks like this:

```json
{
  "src_addr": "gmail address to send alerts FROM",
  "src_pass": "password to gmail account to send alerts FROM",
  "dest_addr": "gmail address to send the alerts TO",
  "smtp_addr": "smtp.gmail.com",
  "smtp_port": 587,
  "imap_addr": "imap.gmail.com"
}
```

At present this should be placed
