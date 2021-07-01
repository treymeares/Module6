# Trey Meares M3 Project
from module6.DuplicateOid import DuplicateOID
from module6.identified_object import IdentifiedObject


class League(IdentifiedObject):

    @property
    def name(self):
        '''
        Property for the league name
        :return: the league name
        '''
        return self._name

    @property
    def teams(self):
        '''
        Property for the teams participating
        :return: teams participating list
        '''
        return self._teams_list

    @property
    def competitions(self):
        '''
        Property for the competitions
        :return: a list of competitions
        '''
        return self._competition_list

    def __init__(self, oid, name):
        '''
        Constructor for league
        :param oid: taken from super
        :param name: Name of competitions
        '''
        super().__init__(oid)
        self._name = name
        self._teams_list = []
        self._competition_list = []

    def add_team(self, team):
        '''
        Add a team to competition
        :param team: team property
        :return: teams appended to add team
        '''
        if team not in self._teams_list:
            return self._teams_list.append(team)
        else:
            raise DuplicateOID(team)

    def add_competition(self, competition):
        '''
        Add a competition to list
        :param competition: competition property
        :return:competitions appended to add competition
        '''
        if competition not in self._competition_list:
            return self._competition_list.append(competition)
        else:
            raise DuplicateOID(competition)

    def teams_for_member(self, member):
        '''
        a list of all teams for which member plays
        :param member: member to locate teams for
        :return: return a list of all teams for which member plays
        '''
        return [s for s in self.teams if member in s.members]

    def competitions_for_team(self, team):
        '''
        a list of all competitions in which team is participating
        :param team: teams to search competitions for
        :return: return a list of all competitions in which team is participating
        '''

        return [x for x in self.competitions if team.name in str(x)]

    def competitions_for_member(self, member):
        '''
        a list of all competitions for which member played on one of the competing teams
        :param member:
        :return: return a list of all competitions for which member played on one of the competing teams
        '''
        print(member)
        return [s for s in self.competitions for y in s.teams_competing if member in y.members]

    def __str__(self):
        '''
        Override __str__ method
        :return:"League Name: N teams, M competitions"
        '''
        return f"{self.name}: {len(self._teams_list)} teams, {len(self.competitions)} competitions"
