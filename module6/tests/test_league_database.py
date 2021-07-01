import unittest
import os
from module6.league_database import LeagueDatabase
from module6.league import League
from module6.team import Team


class MyTestCase(unittest.TestCase):

    def test_3_import_league_reads_utf_8_values(self):
        qb = LeagueDatabase.instance()
        qb.import_league("NPlayers", "../scrambled_teams.csv")
        league_1 = qb.leagues[0]
        self.assertEqual("NPlayers", league_1.name)
        self.assertEqual(4, len(league_1.teams))
        t_names = ['Flintstones', 'Cold Fingers', 'Curl Jam', 'Curl Power']
        t1_mem_names = ["Fred Flintstone", "Barney Rubble", "Betty Rubble", "Wilma Flintstone"]
        t2_mem_names = ["佐藤 ひな", "成神 陽太", "伊座並 杏子", "国宝 阿修羅", "成神 空"]
        t3_mem_names = ["Vedder, Eddie", "Cameron, Matt", "Gossard, Stone",
                        "McCready, Mike", "Ament, Jeff"]
        t4_mem_names = ["Buttercup", "Bubbles", "Blossom", "Mojo Jojo"]
        for t in league_1.teams:
            self.assertIn(t.name, t_names)
            if t.name == 'Flintstones':
                for mem in t.members:
                    self.assertIn(mem.name, t1_mem_names)
            elif t.name == 'Cold Fingers':
                for mem in t.members:
                    self.assertIn(mem.name, t2_mem_names)
            elif t.name == 'Curl Jam':
                for mem in t.members:
                    self.assertIn(mem.name, t3_mem_names)
            elif t.name == 'Curl Power':
                for mem in t.members:
                    self.assertIn(mem.name, t4_mem_names)

    def test_2_export_league_reads_utf_8_values(self):
        db = LeagueDatabase.instance()
        db.import_league("RPlayers", "../scrambled_teams.csv")
        league_1 = db.leagues[0]
        db.export_league(league_1, "../Fighters.csv")
        self.assertTrue(os.path.isfile("../Fighters.csv"))

    def test_1_dumping_a_pickle_with_imported_league(self):
        nb = LeagueDatabase.instance()
        nb.import_league("NPlayers", "../scrambled_teams.csv")
        nb.save("../NewTester.pickle")
        self.assertTrue(os.path.isfile("../NewTester.pickle"))

    def test_d_loading_a_file_does_not_exist(self):
        t = Team(1, "Ice Maniacs")
        league = League(1, "AL State Curling League")
        league.add_team(t)
        league2 = League(2, "Titans")
        first_league = LeagueDatabase()
        first_league.add_league(league)
        first_league.add_league(league2)
        with self.assertRaises(FileNotFoundError):
            first_league.load("../Folks1.pkl")
        with self.assertRaises(FileNotFoundError):
            first_league.load("../Folks1.backup")

    def test_save_file(self):
        t = Team(1, "Ice Maniacs")
        league = League(1, "AL State Curling League")
        league.add_team(t)
        league2 = League(2, "Titans")
        fast_league = LeagueDatabase()
        fast_league.add_league(league)
        fast_league.add_league(league2)
        fast_league.save("../GoodFolks1.pickle")
        self.assertTrue(os.path.isfile("../GoodFolks1.pickle"))

    def test_1_save_file_as_backup(self):
        t = Team(1, "Ice Maniacs")
        league = League(1, "AL State Curling League")
        league.add_team(t)
        first_league_1 = LeagueDatabase.instance()
        first_league_1.add_league(league)
        first_league_1.save("../NewFolks.pickle")
        first_league_1.save("../NewFolks.pickle")
        self.assertTrue(os.path.isfile("../NewFolks.pickle.backup"))

    def test_f_exporting_csv_file_does_exist(self):
        first_league = LeagueDatabase.instance()
        with self.assertRaises(FileNotFoundError):
            first_league.import_league("league2", "../Teams1.csv")

    def test_g_load_file_and_check_for_team(self):
        db1 = LeagueDatabase.load("../NewTester.pickle")
        teams_loaded = []
        for x in db1.leagues:
            teams_loaded.append(str(x))
        self.assertEqual(teams_loaded, ['NPlayers: 4 teams, 0 competitions'])


if __name__ == '__main__':
    unittest.main()
