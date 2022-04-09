import pandas as pd
from pathlib import Path
import datetime


dir = 'data/raw/'

def create_fixtures():
    """
    Creates fixture table
    - Checks if exists, if not then create
    """
    path = Path(dir + 'fixtures.csv')

    if path.is_file():
        print(f'The file {path} exists')
    else:
        print('File does not exist')
        df = pd.DataFrame(
            {
            'fixture_id': pd.Series(dtype='int'),
            'referee': pd.Series(dtype='str'),
            'timestamp': pd.Series(dtype='int'),
            'venue_id': pd.Series(dtype='int'),
            'home_id': pd.Series(dtype='int'),
            'away_id': pd.Series(dtype='int'),
            'created_datetime': pd.Series(dtype='datetime64[ns]'),
            'modified_datetime': pd.Series(dtype='datetime64[ns]')
            }
        )

        df.to_csv(path, index=False)

def create_predictions():
    """
    Creates predictions table
    - Checks if exists, if not then create
    """
    path = Path(dir + 'predictions.csv')

    if path.is_file():
        print(f'The file {path} exists')
    else:
        print('File does not exist')
        df = pd.DataFrame(
            {
            'fixture_id': pd.Series(dtype='int'),
            'referee': pd.Series(dtype='str'),
            'timestamp': pd.Series(dtype='int'),
            'venue_id': pd.Series(dtype='int'),
            'home_id': pd.Series(dtype='int'),
            'away_id': pd.Series(dtype='int'),
            'created_datetime': pd.Series(dtype='datetime64[ns]'),
            'modifed_datetime': pd.Series(dtype='datetime64[ns]')
            }
        )

        df.to_csv(path, index=False)

def create_results():
    """
    Creates results table
    - Checks if exists, if not then create
    """
    path = Path(dir + 'results.csv')

    if path.is_file():
        print(f'The file {path} exists')
    else:
        print('File does not exist')
        df = pd.DataFrame(
            {
            'fixture_id': pd.Series(dtype='int'),
            'referee': pd.Series(dtype='str'),
            'timestamp': pd.Series(dtype='int'),
            'venue_id': pd.Series(dtype='int'),
            'home_id': pd.Series(dtype='int'),
            'away_id': pd.Series(dtype='int'),
            'winner_home': pd.Series(dtype='bool'),
            'winner_away': pd.Series(dtype='bool'),
            'fulltime_home': pd.Series(dtype='int'),
            'fulltime_away': pd.Series(dtype='int'),
            'halftime_home': pd.Series(dtype='int'),
            'halftime_home': pd.Series(dtype='int'),
            'created_datetime': pd.Series(dtype='datetime64[ns]'),
            'modified_datetime': pd.Series(dtype='datetime64[ns]')
            }
        )

        df.to_csv(path, index=False)


#create_fixtures()
create_results()