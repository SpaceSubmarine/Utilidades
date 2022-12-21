import numpy as np

amont_px = 227000000 - 300000 - 300000
average = 0.000008764
avg_pr = amont_px * average
ATH = 0.000075
inject = 1000
fall_factor = 0.15
total_fall = fall_factor * average
n_div = 20
div = (average - total_fall) / n_div
buys = []
for i in range(1, 20):
    buys.append((inject / n_div) / (average - div * i))

act = 3000
normal_in = 1500
normal_out = 650
non_normal_out = 200
total_weight = normal_in - normal_out - non_normal_out
prev_ext = 1400 / 6 * 2
next_time = 1500 + prev_ext - normal_out - non_normal_out
comty = 150
extra_permanent_loss = 150
final = next_time + total_weight + act - comty - extra_permanent_loss
print("Now: ", total_weight)
print("Final: ", final)
print("=======================================================")
print("ATH: ", ATH)
print("Actual amount: ", amont_px, "Shib")
print("Actual amount: ", avg_pr, "€")
print("Average price (w): ", average, "€")
print("Lower price (w): ", avg_pr-total_fall, "€")
print("Injection: ", inject, "€")
print("Fall factor: ", fall_factor * 100, "%")
print("Total fall: ", total_fall, "€")
print("Number of steps: ", n_div)
# print(buys)
print("Buys: ", sum(buys))
future_hold = sum(buys) + amont_px
print("Future hold: ", future_hold)
print("Future hold: ", future_hold*ATH)
print("Hold in 0,005", future_hold*0.05)
print("After burn: ", final-inject)