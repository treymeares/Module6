# Trey Meares M3 Project

from source.identified_object import IdentifiedObject


class Competition(IdentifiedObject):
# Competition class for defining competitions between teams
    @property
    def teams_competing(self):
        '''
        Property for teams competing
        :return: all teams competing against another
        '''
        return self._teams

    @property
    def date_time(self):
        '''
        Property for date and System time
        :return: current date and system time
        '''
        return self._date_time

    @property
    def location(self):
        '''
        Property for location
        :return: location of competition
        '''
        return self._location

    def __init__(self, oid, teams, location, date_time):
        '''
        Constructor for competition
        :param oid: gets oid from super
        :param teams: makes teams list
        :param location: takes in locations from user
        :param date_time: takes in date time from system
        '''
        super().__init__(oid)
        self._teams = teams
        self._location = location
        self._date_time = date_time

    def send_email(self, emailer, subject, message):
        '''
                Function to gather info to send into the emailer class and send email
                :param emailer: inistaes the email class to send an email
                :param subject: subject of email(not currently used)
                :param message: message of email(not currently used)
                :return: the output from the emailer class
                '''
        self.emailer = emailer
        self.subject = subject
        self.message = message
        to_get_email = []

        while True:
            for s in self.teams_competing:
                for y in s.members:
                    for p in y.email.split():
                        if p == None:
                            continue
                        else:
                            to_get_email.append(p)
            emailer.recipients = to_get_email
            sent_email = emailer.send_plain_email(to_get_email, subject, message)
            return sent_email

    def __str__(self):
        '''
        Overrides string method
        :return:  "Competition at location on date_time with N teams"
        (note: date_time may be None in which case just omit the "on date_time" part.
        '''
        if self.date_time is None:
            return f"Competition at {self.location} with {len(self.teams_competing)} teams"
        else:
            return f"Competition at {self.location} on {self.date_time} with {len(self.teams_competing)} teams"
