import argparse

def main(): 
    #creating the parser
    parser = argparse.ArgumentParser(description="Command line arguments")

    #add input arguments
    parser.add_argument("--number1", required=True, type=int, help="number 1")
    parser.add_argument("--number2", required=True, type=int, help="number 2")
    args = parser.parse_args()

    #print command line inputs 
    print(f"Number 1: {args.number1}")
    print(f"Number 2: {args.number2}")

    a = args.number1
    b = args.number2

    total = a+b
    print(f"Total:{total}")

if __name__ == '__main__':
        main()