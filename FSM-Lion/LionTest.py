from unittest import TestCase
from Lion import Lion
import unittest


class LionTest(TestCase):

    def test_init(self):
        lion = Lion("Hungry")
        self.assertEqual("Hungry", lion.FSM.current_state)
        self.assertIsNone(lion.FSM.prev_state)
        self.assertIsNone(lion.FSM.action)

        lion = Lion("Fed")
        self.assertEqual("Fed", lion.FSM.current_state)
        self.assertIsNone(lion.FSM.prev_state)
        self.assertIsNone(lion.FSM.action)

        lion = Lion("Crazy")
        self.assertEqual("Crazy", lion.FSM.current_state)  # it's ok, but transition will be not found
        self.assertIsNone(lion.FSM.prev_state)
        self.assertIsNone(lion.FSM.action)

    def test_meet_antelope(self):
        lion = Lion("Hungry")
        lion.meet("Antelope")
        self.assertEqual("Hungry", lion.FSM.prev_state)
        self.assertEqual("Fed", lion.FSM.current_state)
        self.assertEqual("Eat", lion.FSM.action)

        lion = Lion("Fed")
        lion.meet("Antelope")
        self.assertEqual("Fed", lion.FSM.prev_state)
        self.assertEqual("Hungry", lion.FSM.current_state)
        self.assertEqual("Sleep", lion.FSM.action)

    def test_meet_hunter(self):
        lion = Lion("Hungry")
        lion.meet("Hunter")
        self.assertEqual("Hungry", lion.FSM.prev_state)
        self.assertEqual("Hungry", lion.FSM.current_state)
        self.assertEqual("Run away", lion.FSM.action)

        lion = Lion("Fed")
        lion.meet("Hunter")
        self.assertEqual("Fed", lion.FSM.prev_state)
        self.assertEqual("Hungry", lion.FSM.current_state)
        self.assertEqual("Run away", lion.FSM.action)

    def test_meet_tree(self):
        lion = Lion("Hungry")
        lion.meet("Tree")
        self.assertEqual("Hungry", lion.FSM.prev_state)
        self.assertEqual("Hungry", lion.FSM.current_state)
        self.assertEqual("Sleep", lion.FSM.action)

        lion = Lion("Fed")
        lion.meet("Tree")
        self.assertEqual("Fed", lion.FSM.prev_state)
        self.assertEqual("Hungry", lion.FSM.current_state)
        self.assertEqual("Look", lion.FSM.action)

    def test_meet_tiger(self):
        lion = Lion("Hungry")
        self.assertRaises(Exception, lion.meet, "Tiger")

        lion = Lion("Fed")
        self.assertRaises(Exception, lion.meet, "Tiger")


if __name__ == '__main__':
    unittest.main()