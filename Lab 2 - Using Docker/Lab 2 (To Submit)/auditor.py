# stock value inputs must be integers
# print value of failed_attemps and valid_attempts when user enters 'quit' to quit
# reject negative numbers and values > 500


inventory = 0
failed_attempts = 0

while True:
    delivery_input = input("Enter the number of items delivered (type 'quit' to quit): ")
    if delivery_input == 'quit':
        print("Exiting the program.")
        print(f"Failed attempts: {failed_attempts}")
        print(f"Total Units Processed: {inventory}")
        break

    try:
        # print(f"Current inventory before last input: {inventory}")
        delivery_value = int(delivery_input)
        if delivery_value < 0: # check if input is within valid range
            print("Please try again. Stock quantity must be between 0 and 500.")
            failed_attempts += 1
        elif (delivery_value + inventory > 500) and inventory > 0: # when 0 < inventory < 500 and the user input + inventory > 500
            inventory = 500
            print(f"ALERT: Maximum Storage Limit of 500 reached. Cannot add anymore stock! (Current inventory: {inventory})")
            failed_attempts += 1
            print("Exiting the program.")
            print(f"Failed attempts: {failed_attempts}")
            print(f"Total Units Processed: {inventory}")
            break
        elif delivery_value > 500 and inventory == 0: # when inventory = 0 and the first user input > 500
            inventory = 500
            print(f"ALERT: Maximum Storage Limit of 500 reached. Cannot add anymore stock! (Current inventory: {inventory})")
            failed_attempts += 1
            print("Exiting the program.")
            print(f"Failed attempts: {failed_attempts}")
            print(f"Total Units Processed: {inventory}")
            break
        else:
            inventory += delivery_value
            # print(f"Current inventory after last input: {inventory}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        failed_attempts += 1