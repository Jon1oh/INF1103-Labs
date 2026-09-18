def get_valid_input():
    while True:
        delivery_input = input("Enter the number of items delivered (type 'quit' to quit): ")
        if delivery_input.lower() == "quit":
            return "quit"
        try:
            delivery_value = int(delivery_input)
            if delivery_value < 0:
                print("Please try again. Stock quantity must be 0 or greater.")
                continue
            return delivery_value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return amount * 0.1

def generate_report(total_deliveries, failed_attempts):
    print("\nExiting the program.")
    print(f"Total Deliveries Processed: {total_deliveries}")
    print(f"Failed/Rejected Entries: {failed_attempts}")


inventory = 0
failed_attempts = 0
deliveries_processed = 0

while True:
    value = get_valid_input()
    if value == "quit":
        generate_report(deliveries_processed, failed_attempts)
        break
    inventory = process_delivery(inventory, value)
    tax = calculate_tax(value)
    deliveries_processed += 1

    print(f"Current inventory: {inventory}")
    print(f"Tax for this delivery: {tax:.2f}")

    if inventory > 500:
        inventory = 500
        print(
            f"ALERT: Maximum Storage Limit of 500 reached. "
            f"(Current inventory: {inventory})"
            )
        break

generate_report(deliveries_processed, failed_attempts)

