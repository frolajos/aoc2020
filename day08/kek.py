import copy

with open("input.txt") as f:
    ls = [x.split() for x in f.readlines()]

# solution 1
# found out that you can use lists for accumulation values in recursion
accumulator = [0]

def proccess_cmds(cmds, index, order):
    if len(cmds[index]) == 3:
        return accumulator[0]
    cmds[index].append(order)

    cmd = cmds[index][0]
    val = int(cmds[index][1])
    if cmd == "nop":
        return proccess_cmds(cmds, index + 1, order + 1)
    if cmd == "acc":
        accumulator[0] += val
        return proccess_cmds(cmds, index + 1, order + 1)
    if cmd == "jmp":
        return proccess_cmds(cmds, index + val, order + 1)


print(proccess_cmds(copy.deepcopy(ls), 0, 0))


# solution 2
# got fucked hard by shallow copy
accumulator = [0]

def proccess_cmds2(cmds, index, order):
    if index == len(ls):
        return accumulator[0]
    if len(cmds[index]) == 3:
        return None   
    cmds[index].append(order)
    cmd, val = cmds[index][0], int(cmds[index][1])
    if cmd == "nop":
        return proccess_cmds2(cmds, index + 1, order + 1)
    if cmd == "acc":
        accumulator[0] += val
        return proccess_cmds2(cmds, index + 1, order + 1)
    if cmd == "jmp":
        return proccess_cmds2(cmds, index + val, order + 1)


for i in range(len(ls)):
    accumulator = [0]
    cmds = copy.deepcopy(ls)
    if cmds[i][0] == "jmp":
        prog[i][0] = "nop"
    elif cmds[i][0] == "nop":
        prog[i][0] = "jmp"
    acc = proccess_cmds2(cmds, 0, 0)
    if acc:
        print(acc)
