import re

with open("input.txt") as f:
    ls = [x.strip() for x in f.readlines()]

keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def check_keys(data):
    counter = 0
    cur = 0
    for line in data:
        if line == "":                           
            counter += (cur == len(keys))
            cur = 0
            continue

        for field in line.split():
            key, val = field.split(":")
            cur += (key in keys)

    return counter

def valid(passport):
    for f in keys:
        if f not in passport:
            return False

    if not 1920 <= int(passport["byr"]) <= 2002:
        return False
    if not 2010 <= int(passport["iyr"]) <= 2020:
        return False
    if not 2020 <= int(passport["eyr"]) <= 2030:
        return False

    if "cm" in passport["hgt"] and not (150 <= int(passport["hgt"][:-2]) <= 193):
            return False
    elif "in" in passport["hgt"] and not (59 <= int(passport["hgt"][:-2]) <= 76):
            return False
    if "cm" not in passport["hgt"] and "in" not in passport["hgt"]:
        return False

    if  passport["ecl"] not in ["amb", "blu", "brn","gry","grn","hzl","oth"]:
        return False
    if re.match(r"^\#[0-9a-f]{6}$", passport["hcl"]) is None:
        return False
    if re.match(r"^\d{9}$", passport["pid"]) is None:
        return False

    return True

def check_values(data):
    counter = 0
    cur = {}
    for line in data:
        if line == "":
            counter += (valid(cur))
            cur = {}
            continue

        for field in line.split():
            field, val = field.split(":")
            cur[field] = val
    return counter


print(check_keys(ls))
print(check_values(ls))
