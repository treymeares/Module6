# Trey Meares M3 Project
import keyring
import yagmail


class Emailer:
    # used to send a email to team or
    _sole_instance = None
    sender_address = ""

    def __int__(self):
        self.recipients = None
        self.subject = None
        self.message = None

    @classmethod
    def instance(cls):
        '''
        Class method to return sole instance of emailer
        :return: sole instance of emailer
        '''
        if cls._sole_instance is None:
            cls._sole_instance = cls()
        return cls._sole_instance

    @classmethod
    def configure(cls, sender_address):
        '''
        Class to configure sender address
        :param sender_address: address of one sending email
        :return: sender address
        '''
        cls.sender_address = sender_address


    def send_plain_email(self, recipients, subject, message):
        '''
        Plain Email sender
        :param recipients: recipients of email
        :param subject: subject of email
        :param message: return message of email
        :return: the email to send
        '''
        self.recipients = recipients
        self.subject = subject
        self.message = message
        sent_email = f"Sending mail to: {recipients[0:]}"
        yag = yagmail.SMTP(self.sender_address, keyring.get_password("yagmail", self.sender_address))
        yag.send(to=recipients, subject=subject, contents=message)
        print(f"Email sent to: {recipients}")
        return sent_email
