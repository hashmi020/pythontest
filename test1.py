# Step 1: Define a function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result  # Step 2: Return the calculated factorial

# Step 3: Call the function with a sample number
sample_number = 5
print(f"The factorial of {sample_number} is:", factorial(sample_number))
