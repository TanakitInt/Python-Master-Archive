# printfile2.py prints a file to the screen.

def main():
    fname = input("Enter filename: ")
    infile = open(fname,"r")
    line = infile.readline()
    while not line:        
        print(line)
        line = infile.readline()    
    infile.close()

main()

