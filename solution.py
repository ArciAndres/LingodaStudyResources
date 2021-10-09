# Input:
# solution.solution([13, 5, 6, 2, 5], [5, 2, 5, 13])
# Output:
#     6

# Input:
# solution.solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50])
# Output:
#     -4

def solution(x, y):
    if len(x) > len(y):
        y.append(2000) 
        flag = 0 # list x has the number
    else:
        x.append(2000)
        flag = 1 # list y has the number

    x.sort()
    y.sort()

    for x_, y_ in zip(x, y):
        if x_ != y_:
            if flag == 0:
                if x_ == 2000:
                    return y_
                else:
                    return x_

            if flag == 1:
                if y_ == 2000:
                    return x_
                else:
                    return y_

x, y = [13, 5, 6, 2, 5], [5, 2, 5, 13]
sol = solution(x,y)
print(1, sol)
x, y = [14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50]
sol = solution(x,y)
print(2, sol)
