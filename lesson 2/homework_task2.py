a = 23
b = 68

answer1 = ((a > 50) and (b > 50)) or ((a < 50) and (b < 50))
answer2 = ((a < 50) and (b > 50)) or ((a > 50) and (b < 50))
print(answer1, answer2)