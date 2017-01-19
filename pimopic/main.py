from pimopic.Messengers import Emailer
from pimopic.PiCameraManager import PiCameraManager
from pimopic.IOclasses import Input, Output

from pimopic.Watcher import Watcher

msensor1 = Input(11)
msensor2 = Input(13)
led = Output(16)
camera = PiCameraManager()
messenger = Emailer('jeff_config.json')

if __name__ == "__main__":
    w = Watcher(camera,
                [msensor1, msensor2],
                [led],
                messenger)
    w.watch()
                
                
                
        

    
        
        

