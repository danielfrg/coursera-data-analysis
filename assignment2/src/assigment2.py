import copper

copper.project.path = '../'

print copper.Dataset(copper.read_csv('samsungData.csv'))