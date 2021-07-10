from source.DuplicateEmail import DuplicateEmail
from source.DuplicateOid import DuplicateOID
from source.emailer import Emailer
from source.team import Team
from source.team_member import TeamMember
import unittest


class EmailerFake:
    @staticmethod
    def get_emailer():
        return "bob@bob.com"


class TeamTests(unittest.TestCase):
    def test_create(self):
        name = "Curl Jam"
        oid = 10
        t = Team(oid, name)
        self.assertEqual(name, t.name)
        self.assertEqual(oid, t.oid)

    def test_adding_adds_to_members(self):
        t = Team(1, "Flintstones")
        tm1 = TeamMember(5, "f", "f")
        tm2 = TeamMember(6, "g", "g")
        t.add_member(tm1)
        self.assertIn(tm1, t.members)
        self.assertNotIn(tm2, t.members)
        t.add_member(tm2)
        self.assertIn(tm1, t.members)
        self.assertIn(tm2, t.members)

    def test_removing_removes_from_members(self):
        t = Team(1, "Flintstones")
        tm1 = TeamMember(5, "f", "f")
        tm2 = TeamMember(6, "g", "g")
        t.add_member(tm1)
        t.add_member(tm2)
        t.remove_member(tm1)
        self.assertNotIn(tm1, t.members)
        self.assertIn(tm2, t.members)

    def test_sending_email(self):
        """Tests Sening an email and having corrrect values for subject, message and recipients"""
        t = Team(1, "Flintstones")
        tm1 = TeamMember(5, "f", "trey.meares@me.com")
        tm2 = TeamMember(6, "g", "trey@lodestar-labs.com")
        t.add_member(tm1)
        t.add_member(tm2)
        fe = Emailer.instance()
        fe.configure("treymeares@gmail.com")
        t.send_email(fe, "S", "M")
        self.assertIn("trey.meares@me.com", fe.recipients)
        self.assertIn("trey@lodestar-labs.com", fe.recipients)
        self.assertEqual(2, len(fe.recipients))
        self.assertEqual("S", fe.subject)
        self.assertEqual("M", fe.message)

    def test_string_output_of_team(self):
        """ return a string like the following: "Team Name: N members"""
        t = Team(1, "Flintstones")
        t2 = Team(2, "Barney")
        tm1 = TeamMember(5, "f", "f")
        tm2 = TeamMember(6, "g", "g")
        tm3 = TeamMember(7, "b", "b")
        tm4 = TeamMember(8, "c", "c")
        t.add_member(tm1)
        t.add_member(tm2)
        t2.add_member(tm3)
        t2.add_member(tm4)
        self.assertEqual(str(t), "Flintstones: 2 members")
        self.assertNotEqual(str(t), "Rubies: 5 members")
        self.assertEqual(str(t2), "Barney: 2 members")

    def test_duplicate_oid(self):
        '''
        Tests for duplicate added oid
        Throws DuplicateOID error if a duplicate is found.
        :return:
        '''
        t2 = Team(1, "Flintstones")
        tm1 = TeamMember(5, "f", "f")
        tm2 = TeamMember(6, "g", "g")
        tm3 = TeamMember(6, "b", "b")
        tm4 = TeamMember(7, "f", "f")
        t2.add_member(tm1)
        self.assertIn(tm1, t2.members)
        self.assertNotIn(tm2, t2.members)
        t2.add_member(tm2)
        self.assertIn(tm1, t2.members)
        self.assertIn(tm2, t2.members)
        with self.assertRaises(DuplicateOID):
            t2.add_member(tm3)

    def test_duplicate_email(self):
        '''
        Tests for duplicate added email
        :return:
        '''
        t2 = Team(1, "Flintstones")
        tm1 = TeamMember(5, "f", "f")
        tm2 = TeamMember(6, "g", "g")
        tm3 = TeamMember(6, "b", "b")
        tm4 = TeamMember(7, "f", "f")
        t2.add_member(tm1)
        self.assertIn(tm1, t2.members)
        self.assertNotIn(tm2, t2.members)
        t2.add_member(tm2)
        self.assertIn(tm1, t2.members)
        self.assertIn(tm2, t2.members)
        with self.assertRaises(DuplicateEmail):
            t2.add_member(tm4)


if __name__ == '__main__':
    unittest.main()
