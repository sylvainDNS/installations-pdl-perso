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
