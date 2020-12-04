import sys

def main():
    passwords = []
    input_file = open("input.txt", "r")
    for line in input_file:
        passwords.append(line.strip())
        
    input_file.close()

    valid_counter = 0

    for item in passwords:
        values = item.split()
        min_max = values[0].split("-")
        letter = values[1].split(":")[0]
        password = values[2]
        letter_count = password.count(letter)
        valid_counter += (letter_count >= int(min_max[0]) and letter_count <= int(min_max[1]))

    print(valid_counter)


    valid_counter = 0

    for item in passwords:
        values = item.split()
        positions = values[0].split("-")
        letter = values[1].split(":")[0]
        password = values[2]

        valid_counter += (
            (password[int(positions[0]) - 1] == letter and password[int(positions[1]) - 1] != letter) or
            (password[int(positions[0]) - 1] != letter and password[int(positions[1]) - 1] == letter)
        )

    print(valid_counter)     


if __name__ == "__main__":
    main()
