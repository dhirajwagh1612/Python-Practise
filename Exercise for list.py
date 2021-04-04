def square_matrix_power(A, n):
    output=[item[:] for item in A]
    temp=[item[:] for item in A]
    for i in range(n-1):
        #output=output*A
        # -> output = A * temp
        # temp = output
        output[0][0] = A[0][0]* temp[0][0]+A[0][1] * temp[1][0]
        output[0][1] = A[0][0]* temp[0][1]+A[0][1] * temp[1][1]
        output[1][0] = A[1][0]* temp[0][0]+A[1][1] * temp[1][0]
        output[1][1] = A[1][0]* temp[0][1]+A[1][1] * temp[1][1]
        temp = [item[:] for item in output]
    return output

A=[
    [1,1],
    [1,0]
]


print(square_matrix_power(A, 2))