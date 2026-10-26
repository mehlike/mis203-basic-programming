def calculate_subtototal(unit_price, quantity):
    return unit_price * quantity
def calculate_discount_rate(subtotal):
    if subtotal >= 100.0:
        return 0.10
    return 0.0
def calculate_shipping_fee(subtotal):
    if subtotal >= 150.0:
        return 0.0
    return 20.0
def calculate_final_total(subtotal, discount_rate, shipping_fee):
    discount_amount = subtotal * discount_rate
    return (subtotal - discount_amount) + shipping_fee

sub1 = calculate_subtototal(300.0, 4)
disc1 = calculate_discount_rate(sub1)
ship1 = calculate_shipping_fee(sub1)
total1 = calculate_final_total(sub1, disc1, ship1)
print("order 1 total: ", total1)

sub2 = calculate_subtototal(50.0, 2)
disc2 = calculate_discount_rate(sub2)
ship2 = calculate_shipping_fee(sub2)
total2 = calculate_final_total(sub2, disc2, ship2)
print("order 2 total:", total2)

# Print is showing the answer on the screen for humans to see, while return is handing the final result back to the code so it can keep using it. 
