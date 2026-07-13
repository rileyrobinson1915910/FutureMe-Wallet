name = input("What name would you like us to use? ")
age = int(input(f"{name}, what is your age? "))
income = float(input(f"{name}, what is your weekly income? $"))
savings = float(input(f"{name}, what are your weekly savings? $"))
spending = float(input(f"{name}, what is your weekly spending? $"))


def calculate_future(age):
    return age + 5, age + 10


age_five, age_ten = calculate_future(age)

print(f"In 5 years you will be {age_five}")
print(f"In 10 years you will be {age_ten}")


def health_score_basic(spending, savings):
    if spending >= savings:
        return "We need to work on your finance skills."
    return "Good job managing your spending!"


print(health_score_basic(spending, savings))


def core_calculations(spending, savings, income):
    return income * 52, spending * 52, savings * 52


yearly_income, yearly_spending, yearly_savings = core_calculations(spending, savings, income)

print(f"Yearly Income: ${yearly_income:.2f}")
print(f"Yearly Spending: ${yearly_spending:.2f}")
print(f"Yearly Savings: ${yearly_savings:.2f}")

if yearly_income > 0:

    def health_score(yearly_income, yearly_spending, yearly_savings):
        return yearly_savings / yearly_income, yearly_spending / yearly_income

    savings_rate, spending_rate = health_score(yearly_income, yearly_spending, yearly_savings)

    print(f"Savings Rate: {savings_rate:.2%}")
    print(f"Spending Rate: {spending_rate:.2%}")

    def score_system(savings_rate, spending, savings):
        if spending > savings:
            return "We need to work on controlling your spending."
        if savings_rate >= 0.2:
            return "Excellent, your future self is on track to financial freedom!"
        elif 0.1 <= savings_rate < 0.2:
            return "Your score is okay, but we can improve."
        return "We need to work on controlling your spending."

    print(score_system(savings_rate, spending, savings))

    FM_state_pos = yearly_savings * 5

    def financial_health_score_full(savings_rate, spending_rate, spending, savings):
        if spending > savings:
            category = "Bad"
        elif savings_rate >= 0.2 and spending_rate <= 0.5:
            category = "Excellent"
        elif savings_rate >= 0.1 and spending_rate <= 0.7:
            category = "Okay"
        else:
            category = "Bad"

        messages = {
            "Excellent": "Your future self is on track to financial freedom!",
            "Okay": "You are doing okay, but there is room to improve.",
            "Bad": "We need to work on controlling your spending.",
        }
        return category, messages[category]

    category, message = financial_health_score_full(savings_rate, spending_rate, spending, savings)

    print(f"Category: {category}")
    print(message)

    if category == "Excellent":
        print(f"{name}, when you are {age_five}, you will have saved approximately ${FM_state_pos:.2f}")
        print("Keep it up and you're building strong financial habits!")
    elif category == "Bad":
        print("Small changes now could save thousands over time.")

savings_goals_calc_quest = input("Would you like to try our Savings Goal Calculator? (yes/no) ")

if savings_goals_calc_quest.lower() == "yes":

    goal = float(input("What is your desired amount of money? $"))
    weeks = int(input("In how many weeks do you want to accomplish this goal? "))

    goal_acc = goal / weeks
    short_acc = goal / savings if savings > 0 else 0

    print(f"In order to reach your goal of ${goal:.2f}, you need to save ${goal_acc:.2f} per week to accomplish your goal in {weeks} weeks.")

    if savings > 0 and goal_acc < savings:
        print(f"Great job! You are on track to accomplish your goal of ${goal:.2f}.")
        print(f"At this current rate, you will complete your goal in approximately {short_acc:.1f} weeks.")
    elif savings > 0 and goal_acc == savings:
        print(f"Good job! At this rate, you are on track to accomplish your goal of ${goal:.2f}.")
        print("You're already saving exactly what you need — no extra cuts required.")
    else:
        print(f"You are not on track to accomplish your goal of ${goal:.2f}.")

        gap = goal_acc - savings
        print(f"Challenge: Cut your spending by ${gap:.2f} per week to bring your savings up to ${goal_acc:.2f}/week and hit your goal in {weeks} weeks.")

        easier_cut = gap / 2
        new_savings_easier = savings + easier_cut
        if new_savings_easier > 0:
            easier_weeks = goal / new_savings_easier
            print(f"Prefer a lighter lift? Cut spending by just ${easier_cut:.2f} per week instead, and you'd reach your goal in about {easier_weeks:.1f} weeks.")

        goal_diff = goal_acc - savings
        print(f"Current Savings: ${savings:.2f}")
        print(f"Necessary Savings: ${goal_acc:.2f}")
        print(f"Savings Difference: ${goal_diff:.2f}")