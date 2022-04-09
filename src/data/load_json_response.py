import json
import pandas as pd
import sys


file_name = sys.argv[1]
path_name = sys.argv[2]
def json_to_df(source,dest):
    """
    Reads some source json file and outputs csv to destination

    Parameters
    ----------
    source : str
        Source path to input file
    dest : str
        Destination path to output file
    """
    # load data using Python JSON module
    with open(source,'r') as f:
        data = json.loads(f.read())
    # Flatten data
    df = pd.json_normalize(data, record_path =['response'])
    df.to_csv(dest, index=False, header=True)

json_to_df(file_name,path_name)