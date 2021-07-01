import csv
import os
import pickle
from os import path

from module6.team import Team
from module6.league import League
from module6.team_member import TeamMember


class LeagueDatabase:
    _sole_instance = None

    def __init__(self):
        self._last_oid = 0
        self._leagues_list = []

    @classmethod
    def instance(cls):
        """Creates the sole instance of the class."""
        if cls._sole_instance is None:
            cls._sole_instance = cls()
        return cls._sole_instance

    @classmethod
    def load(cls, file_name):
        try:
            try:
                with open(file_name, mode="rb") as f:
                    cls._sole_instance = pickle.load(f)
                    return cls._sole_instance
            except FileNotFoundError:
                backup = f"{file_name}.backup"
                with open(backup, mode="rb") as f:
                    cls._sole_instance = pickle.load(f)
                    return cls._sole_instance
        except FileNotFoundError:
            print("File not found.")
            raise

    @property
    def leagues(self):
        return self._leagues_list

    def add_league(self, league):
        self._leagues_list.append(league)

    def next_oid(self):
        self._last_oid += 1
        return self._last_oid

    def save(self, file_name):
        if path.exists(file_name):
            os.rename(file_name, f"{file_name}.backup")
        with open(file_name, mode="wb") as f:
            pickle.dump(self, f)

    def import_league(self, league_name, file_name):
        try:
            with open(file_name, "r", encoding="utf-8-sig") as f:
                csvreader = csv.reader(f)
                # This skips the first row of the CSV file.
                next(csvreader)
                _last_oid = len(self.leagues)
                new_league_to_add = League(self.next_oid(), league_name)
                self.add_league(new_league_to_add)
                list_of_teams_in_league = []
                for row in csvreader:
                    team_name = row[0]
                    team_member = row[1]
                    member_email = row[2]
                    _last_oid = len(new_league_to_add.teams)
                    team_member = TeamMember(self.next_oid(), team_member, member_email)
                    if len(new_league_to_add.teams) == 0:
                        team_name = Team(self.next_oid(), team_name)
                        new_league_to_add.add_team(team_name)
                        team_name.add_member(team_member)
                        list_of_teams_in_league.append(str(team_name.name))
                        continue
                    elif team_name in list_of_teams_in_league:
                        for x in new_league_to_add.teams:
                            for y in x.name.split(":"):
                                if y == team_name:
                                    x.add_member(team_member)
                        continue
                    else:
                        team_name = Team(self.next_oid(), team_name)
                        team_name.add_member(team_member)
                        new_league_to_add.add_team(team_name)
                        list_of_teams_in_league.append(str(team_name.name))
                print(list_of_teams_in_league)
        except FileNotFoundError:
            print("CSV File was not found for importing")
            raise

    def export_league(self, league, file_name):
        try:
            with open(file_name, 'w', newline='') as outcsv:
                writer = csv.writer(outcsv)
                writer.writerow(["Team Name", "Member Name", "Member Email"])
                list_league = []
                for x in league.teams:
                    teamname = x.name
                    for y in x.members:
                        membername = y.name
                        memberemail = y.email
                        to_csv = [teamname, membername, memberemail]
                        list_league.append(to_csv)
                writer.writerows(list_league)
        except Exception:
            print("Error has been encountered!")
            raise


if __name__ == "__main__":
    # league1 = League(3, "Another league 2")
    # t1 = Team(1, "t1")
    # t2 = Team(2, "t2")
    # t3 = Team(3, "t3")
    # all_teams = [t1, t2, t3]
    # league1.add_team(t1)
    # league1.add_team(t2)
    # league1.add_team(t3)
    # tm1 = TeamMember(1, "Fred", "fred")
    # tm2 = TeamMember(2, "Barney", "barney")
    # tm3 = TeamMember(3, "Wilma", "wilma")
    # tm4 = TeamMember(4, "Betty", "betty")
    # tm5 = TeamMember(5, "Pebbles", "pebbles")
    # tm6 = TeamMember(6, "Bamm-Bamm", "bam-bam")
    # tm7 = TeamMember(7, "Dino", "dino")
    # tm8 = TeamMember(8, "Mr. Slate", "mrslate")
    # t1.add_member(tm1)
    # t1.add_member(tm2)
    # t2.add_member(tm3)
    # t2.add_member(tm4)
    # t2.add_member(tm5)
    # t3.add_member(tm6)
    # t3.add_member(tm7)
    # t3.add_member(tm8)
    # new1 = LeagueDatabase()
    # new1.add_league(league1)
    # print(new1.leagues)
    # new1.save("Pickler.pickle")

    db = LeagueDatabase.load('NewFolks.pickle')
    for x in db.leagues:
        print(x)
