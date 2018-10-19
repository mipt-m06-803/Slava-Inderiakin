# Упражнение 14
# Допишите код в следующей клетке так, чтобы после наименьшего элемента списка l вставлялся список l2.

l = [float(substr) for substr in input().split()]
l2 = ['b', 'y', 's', 'h']

minimum = min(l)
position = l.index(minimum)
for i in range (len(l2)):
    l.insert(position + i + 1, l2[i])

print(l)
