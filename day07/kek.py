import re

# todays assignment was giga interesting because I found out about some pretty interesting stuff
# just look at these for loops (also took me foken long)
# https://docs.python.org/3/howto/functional.html

with open("input.txt") as f:
    rules = {
        # https://www.guru99.com/python-regular-expressions-complete-tutorial.html#2
        re.match(r"^\w+ \w+", line).group(0): re.findall(r"(\d+) (\w+ \w+)", line) for line in f
    }
    

def can_contain_shiny_gold(color):
    if "shiny gold" == color:
        return True
    return any(can_contain_shiny_gold(color) for _, color in rules[color])


def gold_bag_capacity(color):
    # if bag doesn't contain more bags, return 0
    if not rules[color]:
        return 0
    return sum(int(count) + int(count) * gold_bag_capacity(sub_color) for count, sub_color in rules[color])


print(sum(can_contain_shiny_gold(color) for color in rules.keys() if color != "shiny gold"))
print(gold_bag_capacity("shiny gold"))
