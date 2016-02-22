import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('max_columns', 50)
#%matplotlib inline


#################################################
#########SERIES OBJECT PANDAS####################
#############INITIALS############################
#################################################
#creating series with default indexes
def series_default():
    s = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'])

#creating series with specific indexes
def series_indexes():
    s = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'],
              index=['A', 'Z', 'C', 'Y', 'E'])

#creating series from dictionary - keys will be marked as indexes
def series_dict():
    d = {'Chicago': 1000, 'New York': 1300, 'Portland': 900, 'San Francisco': 1100,
     'Austin': 450, 'Boston': None}
    cities = pd.Series(d)
    print cities
    series_operation(cities, False)

#various series operations
def series_operations(data, ex=False):
    if(ex):
        print data[cities < 1000]
        print cities[['Chicago', 'Portland', 'San Francisco']]
        print cities['Chicago']
        less_than_1000 = cities < 1000
        print less_than_1000
        print '\n'
        print cities[less_than_1000]

def pandas_operations(cities):
    print cities / 3    
    np.square(cities)
    
    # returns a boolean series indicating which values aren't NULL
    cities.notnull()
    print cities.isnull()

#################################################
#########DATAFRAME PANDAS########################
#############INITIALS############################
#################################################

data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
football = pd.DataFrame(data, columns=['year', 'team', 'wins', 'losses'])
football

    

