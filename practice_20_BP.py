def calc_color(x, y):
    calc_brown = 2 * (x + y - 2)
    calc_yellow = (x - 2) * (y - 2)
    return (calc_brown, calc_yellow)

def solution(brown, yellow):
    x = 3
    y = 3

    while brown >= 8 and brown <= 5000 and yellow >= 1 and yellow <= 2000000:
        temp_x = x
        temp_y = y
        while temp_y >= temp_x:
            calc_brown, calc_yellow = calc_color(temp_x, temp_y)
            if brown == calc_brown and yellow == calc_yellow:
                return [temp_y, temp_x]
            else:
                temp_x += 1
        y += 1
    return []

print(solution(24, 24))
            