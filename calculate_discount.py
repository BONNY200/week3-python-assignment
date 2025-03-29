
def calculate_discount(price, discount_percent):
    """Calculates the final price after applying a discount if it's 20% or higher."""
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price

# here is to get user input
try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate and display the final price
    final_price = calculate_discount(price, discount_percent)
    print(f"Final price after discount: {final_price:.2f}")
except ValueError:
    print("Please enter valid numerical values.")

    #It handles invalid input using a try-except block to avoid errors from non-numeric input.
