with open("input.txt") as f:
    ls = [x.strip() for x in f.readlines()]


print(ls)

flight_ids = []

# B amd L are 1s, F and R are 0s
# B  F  F  B  F  F   R L L
# 1  0  0  1  0  1   1 0 0
# 32 16 8  4  2  1   4 2 1

for code in ls:
    row = int(code[:7].replace("F", "0").replace("B", "1"), 2)
    col = int(code[7:].replace("L", "0").replace("R", "1"), 2)

    flight_ids.append(row * 8 + col)

print(max(flight_ids))

flight_ids.sort()
for i in range(len(flight_ids) - 1):
    if not flight_ids[i] + 1 == flight_ids[i + 1]:
        print (flight_ids[i] + 1)



