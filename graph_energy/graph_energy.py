import keras
import pickle
import configparser
import sys
import pandas as pd


class GraphEnergy(object):
    '''
    The GraphEnergy object contains all of the program functionality
    The following methods contain the modules available to the user.

    parse_input():
        Input: A ConfigFile in the following format:

            --------------------------
            [Data]
            path = path/to/data.dat

            [Meta]
            param = some_value
            --------------------------

        Output:
            -- pandas DataFrame of data.dat file
            -- meta parameter dictionary

    '''

    def __init__(self):
        pass

    def parse_input(self, inputfile):

        # Create configParser object and read in .inp
        config = configparser.ConfigParser()
        config.read(inputfile)

        # Read input file variables
        path = config.get('Data', 'path')
        temp = config.getint('Meta', 'temp')
        meta_params = {'Temp': temp}

        # Read .dat file into Pandas DataFrame
        data = pd.read_csv(path, delim_whitespace=True)

        return data, meta_params


if __name__ == '__main__':

    inputfile = sys.argv[1]

    GE = GraphEnergy()
    GE.parse_input(inputfile)
