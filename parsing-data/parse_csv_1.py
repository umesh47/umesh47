import csv

#def get_min_score_difference(self):
#    parsed_data = [
#        ['Team', 'Games', 'Wins', 'Losses', 'Draws', 'Goals', 'Goals Allowed', 'Points'],
#        ['Arsenal', '38', '26', '9', '3', '79', '36', '87'],
#        ['Liverpool', '38', '24', '8', '6', '67', '30', '80']
#    ]
#    self.assertEqual(get_min_score_difference(parsed_data),'37')

def read_data(data):
    with open(data, 'r') as f:
        data = [row for row in csv.reader(f.read().splitlines())]
    return data

#-------run code --------#

data = "football.csv"
read_data(data)