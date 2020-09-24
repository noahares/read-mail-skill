from mycroft import MycroftSkill, intent_file_handler
import mailbox
from time import sleep

mail_dirs = ['~/.mail/yahoo/Inbox/', '~/.mail/kit/INBOX/']

class ReadMail(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('mail.read.intent')
    def handle_mail_read(self, message):
        for dir in mail_dirs:
            for message in mailbox.Maildir(dir):
                if not "S" in message.get_flags():
                    self.speak(message['subject'])
                    self.speak('from')
                    self.speak(message['from'])
                    sleep(2)

def stop(self):
    pass

def create_skill():
    return ReadMail()
