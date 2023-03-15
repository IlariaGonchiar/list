A = list(range(1, 10))
B = A
B[3] = 100
C = list(A)
C[3] =  777
print("B = ", A)
print("A = ", B)
print("C = ", C)
