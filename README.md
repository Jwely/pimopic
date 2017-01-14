# pimopic
This is a simple home monitoring project for the raspberry pi. The initial idea is to use PIR motion sensors to monitor
an area for motion, take short videos of that motion when triggered, and email those videos with an alert. For a home, this
might just be a nice way to see whos at the door or monitor access to a specific area from anywhere you have access to 
your emailwith low bandwidth. A fun next step may be to run human face detection on pieces of the video and 
compare them against known faces to identify frequent visitors.
In a public semi-urban setting it could extend to be a neat way to collect the data required to 
count the number of unique pedestrians who walk past a given sensor with a bit more machine learning 
(assuming the images are sufficiently high resolution, which is a big *maybe*).

Limited utility may exist in the end result, but the **purpose** of this project is to learn
how to program with sensor hardware on the raspberry pi. A simple motion detector wired through the GPIO seems like a very 
approachable hardware task and the V2 camera module is extremely approachable from the python side.

## Primary components
* Raspberry Pi3 
* HC-SR501 Pyroelectric Infrared PIR Motion Sensor Detector Modules
* Pi NoIR Camera Module V2
* bread board, wires, resistors, etc

## Help resources used


## Log


