"""Pizza"""
def main():
    """Pizzzzzzzzzzzzaaaaaa"""
    pcs = int(input())
    box_l = 0
    box_m = 0
    box_s = 0
    box_l = (pcs//12)
    pcs %= 9
    box_m = (pcs//9)
    pcs %= 6
    box_s = (pcs//6)
    if pcs <= 6 and pcs != 0:
        print((box_l), "/", (box_m), "/", (box_s))
    else:
        print((box_l), "/", (box_m), "/", (box_s))
main()
