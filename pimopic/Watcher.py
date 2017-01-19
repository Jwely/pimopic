import time


class Watcher(object):
    """ this is the base watcher object """

    def __init__(self, camera, triggers, alarms, messenger):
        """

        :param camera: an instance of PiCameraManager
        :param triggers: a list of IOclasses.Input instances
        :param alarms: a list of IOClass.Output instances
        :param messenger: a child class instance of Messengers.BaseMessenger
        """
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
                    'body': 'See image!',
                    'attachment': image
                }
                self.report(report_content)
                time.sleep(0.5)
            else:
                self.quiet_alarms()
                time.sleep(0.1)