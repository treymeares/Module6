# Trey Meares M3 Project

from source.identified_object import IdentifiedObject


class TeamMember(IdentifiedObject):
    # used to set the team members for the teams
    @property
    def name(self):
        '''
        Property for name of team member
        :return: name of the team member
        '''
        return self._name

    @name.setter
    def name(self, mem_name):
        self._name = mem_name

    @property
    def email(self):
        '''
        Property for email of team member
        :return: the email of tyhe team member
        '''
        return self._email

    @email.setter
    def email(self, mem_em):
        self._email = mem_em

    def __init__(self, oid, name, email):
        '''
        Constructor for TeamMember
        :param oid: id of the team memebr
        :param name: name of the team member
        :param email: email of the team member
        '''
        super().__init__(oid)
        self._name = name
        self._email = email

    def send_email(self, emailer, subject, message):
        '''
        Function to gather info to send into the emailer class and send email
        :param emailer: inistaes the email class to send an email
        :param subject: subject of email(not currently used)
        :param message: message of email(not currently used)
        :return: the output from the emailer class
        '''
        return emailer.send_plain_email([self.email], subject, message)

    def __str__(self):
        '''
        Override __str__
        :return: a string with the name and email of each team member
        '''
        return f"{self._name} <{self._email}>"
