values = []
for i in range(1, 4):
    a = int(input("Enter value :"))
    values.append(a)

def cal_avg(a, b, c):
    avg = (a+b+c)/3
    return avg

result = cal_avg(values[0], values[1], values[2])
print(result)