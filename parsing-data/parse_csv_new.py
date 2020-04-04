import unittest
from parse_csv_1 import read_data, get_min_score_difference


class ParseCSVTest(unittest.TestCase):

    def setUp(self):
        self.data = 'football.csv'

    def test_csv_read_data_headers(self):
        self.assertEqual(
            read_data(self.data)[0],
            ['Team', 'Games', 'Wins', 'Losses', 'Draws', 'Goals', 'Goals Allowed', 'Points']
        )

    def test_csv_read_data_team_name(self):
        self.assertEqual(read_data(self.data)[1][0], 'Arsenal')
    
    def test_csv_read_data_points(self):
        self. assertEqual(read_data(self.data)[1][7],'87')

    def test_get_min_score_difference(self):
        parsed_data = [
           ['Team', 'Games', 'Wins', 'Losses', 'Draws', 'Goals', 'Goals Allowed', 'Points'],
           ['Arsenal', '38', '26', '9', '3', '79', '36', '87'],
           ['Liverpool', '38', '24', '8', '6', '67', '30', '80']
        ]
        self.assertEqual(get_min_score_difference(parsed_data),37.0)


if __name__=='__main__':
    unittest.main()
