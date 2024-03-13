# Pseudo code for the arithmetic practice program

# Initialize the lists of numbers
numA = [4, 1, 6, 10, 2, 3, 7, 9, 11, 12, 5, 8]
numB = [2, 12, 10, 11, 1, 3, 7, 9, 4, 8, 5, 6]

# Function to perform addition
def add_numbers(a, b):
    return a + b

# Function to perform multiplication
def multiply_numbers(a, b):
    return a * b

# Main function
def main():
    print("Welcome to the Arithmetic Practice Program!")
    print("Choose an operation:")
    print("1. Addition")
    print("2. Multiplication")
    
    # Get user input for the chosen operation
    operation = input("Enter 1 for addition or 2 for multiplication: ")
    
    # Error handling: Validate user input
    try:
        operation = int(operation)
        if operation not in [1, 2]:
            print("Invalid choice. Please enter 1 or 2.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    
    # Initialize a counter for correct answers
    correct_answers = 0
    
    # Loop through the lists and ask questions
    for i in range(len(numA)):
        if operation == 1:
            # Addition
            answer = add_numbers(numA[i], numB[i])
        else:
            # Multiplication
            answer = multiply_numbers(numA[i], numB[i])
        
        # Get user input for the answer
        user_answer = input(f"What is {numA[i]} {'+' if operation == 1 else 'x'} {numB[i]}? ")
        
        # Error handling: Validate user input
        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        # Check if the answer is correct
        if user_answer == answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Wrong. The correct answer is {answer}.")
    
    # Display the total score
    print(f"You answered {correct_answers} out of 12 questions correctly.")

# Call the main function
if __name__ == "__main__":
    main()
