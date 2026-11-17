# Python Code List
01.py:
```python
total_sum = sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0)
print(total_sum)
## Sum of Multiples (3 or 5)

This Python one-liner calculates the sum of all numbers below 1000 that are multiples of either 3 or 5 (a classic coding puzzle).

### How it works:
- **`range(1000)`**: Generates numbers from 0 up to 999.
- **`if i % 3 == 0 or i % 5 == 0`**: Filters the numbers, keeping only those that are divisible by 3, by 5, or by both.
- **`sum(...)`**: Adds all of those filtered numbers together into one total.
- **`print(total_sum)`**: Displays the final calculated result on the screen.
