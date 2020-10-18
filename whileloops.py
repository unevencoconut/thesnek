# PYTHON WHILE LOOPS
# Two Primitive Loop Commands
# While and For

# Keyword: while
# Loop as long as condition is true
i = 1
while i < 6:
    print(i)
    i += 1

# Keyword: break
# With the Break Statement, we can stop the loop if while true
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# Keyword: continue
# With the Continue Statement we can stop the current iteration and continue with the next
i = 0
while i < 6:
    i += 1
    if i == 3: # Observe, there is not 3 is the output
        continue
    print(i)

# Keywrod: else
# This will run a Block of Code when the condition is no longer True
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")