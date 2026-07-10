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