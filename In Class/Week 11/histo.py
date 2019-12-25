"""60070141, 60070156"""
def main():
    """ScoreHistogram"""
    score = input()
    score = score.split(",")
    count = 0
    while count != 10:
        print("{0}-{1}:".format(count, count+1), end="")
        linecount = 0
        if count == 0:
            for i in score:
                if count <= float(i) <= count+1:
                    linecount += 1
        else:
            for i in score:
                if count < float(i) <= count+1:
                    linecount += 1
        print("|" * linecount)
        count += 1
main()
