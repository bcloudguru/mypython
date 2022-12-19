# 365 days, 52 weeks and 12 months
# calculate the days , weeks and years left in your life if you live for 90 years
age=input("whats is your current age?")
balance_age=90-int(age)
bal_months=balance_age*12
balance_days=balance_age*365
balance_weeks=balance_age*52
print(f"You have {balance_days} days, {balance_weeks} weeks, and {bal_months} months left.")
