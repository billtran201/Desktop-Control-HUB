import numpy as np

# Basis for R3 (standard x, y, z axes)
basis = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])  

# An arbitrary vector in R3
vector = np.array([3, -2, 5])

# Finding coefficients for the linear combination
coefficients = np.linalg.solve(basis, vector)  
print(coefficients)  # Output: [3 -2 5]  

# Verification:
resultant_vector = coefficients[0] * basis[0] + coefficients[1] * basis[1] + coefficients[2] * basis[2] 
print(resultant_vector)  # Output: [3 -2 5] (same as original vector)
