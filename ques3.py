# question3 
def print_pascals_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    
    max_digits = len(str(triangle[-1][-1]))

    
    for row in triangle:
        row_str = " ".join(str(num).rjust(max_digits) for num in row)  # join function 
        print(row_str.center(n * max_digits + (n - 1)))  #  using center function of string


print_pascals_triangle(5)
