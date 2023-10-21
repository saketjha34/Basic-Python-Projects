import numpy 
import math
def construct_matrix(m,n): 
    M = []
    for i in range(m):
        row = []
        for j in range(n):
            user_matrix_input = int(input(f"Enter matrix a{i+1}{j+1} : "))
            row.append(user_matrix_input)
        M.append(row)
    return M   

def addition_matrix(A,B):
    C = []
    for i in range(no_row):
        row = []
        for j in range(no_column):
            row.append(A[i][j] + B[i][j])
        C.append(row)
    return C

def subtraction_matrix(A,B):
    C = []
    for i in range(no_row):
        row = []
        for j in range(no_column):
            row.append(A[i][j] - B[i][j])
        C.append(row)
    return C
      
def transpose_matrix(A):
    C = [[0 for i in range(no_row)] for j in range(no_column)]
    for i in range(no_column):
        for j in range(no_row):
            C[i][j] = A[j][i]
    return C        

def multiplication_matrix(A,B):
    C = [[0 for i in range(no_row)] for j in range(no_column)]
    for i in range(no_row):
        for j in range(no_column):
            for k in range(no_column):
                C[i][j] += A[i][k] * B[k][j]
    return C 

def trace_matrix(A):
    trace = 0
    for i in range(no_row):
        for j in range(no_column):
            if i == j :
                trace += A[i][j]
        else:
            continue        
    return trace

def determinant_matrix(A):
    det = round(numpy.linalg.det(A))  
    return det

def inverse_matrix(A):
    inv =  numpy.around(numpy.linalg.inv(A))
    return inv


mainloop = True
no_row = int(input(f"Enter Number Of Rows : "))
no_column = int(input(f"Enter Number Of Column : "))

A = construct_matrix(no_row,no_column)
print("The Matrix A is ")
for i in A:
    print(i)

B = construct_matrix(no_row,no_column)
print("The Matrix B is ")
for i in B:
    print(i)


while mainloop:
    user_prompt = ""
    while user_prompt != "q":
        user_prompt = input(
''' 
Hey User Welcome To This Matrix Applicaton or 'q' to quit or 'replay' to restart
1.Transpose 
2.Multiplication
3.Subtraction
4.Addition 
5.Trace
6.Determinant
7.Inverse
''')
        if user_prompt == "transpose":
            transpose_prompt = input("Hey User Type The Matrix Name(A/B) ").upper()
            if transpose_prompt == "A":
                transpose_A = transpose_matrix(A)
                print("Transpose of Matrix A is")
                for i in transpose_A:
                    print(i)
            elif transpose_prompt == "B":
                transpose_B = transpose_matrix(B)
                print("Transpose of Matrix B is")
                for i in transpose_B:
                    print(i)
            else:
                print("Invalid Input")
        elif user_prompt == "trace":
            trace_prompt = input("Hey User Type The Matrix Name(A/B) ").upper()
            if trace_prompt == "A":
                trace_A = trace_matrix(A)
                print("Tr(A) is = ",trace_A)
                
            elif trace_prompt == "B":
                trace_B = trace_matrix(B)
                print("Tr(B) is = ",trace_B)
            else:
                print("Invalid Input")
        elif user_prompt == "determinant":
            determinant_prompt = input("Hey User Type The Matrix Name(A/B) ").upper()
            if determinant_prompt == "A":
                determinant_A = determinant_matrix(A)
                print("det(A) is = ",determinant_A)
                
            elif determinant_prompt == "B":
                determinant_B = determinant_matrix(B)
                print("det(B) is = ",determinant_B)
            else:
                print("Invalid Input")                                  
        elif user_prompt == "inverse":
            inverse_prompt = input("Hey User Type The Matrix Name(A/B) ").upper()
            if inverse_prompt == "A":
                inverse_A = inverse_matrix(A)
                print("inv(A) is = ",inverse_A)
                
            elif inverse_prompt == "B":
                inverse_B = inverse_matrix(B)
                print("inv(B) is = ",inverse_B)
            else:
                print("Invalid Input")                                  
        elif user_prompt == "addition":
            addition = addition_matrix(A,B)
            print("A + B = ")
            for i in addition:
                print(i)
        elif user_prompt == "multiplication":
            multiplication = multiplication_matrix(A,B)
            print("A X B = ")
            for i in multiplication:
                print(i) 
        elif user_prompt == "subtraction":
            multiplication = subtraction_matrix(A,B)
            print("A - B = ")
            for i in multiplication:
                print(i)
        
        elif user_prompt== "replay":
            no_row = int(input(f"Enter Number Of Rows : "))
            no_column = int(input(f"Enter Number Of Column : "))
            A = construct_matrix(no_row,no_column)
            print("The Matrix A is ")
            for i in A:
                print(i)

            B = construct_matrix(no_row,no_column)
            print("The Matrix B is ")
            for i in B:
                print(i)

        else:
            mainloop = False
            print("Thanks!")















