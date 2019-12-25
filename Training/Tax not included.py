"""Tax not included"""
def tax():
    """start compute tax"""
    subtotal = int(input())
    tax_rate = float(input())
    compute_tax = int(subtotal*tax_rate)
    print("Subtotal:", subtotal)
    print(("Tax (",tax_rate*100, "%):", compute_tax))
    print("Total:", subtotal+compute_tax)
tax()
