"""Max speed"""
def traffic():
    """go drive!"""
    speed_limit = int(input())
    current_speed = int(input())
    fine = 0
    #when drive illegal but not more than 90
    if current_speed > speed_limit and current_speed <= 90:
        fine = 50 + abs((speed_limit-current_speed)*5)
        print("The speed is illegal, your fine is $"+'%.2f'%fine)
    #when drive illegal and more than 90
    elif current_speed > speed_limit and current_speed > 90:
        fine = 50 + abs((speed_limit-current_speed)*5) + 200
        print("The speed is illegal, your fine is $"+'%.2f'%fine)
    #when drive legal
    else:
        print("Your speed is legal.")
traffic()
