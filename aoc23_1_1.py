import sys
total = 0
for line in sys.stdin:
    line = str(line.rstrip())
    # print(line)
    first = True
    val1 = -1
    val2 = -1
    for i in range(len(line)):
        if line[i] in list('1234567890'):
            val2 = i
            if first:
                val1 = i
                first = False
    # print(val1, val2)
    total += int(''.join([line[val1], line[val2]]))

print(c_val)
