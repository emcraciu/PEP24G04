blocks = int(input("Give blocks"))

current_blocks = 0
high = 0
for i in range(1, 1000000000000000):
    if blocks >= i + current_blocks:
        high += 1
        current_blocks += i
    else:
        break

print(high)
