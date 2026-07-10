def health_score_basic(spending, savings):
    if spending >= savings:
        return "We need to work on your finance skills.", False
    return "Good job managing your spending!", True


def score_system(savings_rate, spending, savings):
    if spending > savings:
        return "We need to work on controlling your spending."
    if savings_rate >= 0.2:
        return "Excellent, your future self is on track to financial freedom!"
    elif 0.1 <= savings_rate < 0.2:
        return "Your score is okay, but we can improve."
    return "We need to work on controlling your spending."


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