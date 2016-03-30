# -*- coding: utf-8 -*-

"""
    Module unit_test - les tests unitaires
    ======================================

    Ce module inclut les test unitaires a effectuer. La plupart des modules servant a gerer un base de donnees, il devient difficile d'effectuer des tests unitaires sur les fonctions de ces dernieres. Nous n'en avons donc implementer qu'un seul.
"""

import unittest
from importers.utils.CSVPusher import csvPusher

class TestCsvPusher(unittest.TestCase):

    def test_csvPusher(self):

        path = "../csv/test.csv";
        testList = [['YO', 'YA', 'YU'], ['BO', 'BA', 'BU BU']]
        toTestList = csvPusher(path)
        self.assertEqual(toTestList, testList)

if __name__ == '__main__':
    unittest.main()
