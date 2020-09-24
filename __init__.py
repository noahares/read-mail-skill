from mycroft import MycroftSkill, intent_file_handler


class ReadMail(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('mail.read.intent')
    def handle_mail_read(self, message):
        self.speak_dialog('mail.read')


def create_skill():
    return ReadMail()

