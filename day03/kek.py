# this open is copypaste from some indian guy
with open("input.txt") as f:
    ls = [x.strip() for x in f.readlines()]

def count_trees(x_add, y_add):
    counter = 0
    x = 0
    y = 0
    line_len = len(ls[0])
    while y < len(ls):
        if ls[y][x % line_len] == "#":
            counter += 1
        x += x_add
        y += y_add

    return counter

print(count_trees(3, 1))

kek = count_trees(1, 1) * count_trees(3, 1) * count_trees(5, 1) * count_trees(7, 1) * count_trees(1, 2)
print(kek)
