while True:
    try:
        size = int(input("Enter the size of the pattern: "))
        if size > 0:
            row = 0

    # Use a while loop to iterate through rows
            while row < size:
                # Use a for loop to print asterisks for the current row
                for x in range(size):
                    print("*", end="")
                # Move to the next line after completing the row
                print()
                row += 1
            break   
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

    # Initialize row counter
