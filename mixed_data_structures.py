# Q41. Student Performance System

students = [
    {"id": 1, "name": "Ali", "marks": (85, 90, 88)},
    {"id": 2, "name": "Sara", "marks": (92, 95, 91)},
    {"id": 3, "name": "Ahmed", "marks": (78, 84, 80)}
]

ali_average = sum(students[0]["marks"]) / len(students[0]["marks"])
sara_average = sum(students[1]["marks"]) / len(students[1]["marks"])
ahmed_average = sum(students[2]["marks"]) / len(students[2]["marks"])

averages = {
    students[0]["name"]: ali_average,
    students[1]["name"]: sara_average,
    students[2]["name"]: ahmed_average
}

top_student = max(averages, key=averages.get)

names = (
    students[0]["name"],
    students[1]["name"],
    students[2]["name"]
)

unique_marks = set(
    students[0]["marks"]
    + students[1]["marks"]
    + students[2]["marks"]
)

print("Q41 Averages:", averages)
print("Top Student:", top_student)
print("Names:", names)
print("Unique Marks:", unique_marks)


# Q42. Employee Skills

employees = {
    "Ali": {"Python", "SQL", "AWS"},
    "Sara": {"Python", "Databricks", "SQL"},
    "Ahmed": {"AWS", "Snowflake", "SQL"}
}

common_skills = (
    employees["Ali"]
    & employees["Sara"]
    & employees["Ahmed"]
)

ali_only = employees["Ali"] - (
    employees["Sara"] | employees["Ahmed"]
)

all_team_skills = (
    employees["Ali"]
    | employees["Sara"]
    | employees["Ahmed"]
)

required_skills = {"Python", "SQL"}

ali_qualified = required_skills.issubset(employees["Ali"])
sara_qualified = required_skills.issubset(employees["Sara"])
ahmed_qualified = required_skills.issubset(employees["Ahmed"])

qualified_employees = (
    {"Ali"} if ali_qualified else set()
) | (
    {"Sara"} if sara_qualified else set()
) | (
    {"Ahmed"} if ahmed_qualified else set()
)

print("Q42 Common Skills:", common_skills)
print("Ali Only Skills:", ali_only)
print("All Team Skills:", all_team_skills)
print("Qualified Employees:", qualified_employees)


# Q43. Sales Data

sales = [
    ("Laptop", 120000, 2),
    ("Mouse", 1500, 5),
    ("Keyboard", 3500, 3)
]

laptop_revenue = sales[0][1] * sales[0][2]
mouse_revenue = sales[1][1] * sales[1][2]
keyboard_revenue = sales[2][1] * sales[2][2]

total_revenue = laptop_revenue + mouse_revenue + keyboard_revenue

revenue = {
    sales[0][0]: laptop_revenue,
    sales[1][0]: mouse_revenue,
    sales[2][0]: keyboard_revenue
}

top_product = max(revenue, key=revenue.get)

prices = {
    sales[0][1],
    sales[1][1],
    sales[2][1]
}

print("Q43 Total Revenue:", total_revenue)
print("Top Revenue Product:", top_product)
print("Name to Revenue:", revenue)
print("Prices:", prices)


# Q44. Customer Orders

customers = {
    "C101": {"name": "Ali", "orders": [1200, 2500, 1800]},
    "C102": {"name": "Sara", "orders": [3000, 4500]},
    "C103": {"name": "Ahmed", "orders": [1500, 2000, 1000]}
}

ali_total = sum(customers["C101"]["orders"])
sara_total = sum(customers["C102"]["orders"])
ahmed_total = sum(customers["C103"]["orders"])

spending = {
    "Ali": ali_total,
    "Sara": sara_total,
    "Ahmed": ahmed_total
}

top_customer = max(spending, key=spending.get)

customer_totals = (
    ali_total,
    sara_total,
    ahmed_total
)

print("Q44 Spending:", spending)
print("Top Customer:", top_customer)
print("Customer Totals:", customer_totals)


# Q45. Course Enrollment

courses = {
    "Python": {"Ali", "Sara", "Ahmed"},
    "SQL": {"Sara", "Ahmed", "Zain"},
    "AWS": {"Ali", "Ahmed", "Zain"}
}

python = courses["Python"]
sql = courses["SQL"]
aws = courses["AWS"]

all_three = python & sql & aws

exactly_two = (
    ((python & sql) - aws)
    | ((python & aws) - sql)
    | ((sql & aws) - python)
)

exactly_one = (
    (python - sql - aws)
    | (sql - python - aws)
    | (aws - python - sql)
)

all_students = python | sql | aws
unique_student_count = len(all_students)

print("Q45 Exactly Two:", exactly_two)
print("All Three Courses:", all_three)
print("Exactly One:", exactly_one)
print("Unique Students:", unique_student_count)


# Q46. E-Commerce Transactions

transactions = [
    {
        "id": 101,
        "customer": "Ali",
        "items": [("Laptop", 120000, 1), ("Mouse", 1500, 2)]
    },
    {
        "id": 102,
        "customer": "Sara",
        "items": [("Keyboard", 3500, 2), ("Mouse", 1500, 1)]
    },
    {
        "id": 103,
        "customer": "Ali",
        "items": [("Monitor", 45000, 1)]
    }
]

transaction1 = (
    transactions[0]["items"][0][1] * transactions[0]["items"][0][2]
    + transactions[0]["items"][1][1] * transactions[0]["items"][1][2]
)

transaction2 = (
    transactions[1]["items"][0][1] * transactions[1]["items"][0][2]
    + transactions[1]["items"][1][1] * transactions[1]["items"][1][2]
)

transaction3 = (
    transactions[2]["items"][0][1] * transactions[2]["items"][0][2]
)

total_revenue = transaction1 + transaction2 + transaction3

ali_spending = transaction1 + transaction3

largest_transaction = max(
    transaction1,
    transaction2,
    transaction3
)

unique_products = {
    transactions[0]["items"][0][0],
    transactions[0]["items"][1][0],
    transactions[1]["items"][0][0],
    transactions[2]["items"][0][0]
}

print("Q46 Total Revenue:", total_revenue)
print("Ali Spending:", ali_spending)
print("Largest Transaction:", largest_transaction)
print("Unique Products:", unique_products)


# Q47. Pipeline Monitoring

pipelines = {
    "pipeline_1": {"status": "success", "records": (1000, 1200, 1100)},
    "pipeline_2": {"status": "failed", "records": (800, 0, 0)},
    "pipeline_3": {"status": "success", "records": (1500, 1600, 1700)}
}

pipeline1_total = sum(pipelines["pipeline_1"]["records"])
pipeline2_total = sum(pipelines["pipeline_2"]["records"])
pipeline3_total = sum(pipelines["pipeline_3"]["records"])

total_records = (
    pipeline1_total
    + pipeline2_total
    + pipeline3_total
)

failed_pipelines = {
    "pipeline_2"
} if pipelines["pipeline_2"]["status"] == "failed" else set()

largest_pipeline = max(
    pipeline1_total,
    pipeline2_total,
    pipeline3_total
)

averages = {
    "pipeline_1": pipeline1_total / len(pipelines["pipeline_1"]["records"]),
    "pipeline_2": pipeline2_total / len(pipelines["pipeline_2"]["records"]),
    "pipeline_3": pipeline3_total / len(pipelines["pipeline_3"]["records"])
}

print("Q47 Total Records:", total_records)
print("Failed Pipelines:", failed_pipelines)
print("Largest Pipeline Total:", largest_pipeline)
print("Average Records:", averages)


# Q48. Banking Transactions

accounts = {
    "A101": {"holder": "Ali", "transactions": [5000, -2000, 3000, -1000]},
    "A102": {"holder": "Sara", "transactions": [10000, -3000, -2000]},
    "A103": {"holder": "Ahmed", "transactions": [7000, -1500, 2500]}
}

ali_balance = sum(accounts["A101"]["transactions"])
sara_balance = sum(accounts["A102"]["transactions"])
ahmed_balance = sum(accounts["A103"]["transactions"])

balances = {
    "Ali": ali_balance,
    "Sara": sara_balance,
    "Ahmed": ahmed_balance
}

highest_balance = max(balances.values())

total_withdrawals = (
    2000 + 1000
    + 3000 + 2000
    + 1500
)

largest_deposit = max(
    5000, 3000,
    10000,
    7000, 2500
)

print("Q48 Final Balances:", balances)
print("Highest Balance:", highest_balance)
print("Total Withdrawals:", total_withdrawals)
print("Largest Deposit:", largest_deposit)


# Q49. Product Recommendations

users = {
    "Ali": {
        "purchased": {"Laptop", "Mouse"},
        "wishlist": {"Keyboard", "Monitor", "Mouse"}
    },
    "Sara": {
        "purchased": {"Keyboard", "Monitor"},
        "wishlist": {"Laptop", "Mouse"}
    },
    "Ahmed": {
        "purchased": {"Laptop", "Keyboard"},
        "wishlist": {"Monitor", "Headphones"}
    }
}

ali_purchased = users["Ali"]["purchased"]
sara_purchased = users["Sara"]["purchased"]
ahmed_purchased = users["Ahmed"]["purchased"]

bought_by_two_or_more = (
    (ali_purchased & sara_purchased)
    | (ali_purchased & ahmed_purchased)
    | (sara_purchased & ahmed_purchased)
)

ali_recommendations = (
    users["Ali"]["wishlist"] - users["Ali"]["purchased"]
)

shared_wishlist = (
    (users["Ali"]["wishlist"] & users["Sara"]["wishlist"])
    | (users["Ali"]["wishlist"] & users["Ahmed"]["wishlist"])
    | (users["Sara"]["wishlist"] & users["Ahmed"]["wishlist"])
)

all_products = (
    users["Ali"]["purchased"]
    | users["Ali"]["wishlist"]
    | users["Sara"]["purchased"]
    | users["Sara"]["wishlist"]
    | users["Ahmed"]["purchased"]
    | users["Ahmed"]["wishlist"]
)

print("Q49 Bought by Two or More:", bought_by_two_or_more)
print("Ali Recommendations:", ali_recommendations)
print("Shared Wishlist:", shared_wishlist)
print("All Products:", all_products)


# Q50. Final Company Analysis

company = {
    "departments": {
        "Engineering": {
            "employees": [
                ("Ali", 120000, {"Python", "AWS", "SQL"}),
                ("Sara", 150000, {"Python", "Databricks", "SQL"})
            ],
            "budget": 500000
        },
        "Analytics": {
            "employees": [
                ("Ahmed", 100000, {"SQL", "Power BI"}),
                ("Zain", 130000, {"Python", "SQL", "Tableau"})
            ],
            "budget": 400000
        }
    }
}

engineering = company["departments"]["Engineering"]
analytics = company["departments"]["Analytics"]

engineering_payroll = (
    engineering["employees"][0][1]
    + engineering["employees"][1][1]
)

analytics_payroll = (
    analytics["employees"][0][1]
    + analytics["employees"][1][1]
)

company_payroll = engineering_payroll + analytics_payroll

highest_paid = max(
    engineering["employees"][0],
    engineering["employees"][1],
    analytics["employees"][0],
    analytics["employees"][1],
    key=lambda employee: employee[1]
)

shared_skills = (
    engineering["employees"][0][2]
    & engineering["employees"][1][2]
    & analytics["employees"][0][2]
    & analytics["employees"][1][2]
)

engineering_skills = (
    engineering["employees"][0][2]
    | engineering["employees"][1][2]
)

analytics_skills = (
    analytics["employees"][0][2]
    | analytics["employees"][1][2]
)

engineering_only = engineering_skills - analytics_skills

engineering_remaining = engineering["budget"] - engineering_payroll
analytics_remaining = analytics["budget"] - analytics_payroll

engineering_average = engineering_payroll / 2
analytics_average = analytics_payroll / 2

higher_average_department = (
    "Engineering"
    if engineering_average > analytics_average
    else "Analytics"
)

name_to_salary = {
    engineering["employees"][0][0]: engineering["employees"][0][1],
    engineering["employees"][1][0]: engineering["employees"][1][1],
    analytics["employees"][0][0]: analytics["employees"][0][1],
    analytics["employees"][1][0]: analytics["employees"][1][1]
}

all_unique_skills = engineering_skills | analytics_skills

combined_budget = engineering["budget"] + analytics["budget"]

budget_sufficient = combined_budget >= company_payroll

print("Q50 Engineering Payroll:", engineering_payroll)
print("Analytics Payroll:", analytics_payroll)
print("Company Payroll:", company_payroll)
print("Highest Paid Employee:", highest_paid)
print("Shared Skills:", shared_skills)
print("Engineering Only Skills:", engineering_only)
print("Engineering Remaining Budget:", engineering_remaining)
print("Analytics Remaining Budget:", analytics_remaining)
print("Higher Average Salary Department:", higher_average_department)
print("Name to Salary:", name_to_salary)
print("All Unique Skills:", all_unique_skills)
print("Combined Budget Sufficient:", budget_sufficient)
