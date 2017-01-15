import smtplib
import os
import json
from datetime import datetime
from contextlib import contextmanager
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class BaseMessenger(object):
    """
    Base configclass that allows multiple children to read relevant info
    from one config file
    """

    def __init__(self, config_file):
        """
        :param config_file: path to json file with config info!
        """
        self.config_file = config_file
        self._parse_config()

        # set up universal attributes that all monitor subclasses must also have.
        self.outbox = []

    def _parse_config(self):
        """ Sets attributes of this emailer instance from config file"""
        with open(self.config_file, 'r') as j:
            config_dict = json.loads(j.read())
        # if attribute is already defined as None in class instances dict, update it.
        for k, v in config_dict.items():
            if k in self.__dict__.keys():
                if self.__dict__[k] is None:
                    setattr(self, k, v)
                    

class Emailer(BaseMessenger):
    """
    The emailer object sends emails from the source account to the destination
    address.
    """
    def __init__(self, config_file):
        """
        :param config_file: path to json file with config info!
        """
        # define attributes that this class should read from the config file
        self.src_addr = None
        self.src_pass = None
        self.dest_addr = None
        self.smtp_addr = None
        self.smtp_port = None

        super().__init__(config_file)

    @contextmanager
    def smtp_server(self):
        """ opens an smtp server connection for sending emails. """
        s = smtplib.SMTP(self.smtp_addr, self.smtp_port)
        s.starttls()
        s.login(self.src_addr, self.src_pass)
        try:
            yield s
        except:
            raise
        finally:
            s.quit()

    def build_message(self, subject, body, attachment=None):
        """ adds a email message to the outbox for later sending. """
        msg = MIMEMultipart()
        msg['From'] = self.src_addr
        msg['To'] = self.dest_addr
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        if attachment is not None:
            if os.path.exists(attachment):
                with open(attachment, 'rb') as a:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(a.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', 'attachment; filename= {}'.format(attachment))
                    msg.attach(part)

        self.outbox.append(msg)

    def send(self):
        """ sends all the messages in the outbox """
        with self.smtp_server() as s:
            for msg in self.outbox:
                s.sendmail(self.src_addr, self.dest_addr, msg.as_string())

        # TODO: this is a sloppy way to do outbox cleanup.
        self.outbox = []


class TextMessager(BaseMessenger):
    def __init__(self, config_file):
        super().__init__(config_file)
        raise NotImplementedError('finish me!')


if __name__ == "__main__":
    # just some quick scratch tests.
    e = Emailer('jeff_config.json')
    e.build_message('Test test test woooo', 'butts', 'README.md')
    e.send()
