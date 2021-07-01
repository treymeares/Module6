import datetime
import unittest

from module6.competition import Competition
from module6.fake_emailer import FakeEmailer
from module6.team import Team
from module6.team_member import TeamMember
from module6.emailer import Emailer


class CompetitionTests(unittest.TestCase):
    def test_create(self):
        now = datetime.datetime.now()
        t1 = Team(1, "Team 1")
        t2 = Team(2, "Team 2")
        t3 = Team(3, "Team 3")
        c1 = Competition(1, [t1, t2], "Here", None)
        c2 = Competition(2, [t2, t3], "There", now)

        self.assertEqual("Here", c1.location)
        self.assertEqual(1, c1.oid)
        self.assertIsNone(c1.date_time)
        self.assertEqual(2, len(c1.teams_competing))
        self.assertIn(t1, c1.teams_competing)
        self.assertIn(t2, c1.teams_competing)
        self.assertNotIn(t3, c1.teams_competing)

        self.assertEqual("There", c2.location)
        self.assertEqual(2, c2.oid)
        self.assertEqual(now, c2.date_time)
        self.assertEqual(2, len(c2.teams_competing))
        self.assertNotIn(t1, c2.teams_competing)
        self.assertIn(t2, c2.teams_competing)
        self.assertIn(t3, c2.teams_competing)

    def test_sends_email(self):
        now = datetime.datetime.now()
        t1 = Team(1, "Team 1")
        mem_1 = TeamMember(1, "Joe", "jp1@aub.edu")
        mem_2 = TeamMember(2, "James", "f1@foo.com")
        mem_3 = TeamMember(3, "Jolt", "jolt1@aub.edu")

        t1.add_member(mem_1)
        t1.add_member(mem_2)
        t1.add_member(mem_3)

        t2 = Team(2, "Team 2")
        mem_4 = TeamMember(1, "Joe", "jp2@aub.edu")
        mem_5 = TeamMember(2, "James", "f2@foo.com")
        mem_6 = TeamMember(3, "Jolt", "jolt2@aub.edu")
        t2.add_member(mem_4)
        t2.add_member(mem_5)
        t2.add_member(mem_6)

        t3 = Team(3, "Team 3")
        mem_7 = TeamMember(1, "Joe", "jp3@aub.edu")
        mem_8 = TeamMember(2, "James", "f3@foo.com")
        mem_9 = TeamMember(3, "Jolt", "jolt3@aub.edu")
        t3.add_member(mem_7)
        t3.add_member(mem_8)
        t3.add_member(mem_9)

        e = Emailer()
        e.configure("treymeares@gmail.com")
        c = Competition(1, [t1, t2, t3], "Here", None)
        c.send_email(e, "S", "M")

        self.assertIn("jp1@aub.edu", e.recipients)
        self.assertIn("f1@foo.com", e.recipients)
        self.assertIn("jolt1@aub.edu", e.recipients)
        self.assertIn("jp2@aub.edu", e.recipients)
        self.assertIn("f2@foo.com", e.recipients)
        self.assertIn("jolt2@aub.edu", e.recipients)
        self.assertIn("jp3@aub.edu", e.recipients)
        self.assertIn("f3@foo.com", e.recipients)
        self.assertIn("jolt3@aub.edu", e.recipients)

        self.assertEqual(9, len(e.recipients))
        self.assertEqual("S", e.subject)
        self.assertEqual("M", e.message)

    def test_string_output_of_competition(self):
        now = datetime.datetime.now().strftime('%M:%S.%f')[:-4]
        t1 = Team(1, "Team 1")
        t2 = Team(2, "Team 2")
        t3 = Team(3, "Team 3")
        c1 = Competition(1, [t1, t2], "Here", None)
        c2 = Competition(2, [t2, t3], "There", now)

        self.assertEqual(str(c2), f"Competition at There on {now} with 2 teams")
        self.assertEqual(str(c1), f"Competition at Here with 2 teams")


if __name__ == '__main__':
    unittest.main()
