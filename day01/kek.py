import sys

def main():
    expenses = []
    input_file = open("input.txt", "r")
    for line in input_file:
        expenses.append(int(line.strip()))
        
    input_file.close()

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
