#Q.1 Write a Python program to print the Fibonacci series.


# Function to print Fibonacci series up to n terms
def fibonacci_series(n):
    a, b = 0, 1
    print("Fibonacci series:", end=" ")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Input number of terms
n_terms = int(input("Enter the number of terms: "))
fibonacci_series(n_terms)


Output:
Enter the number of terms: 10
Fibonacci series: 0 1 1 2 3 5 8 13 21 34
