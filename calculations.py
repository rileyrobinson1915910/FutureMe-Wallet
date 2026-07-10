def calculate_future(age):
    return age + 5, age + 10

def core_calculations(spending, savings, income):
    yearly_income = income * 52
    yearly_spending = spending * 52
    yearly_savings = savings * 52
    return yearly_income, yearly_spending, yearly_savings

def health_score(yearly_income, yearly_spending, yearly_savings):
    savings_rate = yearly_savings / yearly_income
    spending_rate = yearly_spending / yearly_income
    return savings_rate, spending_rate