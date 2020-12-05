import sys

def main():
    expenses = []
    with open("input.txt", "r") as input_file:
        for line in input_file:
            expenses.append(int(line.strip()))
        
    for a in expenses:
        for b in expenses:
            if a + b == 2020:
                print(a * b)

    for a in expenses:
        for b in expenses:
            for c in expenses:
                if a + b + c == 2020:
                    print(a * b * c)


if __name__ == "__main__":
    main()
