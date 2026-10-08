
def calculate_next_payment(monthly_interest, remaining_loan, remaining_payments):
    if monthly_interest <= 0:
        raise ValueError("Monthly interest must be greater than 0.")

    if remaining_loan <= 0:
        raise ValueError("Remaining loan amount must be greater than 0.")

    if remaining_payments <= 0:
        raise ValueError("Number of remaining payments must be greater than 0.")

    payment = (
        remaining_loan * monthly_interest
        / (1 - (1 + monthly_interest) ** -remaining_payments)
    )

    return (payment/100)  # Convert from cents to euros

my_loan_amount = 7800000 # senttiä
my_monthly_interest = 0.05 # 5%
my_remaining_payments = 6

payment = calculate_next_payment(my_monthly_interest, my_loan_amount, my_remaining_payments)

print(f"The next payment is {payment:.2f} euros")
