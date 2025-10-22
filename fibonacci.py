# Function 1: get a valid positive integer from the user
def get_terms():
    while True:
        user_input = input("Enter the number of terms: ")
        if user_input.isdigit():
            num = int(user_input)
            if num > 0:
                return num
        print("Please enter a positive integer.")

# Function 2: generate (and print) Fibonacci numbers using a for loop
def fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        print(a)
        temp = a + b
        a = b
        b = temp

# Function 3: print the sequence (drives the program)
def main():
    terms = get_terms()
    print("Fibonacci sequence:")
    fibonacci(terms)

# Run the program
main()

