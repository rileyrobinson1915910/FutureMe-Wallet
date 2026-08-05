import streamlit as st
from calculations import calculate_future, core_calculations, health_score
from messages import health_score_basic, score_system, financial_health_score_full
from database import get_connection, get_user, insert_user, update_user_field

st.set_page_config(page_title="Future Me Wallet", page_icon="💰", layout="centered")

connection, cursor = get_connection()

st.title("💰 Future Me Wallet")
st.write("Let's start with a few questions.")

name = st.text_input("What name would you like us to use?")

age = income = savings = spending = None
existing_user = None

if name:
    existing_user = get_user(cursor, name)

# ---------- RETURNING USER ----------
if existing_user is not None:
    _, saved_age, saved_income, saved_savings, saved_spending = existing_user

    st.success(f"Welcome back, {name}!")

    c1, c2 = st.columns(2)
    c1.metric("Age", saved_age)
    c2.metric("Income", f"${saved_income:,.2f}")
    c3, c4 = st.columns(2)
    c3.metric("Savings", f"${saved_savings:,.2f}")
    c4.metric("Spending", f"${saved_spending:,.2f}")

    st.divider()
    st.subheader("Update your info")

    field_choice = st.selectbox(
        "Would you like to update a field?",
        ["No", "Age", "Income", "Savings", "Spending"]
    )

    if field_choice != "No":
        new_value = st.number_input(f"New {field_choice.lower()}", min_value=0.0, value=None)
        if new_value is not None and st.button("Save update"):
            column_map = {"Age": "age", "Income": "income", "Savings": "savings", "Spending": "spending"}
            update_user_field(cursor, connection, name, column_map[field_choice], new_value)
            st.success(f"{field_choice} updated! Refresh the page to see your new results below.")

    age, income, savings, spending = saved_age, saved_income, saved_savings, saved_spending

# ---------- NEW USER ----------
elif name:
    age = st.number_input(
        f"{name}, what is your age?",
        min_value=0, step=1, value=None, placeholder="Enter your age",
    )

    if age is not None:
        income = st.number_input(
            f"{name}, what is your weekly income?",
            min_value=0.0, value=None, placeholder="Enter weekly income ($)",
        )

    if income is not None:
        savings = st.number_input(
            f"{name}, what are your weekly savings?",
            min_value=0.0, value=None, placeholder="Enter weekly savings ($)",
        )

    if savings is not None:
        spending = st.number_input(
            f"{name}, what is your weekly spending?",
            min_value=0.0, value=None, placeholder="Enter weekly spending ($)",
        )

    if spending is not None:
        insert_user(cursor, connection, name, age, income, savings, spending)
        st.success("New record saved!")

# ---------- RESULTS (shown for both new and returning users, once data is ready) ----------
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

connection.close()