from Messengers import Emailer
from PiCameraManager import PiCameraManager
from ioclass import Input, Output
import time


msensor1 = Input(11)
msensor2 = Input(13)
led = Output(16)
camera = PiCameraManager()
messenger = Emailer('jeff_config.json')


class Watcher(object):

    def __init__(self, camera, triggers, alarms, messenger):
        self.camera = camera
        self.triggers = triggers
        self.alarms = alarms
        self.messenger = messenger

    def report(self, message_dict):
        self.messenger.build_message(**message_dict)
        self.messenger.send()

    def check_triggers(self):
        if any([t.ison for t in self.triggers]):
            return True
        else:
            return False

    def raise_alarms(self):
        print('raise alarms!')
        for alarm in self.alarms:
            alarm.set_on()

    def quiet_alarms(self):
        for alarm in self.alarms:
            alarm.set_off()

    def watch(self):

        while True:
            # if tripped raise alarms and start recording
            if self.check_triggers():
                self.raise_alarms()
                image = self.camera.capture()
                report_content = {
                    'subject': 'Alert!',
                    'body': 'See video',
                    'attachment': image
                }
                self.report(report_content)
                time.sleep(0.5)
            else:
                self.quiet_alarms()
                time.sleep(0.1)


if __name__ == "__main__":
    w = Watcher(camera,
                [msensor1, msensor2],
                [led],
                messenger)
    w.watch()
                
                
                
        

    
        
        

