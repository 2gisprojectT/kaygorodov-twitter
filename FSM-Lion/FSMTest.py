from unittest import TestCase
from FSM import FSM
import unittest


class FSMTest(TestCase):

    def test_init(self):
        fsm = FSM("start")
        self.assertEqual("start", fsm.current_state)
        self.assertIsNone(fsm.prev_state)
        self.assertIsNone(fsm.action)
        self.assertEqual({}, fsm.transitions)

    def test_add_transition_4args(self):
        fsm = FSM("off")
        fsm.add_transition("play", "off", "music", "on")
        self.assertEqual(("music", "on"), fsm.transitions[("play", "off")])

    def test_add_transition_3args(self):
        fsm = FSM("on")
        fsm.add_transition("change", "on", "radio")
        self.assertEqual(("radio", "on"), fsm.transitions[("change", "on")])

    def test_execute_transition_found(self):
        fsm = FSM("off")
        fsm.add_transition("play", "off", "music", "on")
        fsm.execute("play")
        self.assertEqual("music", fsm.action)
        self.assertEqual("off", fsm.prev_state)
        self.assertEqual("on", fsm.current_state)

    def test_execute_transition_not_found(self):
        fsm = FSM("off")
        fsm.add_transition("play", "off", "music", "on")
        self.assertRaises(Exception, fsm.execute, "stop")
        self.assertIsNone(fsm.action)
        self.assertIsNone(fsm.prev_state)
        self.assertEqual("off", fsm.current_state)


if __name__ == '__main__':
    unittest.main()