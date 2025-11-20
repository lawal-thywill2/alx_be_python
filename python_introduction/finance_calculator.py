user_monthly_income = float(input("Enter your monthly income: "))
user_monthly_expenses = float(input("Enter your monthly expenses: "))
monthly_savings = user_monthly_income - user_monthly_expenses
print("Your monthly savings are:", monthly_savings)
projected_savings = monthly_savings * 12 + (monthly_savings * 0.05 * 12)
print("projected savings after one year, with interest, is:", projected_savings)