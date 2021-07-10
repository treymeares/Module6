# Trey Meares M3 Project
from source.DuplicateEmail import DuplicateEmail
from source.identified_object import IdentifiedObject
from source.DuplicateOid import DuplicateOID


class Team(IdentifiedObject):
    # Forms the teams for the TeamMembers
    @property
    def name(self):
        '''
        Property for name of team
        :return: The name of the team
        '''
        return self._name

    @property
    def members(self):
        '''
        Property for members of teh team
        :return: the members of teh team in a list
        '''
        return self._members_list

    def __init__(self, oid, name):
        '''
        Constructor for the Team class.
        :param oid: takes the id from the super class, identified obj
        :param name:takes in the name of the team
        '''
        super().__init__(oid)
        self._name = name
        self._members_list = []

    def add_member(self, member):
        '''
        Adds a memebr to the team list
        Throws exception
        :param member: takes in the member property
        :return: a member appended to the list
        '''
        for s in self.members:
                for x in s.email:
                    if member.email == x:
                        raise DuplicateEmail(member)
        if member in self._members_list:
            raise DuplicateOID(member)
        elif member not in self._members_list:
            self._members_list.append(member)

    def remove_member(self, member_to_remove):
        '''
        Removes a memebr from the members list.
        :param member_to_remove: takes a memebr to remove from the team
        :return: a list with the memebr removed.
        '''
        self._members_list.remove(member_to_remove)

    def send_email(self, emailer, subject, message):
        '''
                Function to gather info to send into the emailer class and send email
                :param emailer: inistaes the email class to send an email
                :param subject: subject of email(not currently used)
                :param message: message of email(not currently used)
                :return: the output from the emailer class
                '''
        to_get_email = []
        for s in self.members:
            for y in s.email.split():
                if y == None:
                    continue
                else:
                    to_get_email.append(s.email)
        emailer.recipients = to_get_email
        sent_email = emailer.send_plain_email(to_get_email, subject, message)
        return sent_email

    def __str__(self):
        '''
        override __str__ class
        :return:return  return a string like the following: "Team Name: N members"
        '''
        return f"{self.name}: {len(self.members)} members"
