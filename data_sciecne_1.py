### #1 - Calculate the BMI (body mass index) on the two lists below using NDArrays...

import numpy as np
# formula = weight / (height**2) * 730
import numpy as np

height = np.array([69, 70, 71, 72, 73, 74, 75]) / 39.37  # Convert height from inches to meters
weight = np.array([110, 120, 130, 140, 150, 160, 170])  # Weight in pounds

# Calculate BMI
bmi = weight / (height ** 2)

print(bmi)



def create_random_matrix(rows, cols, shape='2D', dtype=float):
    """
    Create a random matrix based on the parameters provided.

    Parameters:
    rows (int): Number of rows in the matrix.
    cols (int): Number of columns in the matrix.
    shape (str): Shape of the matrix. Options: '1D', '2D'. Default is '2D'.
    dtype (type): Data type of the matrix elements. Default is float.

    Returns:
    numpy.ndarray: Random matrix with specified shape and data type.
    """
    if shape == '2D':
        return np.random.random((rows, cols)).astype(dtype)
    elif shape == '1D':
        return np.random.random(rows).astype(dtype)
    else:
        raise ValueError("Invalid shape. Please choose '1D' or '2D'.")

# Example usage:
# Create a 3x3 random matrix with default data type (float)
matrix_2d = create_random_matrix(3, 3)
print("2D Matrix:")
print(matrix_2d)

# Create a 1D random matrix with 5 elements and integer data type
matrix_1d = create_random_matrix(5, shape='1D', dtype=int)
print("\n1D Matrix:")
print(matrix_1d)

import numpy as np

def load_data(filename, dtypes):
    """
    Load data from a text file into a NumPy array.

    Parameters:
    filename (str): Name of the text file to load.
    dtypes (list of tuples): Data types for each field in the text file.

    Returns:
    numpy.ndarray: NumPy array containing the loaded data.
    """
    data = np.genfromtxt(filename, delimiter=',', skip_header=1, dtype=dtypes, encoding=None)
    return data

# Define data types for the fields
DATATYPES = [('rk', 'i'), ('pos', '|S25'), ('name', '|S25'), ('age', 'i'), ('g', 'i'), ('pa', 'i'), ('ab', 'i'),
             ('r', 'i'), ('h', 'i'), ('2b', 'i'), ('3b', 'i'), ('hr', 'i'), ('rbi', 'i'), ('sb', 'i'), ('cs', 'i'),
             ('bb', 'i'), ('so', 'i'), ('ba', 'f'), ('obp', 'f'), ('slg', 'f'), ('ops', 'f'), ('opsp', 'i'),
             ('tb', 'i'), ('gdp', 'i'), ('hbp', 'i'), ('sh', 'i'), ('sf', 'i'), ('ibb', 'i')]

# Load data for 2017 and 2018
data_2017 = load_data('redsox_2017_hitting.txt', DATATYPES)
data_2018 = load_data('redsox_2018_hitting.txt', DATATYPES)

# Calculate average SLG for each year
avg_slg_2017 = np.mean(data_2017['slg'])
avg_slg_2018 = np.mean(data_2018['slg'])

# Determine which year had a higher SLG
if avg_slg_2017 > avg_slg_2018:
    print("2017 was a better year based on SLG.")
elif avg_slg_2018 > avg_slg_2017:
    print("2018 was a better year based on SLG.")
else:
    print("Both years had the same SLG.")
