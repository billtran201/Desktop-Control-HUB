import random
import numpy as np


def create_matrix(row, col):
    matrix  = [[0 for _ in range(col)] for _ in range(row)]
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

    return

def matrix_row_col(matrix):

    row = len(matrix)
    col = len(matrix[0])

    return row, col

def populate_matrix(matrix, min_value, max_value):
    # Get the number of rows and columns in the matrix
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Modify each element of the matrix with a new random number
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = random.randint(min_value, max_value)
    
    return matrix

def trace(matrix):
    # Ensure the matrix is square
    if len(matrix) != len(matrix[0]):
        print("Matrix must be square to calculate its trace")
        return
    
    # Calculate the trace
    trace_sum = 0
    for i in range(len(matrix)):
        trace_sum += matrix[i][i]
    
    return trace_sum

def transpose(matrix):
    # Get the number of rows and columns in the original matrix
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create a new matrix to store the transposed matrix
    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]
    
    # Iterate over the original matrix and fill the transposed matrix
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]
    
    return transposed_matrix

def matrix_addition(matrix1, matrix2):
    # Check if the dimensions of the matrices are the same
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Matrices must have the same dimensions for addition")
        return

    # Initialize a result matrix with the same dimensions as the input matrices
    rows = len(matrix1)
    cols = len(matrix1[0])
    result_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    # Perform element-wise addition
    for i in range(rows):
        for j in range(cols):
            result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]

    return result_matrix

def matrix_subtraction(matrix1, matrix2):
    # Check if the dimensions of the matrices are the same
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Matrices must have the same dimensions for subtraction")
        return
    
    # Initialize a result matrix with the same dimensions as the input matrices
    rows = len(matrix1)
    cols = len(matrix1[0])
    result_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    # Perform element-wise addition
    for i in range(rows):
        for j in range(cols):
            result_matrix[i][j] = matrix1[i][j] - matrix2[i][j]

    return result_matrix

def matrix_multiplication(matrix1, matrix2):
    # Check if the dimensions of the matrices are compatible for multiplication
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Number of columns in matrix1 must be equal to the number of rows in matrix2 for matrix multiplication")

    # Initialize a result matrix with appropriate dimensions
    rows_result = len(matrix1)
    cols_result = len(matrix2[0])
    result_matrix = [[0 for _ in range(cols_result)] for _ in range(rows_result)]

    # Perform matrix multiplication
    for i in range(rows_result):
        for j in range(cols_result):
            for k in range(len(matrix2)):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    return result_matrix

def scalar_multiplication(matrix, scalar):
    # Initialize a result matrix with the same dimensions as the input matrix
    rows = len(matrix)
    cols = len(matrix[0])
    result_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    # Perform scalar multiplication
    for i in range(rows):
        for j in range(cols):
            result_matrix[i][j] = matrix[i][j] * scalar

    return result_matrix

def determinant(matrix):
    # Check if the matrix is square
    if len(matrix) != len(matrix[0]):
        raise ValueError("Matrix must be square to calculate its determinant")
    
    # Base case for 2x2 matrix
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    # Calculate determinant using cofactor expansion along the first row
    for j in range(len(matrix)):
        minor = [row[:j] + row[j+1:] for row in matrix[1:]]
        det += (-1) ** j * matrix[0][j] * determinant(minor)
    
    return det

def cofactor(matrix):
    cofactor_matrix = []
    for i in range(len(matrix)):
        cofactor_row = []
        for j in range(len(matrix)):
            minor = [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]
            cofactor_row.append(((-1) ** (i+j)) * determinant(minor))
        cofactor_matrix.append(cofactor_row)
    return cofactor_matrix

def inverse(matrix):
    det = determinant(matrix)
    if det == 0:
        raise ValueError("Matrix is not invertible")

    # Calculate the adjugate matrix
    cofactor_matrix = cofactor(matrix)
    adjugate_matrix = transpose(cofactor_matrix)

    # Calculate the inverse by dividing the adjugate matrix by the determinant
    inverse_matrix = [[element / det for element in row] for row in adjugate_matrix]
    return inverse_matrix

def eigen(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors

def diagonalize(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    D = np.diag(eigenvalues)
    P = eigenvectors
    return P, D

def matrix_rank(matrix):
    return np.linalg.matrix_rank(matrix)

def row_echelon_form(matrix):
    # Make a copy of the matrix to avoid modifying the original
    matrix = [row[:] for row in matrix]

    num_rows = len(matrix)
    num_cols = len(matrix[0])
    pivot_row = 0

    for col in range(num_cols):
        # Find the pivot row for this column
        while pivot_row < num_rows and matrix[pivot_row][col] == 0:
            pivot_row += 1

        # If a pivot row is found, swap it with the current row
        if pivot_row < num_rows:
            matrix[pivot_row], matrix[col] = matrix[col], matrix[pivot_row]

            # Make the diagonal element 1
            divisor = matrix[col][col]
            matrix[col] = [element / divisor for element in matrix[col]]

            # Make all other elements in the column zero
            for row in range(num_rows):
                if row != col:
                    factor = matrix[row][col]
                    matrix[row] = [x - factor * y for x, y in zip(matrix[row], matrix[col])]

            pivot_row += 1

    return matrix

def reduced_row_echelon_form(matrix):
    # Make a copy of the matrix to avoid modifying the original
    matrix = [row[:] for row in matrix]

    num_rows = len(matrix)
    num_cols = len(matrix[0])
    pivot_row = 0

    for col in range(num_cols):
        # Find the pivot row for this column
        while pivot_row < num_rows and matrix[pivot_row][col] == 0:
            pivot_row += 1

        # If a pivot row is found, perform row operations to make all other entries in the column zero
        if pivot_row < num_rows:
            matrix[pivot_row], matrix[col] = matrix[col], matrix[pivot_row]

            # Make the diagonal element 1
            divisor = matrix[col][col]
            matrix[col] = [element / divisor for element in matrix[col]]

            # Make all other elements in the column zero
            for row in range(num_rows):
                if row != col:
                    factor = matrix[row][col]
                    matrix[row] = [x - factor * y for x, y in zip(matrix[row], matrix[col])]

            pivot_row += 1

    return matrix

def svd_decomposition(matrix):
    # Compute the SVD
    U, S, Vt = np.linalg.svd(matrix)
    return U, S, Vt

def orthogonalize(vectors, normalize=False):
    # Convert the list of vectors into a numpy array
    vectors = np.array(vectors, dtype=np.float64)
    
    # Initialize a list to store the orthogonalized vectors
    orthogonalized = []
    
    for i in range(len(vectors)):
        # Orthogonalize the current vector against the previous vectors
        orthogonalized_vector = vectors[i]
        for j in range(i):
            orthogonalized_vector -= np.dot(vectors[i], orthogonalized[j]) / np.dot(orthogonalized[j], orthogonalized[j]) * orthogonalized[j]
        
        # Normalize the vector if specified
        if normalize:
            orthogonalized_vector /= np.linalg.norm(orthogonalized_vector)
        
        # Append the orthogonalized vector to the result list
        orthogonalized.append(orthogonalized_vector)
    
    return orthogonalized



matrix1 = create_matrix(50,60)

populate_matrix(matrix1, 1, 10)

matrix_dimensions = matrix_row_col(matrix1)
print(f"Row: {matrix_dimensions[0]}, Column: {matrix_dimensions[1]}")

matrix1 = transpose(matrix1)


matrix_dimensions = matrix_row_col(matrix1)
print(f"Row: {matrix_dimensions[0]}, Column: {matrix_dimensions[1]}")

#print(trace(matrix))