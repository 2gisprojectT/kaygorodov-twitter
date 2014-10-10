from unittest import TestCase
from Lion import Lion
import unittest


class LionTest(TestCase):

    def test_init(self):
        #positive tests
        lion = Lion("Hungry")
        self.assertEqual("Hungry", lion.FSM.current_state)
        self.assertIsNone(lion.FSM.prev_state)
        self.assertIsNone(lion.FSM.action)

        lion = Lion("Fed")
        self.assertEqual("Fed", lion.FSM.current_state)
        self.assertIsNone(lion.FSM.prev_state)
        self.assertIsNone(lion.FSM.action)

        #negative tests
        lion = Lion("Crazy")
        self.assertEqual("Crazy", lion.FSM.current_state)  # it's ok, but transition will be not found
        self.assertIsNone(lion.FSM.prev_state)
        self.assertIsNone(lion.FSM.action)

    def test_meet(self):
        # positive tests
        lion = Lion("Hungry")
        lion.meet("Antelope")
        self.assertEqual("Hungry", lion.FSM.prev_state)
        self.assertEqual("Fed", lion.FSM.current_state)
        self.assertEqual("Eat", lion.FSM.action)

        lion = Lion("Hungry")
        lion.meet("Hunter")
        self.assertEqual("Hungry", lion.FSM.prev_state)
        self.assertEqual("Hungry", lion.FSM.current_state)
        self.assertEqual("Run away", lion.FSM.action)

        lion = Lion("Hungry")
        lion.meet("Tree")
        self.assertEqual("Hungry", lion.FSM.prev_state)
        self.assertEqual("Hungry", lion.FSM.current_state)
        self.assertEqual("Sleep", lion.FSM.action)

        lion = Lion("Fed")
        lion.meet("Antelope")
        self.assertEqual("Fed", lion.FSM.prev_state)
        self.assertEqual("Hungry", lion.FSM.current_state)
        self.assertEqual("Sleep", lion.FSM.action)

        lion = Lion("Fed")
        lion.meet("Hunter")
        self.assertEqual("Fed", lion.FSM.prev_state)
        self.assertEqual("Hungry", lion.FSM.current_state)
        self.assertEqual("Run away", lion.FSM.action)

        lion = Lion("Fed")
        lion.meet("Tree")
        self.assertEqual("Fed", lion.FSM.prev_state)
        self.assertEqual("Hungry", lion.FSM.current_state)
        self.assertEqual("Look", lion.FSM.action)

        # negative tests
        lion = Lion("Fed")
        self.assertRaises(Exception, lion.meet, "Tiger")


if __name__ == '__main__':
    unittest.main()