def crout_decomposition(A):
    """
    Melakukan dekomposisi Crout pada matriks A.
    Mengembalikan lower triangular matrix L dan unit upper triangular matrix U.
    """
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]
    
    for j in range(n):
        U[j][j] = 1  # Diagonal dari U diisi dengan 1
        
        for i in range(j, n):
            sum_l = sum(L[i][k] * U[k][j] for k in range(j))
            L[i][j] = A[i][j] - sum_l
        
        for i in range(j+1, n):
            sum_u = sum(L[j][k] * U[k][i] for k in range(j))
            U[j][i] = (A[j][i] - sum_u) / L[j][j]
    
    return L, U

def forward_substitution(L, b):
    """
    Menyelesaikan Ly = b dengan substitusi maju.
    """
    n = len(L)
    y = [0.0] * n
    for i in range(n):
        sum_ly = sum(L[i][j] * y[j] for j in range(i))
        y[i] = (b[i] - sum_ly) / L[i][i]
    return y

def backward_substitution(U, y):
    """
    Menyelesaikan Ux = y dengan substitusi mundur.
    """
    n = len(U)
    x = [0.0] * n
    for i in range(n-1, -1, -1):
        sum_ux = sum(U[i][j] * x[j] for j in range(i+1, n))
        x[i] = y[i] - sum_ux
    return x

def solve_linear_system(A, b):
    """
    Menggunakan dekomposisi Crout untuk menyelesaikan sistem persamaan linear Ax = b.
    """
    L, U = crout_decomposition(A)
    y = forward_substitution(L, b)
    x = backward_substitution(U, y)
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
