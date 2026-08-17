def calculate_future(age):
    age_five = age + 5
    age_ten = age + 10
    return age_five, age_ten


def core_calculations(income, spending, savings):
    yearly_income = income * 52
    yearly_spending = spending * 52
    yearly_savings = savings * 52
    return yearly_income, yearly_spending, yearly_savings


def health_score(yearly_income, yearly_spending, yearly_savings):
    savings_rate = yearly_savings / yearly_income
    spending_rate = yearly_spending / yearly_income
    return savings_rate, spending_rate