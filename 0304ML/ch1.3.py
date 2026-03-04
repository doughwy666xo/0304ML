# A list of dictionaries — mimics a simple database table
employees = [
    {"name": "Alice",   "dept": "Sales",   "salary": 72_000},
    {"name": "Bob",     "dept": "Finance", "salary": 85_000},
    {"name": "Carol",   "dept": "Sales",   "salary": 69_000},
    {"name": "David",   "dept": "IT",      "salary": 92_000},
]

# Filter: Sales department only
sales_team = [e for e in employees if e["dept"] == "Sales"]
avg_sales_salary = sum(e["salary"] for e in sales_team) / len(sales_team)

print(f"Average Sales Salary: ${avg_sales_salary:,.2f}")
print(avg_sales_salary)
print(sales_team)