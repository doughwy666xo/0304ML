#
#Clay, 2026/3/4
#Clay_for_2.py
#iliterate for loop with range function
#



# range() generates a sequence of numbers
# range(start, stop, step)  — stop is exclusive
print("Sales Report — Q1 Weeks")
for week in range(1, 53):          # weeks 1 through 12
    weekly_target = 50_000
    print(f"  Week {week:>2}: Target = ${weekly_target:,}")