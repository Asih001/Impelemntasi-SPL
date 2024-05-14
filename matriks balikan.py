def minor(matrix, row, col):
    """
    Mengembalikan minor dari sebuah matriks setelah menghapus baris dan kolom tertentu.
    """
    return [r[:col] + r[col + 1:] for r in (matrix[:row] + matrix[row + 1:])]

def determinant(matrix):
    """
    Menghitung determinan dari sebuah matriks persegi secara rekursif.
    """
    # Basis: determinan dari matriks 1x1 adalah nilai tunggalnya
    if len(matrix) == 1:
        return matrix[0][0]
    
    # Basis: determinan dari matriks 2x2
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    # Rekursi: hitung determinan menggunakan ekspansi kofaktor
    det = 0
    for c in range(len(matrix)):
        det += ((-1) ** c) * matrix[0][c] * determinant(minor(matrix, 0, c))
    return det

def transpose(matrix):
    """
    Menghitung transpose dari sebuah matriks.
    """
    return list(map(list, zip(*matrix)))

def cofactor(matrix):
    """
    Menghitung matriks kofaktor dari sebuah matriks persegi.
    """
    cofactors = []
    for r in range(len(matrix)):
        cofactorRow = []
        for c in range(len(matrix)):
            minor_matrix = minor(matrix, r, c)
            cofactorRow.append(((-1) ** (r + c)) * determinant(minor_matrix))
        cofactors.append(cofactorRow)
    return cofactors

def inverse(matrix):
    """
    Menghitung invers dari sebuah matriks persegi.
    """
    det = determinant(matrix)
    if det == 0:
        raise ValueError("Matriks tidak memiliki invers karena determinannya 0.")
    
    # Transpose dari matriks kofaktor
    cofactors = cofactor(matrix)
    cofactors = transpose(cofactors)
    
    # Bagi setiap elemen dengan determinan
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / det
    
    return cofactors

def multiply_matrix_vector(matrix, vector):
    """
    Mengalikan matriks dengan vektor.
    """
    result = []
    for row in matrix:
        result.append(sum(row[i] * vector[i] for i in range(len(vector))))
    return result

def solve_linear_system(A, b):
    """
    Menggunakan metode matriks balikan untuk menyelesaikan sistem persamaan linear Ax = b.
    """
    A_inv = inverse(A)
    x = multiply_matrix_vector(A_inv, b)
    return x

# Fungsi untuk melakukan pengujian
def test_solve_linear_system():
    # Kasus uji 1
    A1 = [[2, 3], [1, 2]]
    b1 = [8, 5]
    x1 = solve_linear_system(A1, b1)
    print("Solusi untuk kasus uji 1:", x1)
    
    # Kasus uji 2
    A2 = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]
    b2 = [6, 4, 3]
    x2 = solve_linear_system(A2, b2)
    print("Solusi untuk kasus uji 2:", x2)
    
    # Kasus uji 3
    A3 = [[4, 7], [2, 6]]
    b3 = [10, 8]
    x3 = solve_linear_system(A3, b3)
    print("Solusi untuk kasus uji 3:", x3)

# Jalankan fungsi pengujian
test_solve_linear_system()
