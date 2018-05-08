# Function/method spec for data to microstate functionality:

## Preconditions:
 1. Data and input files have been parsed. `self.data` contains a dataframe with the specs below.
 2. `self.train` is set as a boolean

## Postconditions:
 1. `self.microstates` contains a dataframe with specs below.
 2. If `self.train`: `self.energies` contains a series with the corresponding average energies

## Inputs:
 1. (Optional) A list of topological parameters on which to base the microstates.
 Default = `None`: if `None`, then use all available microstates
 2. (Optional) A dictionary of bin sizes for the continuous topological parameters. 
 Default = `None`: if `None`, use a default defined within the function.

## Outputs:
None.

## Dataframe specifications:
Minor examples of the dataframes are given below the specs.
 * `self.data`: A `pandas.DataFrame` object.
 The rows of the dataframe correspond to the subgraphs read in from the data files.
 The columns of the dataframe correspond to topological parameters and temperature.
 The columns may (and likely will) have replicated values across columns
 (e.g. for the first order edge distribution, many subgraphs will have the same value).
 It is also possible for rows to be identical for all topological parameters and temperature.
 * `self.microstates`: A `pandas.DataFrame` object.
 The rows of the dataframe correspond to unique microstates.
 The columns of the dataframe correspond to the topological parameters, temperature, and population.
 Each row should be unique - that is to say no row can be the duplicate of another.
 For the continuous topological parameters,
 the entries in the dataframe should be the start (inclusive) and end of the value bin.
 * `self.energy`: A `pandas.Series` object which contains the average energy of the subgraphs within each microstate
 (with corresponding indices between `energy` and `microstates`) 


A `data` dataframe might look like:

 | Index | ed1 | ed2 | ed3 | pr2 | pr3 | cy3 | cy4 | gd3 | en | Temp |
 |-------|-----|-----|-----|-----|-----|-----|-----|-----|----|------|
 |   0   |  3  |  5  |  5  | 2.3 | 3.6 | 3.1 | 0.4 | 5.6 | 30 |  70  |
 |   1   |  2  |  4  |  6  | 3.3 | 6.3 | 3.2 | 5.6 | 4.2 | 42 |  80  |
 |   2   |  3  |  5  |  5  | 2.2 | 3.3 | 3.3 | 0.8 | 5.1 |32.6|  70  |
 |   3   |  1  |  5  |  2  | 2.1 | 4.0 | 3.1 | 1.2 | 9.7 | 12 |  70  |

The `microstate` dataframe generated from that might look like:
 | Index | ed1 | ed2 | ed3 | pr2s | pr2e | pr3s | pr3e | cy3s | cy3e | cy4s | cy4e | gd3s | gd3e | Temp | Pop |
 |-------|-----|-----|-----|------|------|------|------|------|------|------|------|------|------|------|-----|
 |   0   |  3  |  5  |  5  |  2.0 |  2.5 |  3.3 |  3.8 |  3.1 |  3.3 |  0.0 |  1.0 |  4.0 |  6.0 |  70  |  2  |
 |   1   |  2  |  4  |  6  |  3.0 |  3.5 |  6.3 |  6.8 |  3.1 |  3.3 |  5.0 |  6.0 |  4.0 |  6.0 |  80  |  1  |
 |   2   |  1  |  5  |  2  |  2.0 |  2.5 |  3.8 |  4.3 |  3.1 |  3.3 |  1.0 |  2.0 |  8.0 | 10.0 |  70  |  1  |
which has the `energy` as:
 | Index | en |
 |-------|----|
 |   0   |31.3|
 |   1   | 42 |
 |   2   | 12 |

## Errors
 * `self.train` is `True`, but there is no `'en'` column in the `data` dataframe
 * Input 1 (list of parameters) has a string that doesn't exist within the `data` dataframe columns
 * Input 2 (dict of bin sizes) has a key that doesn't exist within the `data` dataframe columns
