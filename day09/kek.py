with open("input.txt") as f:
    numbers = [x.strip() for x in f.readlines()]
    numbers = [int(x) for x in numbers]


def find_weakness():
    for x in range(25, len(numbers)):
        if not check_num(x - 25, x):
            return numbers[x]

def check_num(start, index): 
    for i in range(start, index):
        for j in range(start + 1, index - 1):
            if numbers[i] + numbers[j] == numbers[index]:
                return True

    return False

invalid_number = find_weakness()
print(invalid_number)


# it is slow but gets the job done
def encrypt_weakness(invalid_number):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            candidates = numbers[i:j]
            if sum(candidates) == invalid_number:
                candidates.sort()
                return candidates[0] + candidates[-1]
    

print(encrypt_weakness(invalid_number))
