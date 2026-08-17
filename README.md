FutureMe Wallet is a financial literacy tool that shows you where your money habits are actually taking you and not just where you stand today.

Why I built this:

I noticed a gap, most financial literacy apps show you a snapshot of where your money is right now, however I recognized that if you can simulate where you're going it is much easier for you interact and stick with your goals because you can almost see the future and how the decision you are about to make will impact you in 10 years.

I grew up hearing my parents, one of whom is an immigrant, speak about financial literacy and how they had no clue what savings, budgeting, and investing even were until they were well into adulthood. Education and technology have come a long ways since my parents were kids, however my friends portray the same story my parents lived 40 years ago revolving around financial literacy. School curriculums haven't caught up to how complicated managing money has become; kids are expected to navigate credit, digital banking, and investing with essentially no formal education on any of it.

FutureMe Wallet is my attempt at closing a small piece of that gap, it's a tool simple enough that it could've actually helped my own family, and help my friends understand where their money is going before they're adults making real financial decisions with no foundation.

What it does: Collects a few basic financial habits (income, savings, spending) Projects what those habits mean for your future self. it;s not just a spending breakdown, but it shows where you're actually headed in 5 and 10 years if you continue the same habits now. Gives a plain-language financial health score based on savings vs. spending Includes a goal calculator that tells you exactly how much to save per week to hit a savings goal on time and a lighter alternative if the exact number feels out of reach Lets returning users update their saved data, field by field, instead of starting over Tech stack Python — core logic and calculations Streamlit — web app framework and UI SQLite — data persistence across sessions Project structure futureme-wallet/ ├── main.py # Streamlit UI ├── calculations.py # Core financial math (pure functions, no UI) ├── messages.py # Scoring and feedback logic ├── legacy_console_version.py # Original plain-Python (no Streamlit) version, kept for reference ├── requirements.txt └── .streamlit/ └── config.toml # App theme Running it locally bash pip install -r requirements.txt streamlit run main.py Status

Actively in development. Currently working on:

Persisting user data across sessions with SQLite Expanding the goal calculator Ongoing UI/UX polish About

Built by Riley Robinson, planning to submit to the Congressional App Challenge.
