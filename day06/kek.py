# load whole groups
with open("input.txt") as f:
    ls = f.read().split('\n\n')

#print(ls)

def question_count():
    counter = 0
    for l in ls:
        counter += len(set(l.replace('\n', '')))
    return counter
     

def question_count2():
    counter = 0
    for l in ls:
        ppl = [set(ppl) for ppl in l.split()]
        #print(ppl)
    
        counter += len(ppl[0].intersection(*ppl[1:]))
    return counter


print(question_count())
print(question_count2())
