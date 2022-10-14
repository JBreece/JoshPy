from math import sqrt

players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]

sum = 0
sqrdistance = 0
sum2 = 0
standard_deviation = 0

for player in players:
    sum = sum + player
mean = sum / len(players)
# print(mean)
for player in players:
    sqrdistance = (mean - player) * (mean - player)
    sum2 = sum2 + sqrdistance
standard_deviation = sum2 / len(players)
standard_deviation = sqrt(standard_deviation)
# print(standard_deviation)

final_output = 0

for player in players:
    if ( abs(player - mean) <= standard_deviation ):
        # print(player)
        final_output = final_output + 1

print(final_output)