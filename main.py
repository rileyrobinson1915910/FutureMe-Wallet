import streamlit as st
from calculations import calculate_future, core_calculations, health_score
from messages import health_score_basic, score_system, financial_health_score_full

st.set_page_config(page_title="Future Me Wallet", page_icon="💰", layout="centered")

st.title("💰 Future Me Wallet")
st.write("Let's start with a few questions.")

if "show_goal_calc" not in st.session_state:
    st.session_state.show_goal_calc = False

name = st.text_input("What name would you like us to use?")

age = None
if name:
    age = st.number_input(
        f"{name}, what is your age?",
        min_value=0, step=1, value=None, placeholder="Enter your age",
    )

income = None
if age is not None:
    income = st.number_input(
        f"{name}, what is your weekly income?",
        min_value=0.0, value=None, placeholder="Enter weekly income ($)",
    )

savings = None
if income is not None:
    savings = st.number_input(
        f"{name}, what are your weekly savings?",
        min_value=0.0, value=None, placeholder="Enter weekly savings ($)",
    )

spending = None
if savings is not None:
    spending = st.number_input(
        f"{name}, what is your weekly spending?",
        min_value=0.0, value=None, placeholder="Enter weekly spending ($)",
    )

if spending is not None:

    age_five, age_ten = calculate_future(age)

    st.divider()
    st.subheader("📅 Future Age")
    c1, c2 = st.columns(2)
    c1.metric("In 5 years", f"{age_five}")
    c2.metric("In 10 years", f"{age_ten}")

    st.subheader("🩺 Basic Health Score")
    msg, ok = health_score_basic(spending, savings)
    if ok:
        st.success(msg)
    else:
        st.warning(msg)

    yearly_income, yearly_spending, yearly_savings = core_calculations(
        spending, savings, income
    )

    st.subheader("📊 Yearly Projections")
    c1, c2, c3 = st.columns(3)
    c1.metric("Yearly Income", f"${yearly_income:,.2f}")
    c2.metric("Yearly Spending", f"${yearly_spending:,.2f}")
    c3.metric("Yearly Savings", f"${yearly_savings:,.2f}")

    if yearly_income > 0:

        savings_rate, spending_rate = health_score(
            yearly_income, yearly_spending, yearly_savings
        )

        st.subheader("📈 Financial Ratios")
        st.write(f"Savings Rate: **{savings_rate:.2%}**")
        st.progress(min(savings_rate, 1.0))
        st.write(f"Spending Rate: **{spending_rate:.2%}**")
        st.progress(min(spending_rate, 1.0))

        st.subheader("🏆 Score")
        st.info(score_system(savings_rate, spending, savings))

        FM_state_pos = yearly_savings * 5

        category, message = financial_health_score_full(
            savings_rate, spending_rate, spending, savings
        )

        st.subheader("🔮 Future Me")
        st.write(f"Category: **{category}**")
        st.write(message)

        if category == "Excellent":
            st.success(
                f"{name}, when you are {age_five}, you will have saved approximately "
                f"${FM_state_pos:,.2f}"
            )
            st.write("Keep it up and you're building strong financial habits!")
        elif category == "Bad":
            st.warning("Small changes now could save thousands over time.")

    st.divider()
    st.subheader("🎯 Savings Goal Calculator")

    savings_goals_calc_quest = st.selectbox(
        "Would you like to try our Savings Goal Calculator?",
        ["No", "Yes"],
    )
    st.session_state.show_goal_calc = savings_goals_calc_quest == "Yes"

    if st.session_state.show_goal_calc:

        goal = st.number_input(
            "What is your desired amount of money?",
            min_value=0.0, value=None, placeholder="Enter your goal amount ($)",
        )

        weeks = None
        if goal is not None:
            weeks = st.number_input(
                "In how many weeks do you want to accomplish this goal?",
                min_value=1, step=1, value=None, placeholder="Enter number of weeks",
            )

        if weeks is not None:
            goal_acc = goal / weeks
            short_acc = goal / savings if savings > 0 else 0

            st.write(
                f"In order to reach your goal of ${goal:,.2f}, you need to save "
                f"${goal_acc:,.2f} per week to accomplish your goal in {weeks} weeks."
            )

            if savings > 0 and goal_acc < savings:
                st.success(f"Great job! You are on track to accomplish your goal of ${goal:,.2f}.")
                st.write(
                    f"At this current rate, you will complete your goal in approximately "
                    f"{short_acc:.1f} weeks."
                )
            elif savings > 0 and goal_acc == savings:
                st.info(f"Good job! At this rate, you are on track to accomplish your goal of ${goal:,.2f}.")
                st.write("You're already saving exactly what you need — no extra cuts required.")
            else:
                st.error(f"You are not on track to accomplish your goal of ${goal:,.2f}.")

                gap = goal_acc - savings
                st.write(
                    f"Challenge: Cut your spending by ${gap:,.2f} per week to bring your "
                    f"savings up to ${goal_acc:,.2f}/week and hit your goal in {weeks} weeks."
                )

                easier_cut = gap / 2
                new_savings_easier = savings + easier_cut
                if new_savings_easier > 0:
                    easier_weeks = goal / new_savings_easier
                    st.write(
                        f"Prefer a lighter lift? Cut spending by just ${easier_cut:,.2f} per "
                        f"week instead, and you'd reach your goal in about {easier_weeks:.1f} "
                        f"weeks."
                    )

                c1, c2, c3 = st.columns(3)
                c1.metric("Current Savings", f"${savings:,.2f}")
                c2.metric("Necessary Savings", f"${goal_acc:,.2f}")
                c3.metric("Difference", f"${gap:,.2f}")