# create a unit test for challenge 1
import unittest
import pandas as pd

from challenge_1 import do_challenge_1


class TestChallenge1(unittest.TestCase):
    def test_do_challenge_1(self):
        df_in = pd.read_csv("challenge_1_test.in", sep=" ", header=None)
        df_out = pd.read_csv("challenge_1_test.out", sep=" ", header=None)
        # check if df_in and df_out are equal
        self.assertTrue(df_in.equals(df_out))