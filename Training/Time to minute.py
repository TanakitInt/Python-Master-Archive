"""Convert to minute"""
def paragraph():
    """this will compute a string to minute"""
    time = str(input())
    hour = int(time[0:2])
    minute = int(time[4:6])
    print((60*hour)+ minute)
paragraph()
