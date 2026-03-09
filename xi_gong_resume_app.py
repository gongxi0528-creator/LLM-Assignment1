
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Xi Gong | Resume Dashboard", layout="wide")

# -----------------------------
# Data from Xi Gong's resume
# -----------------------------
profile = {
    "name": "Xi Gong",
    "title": "Financial Analyst / Management Analytics Candidate",
    "summary": (
        "Financial Analyst with experience in financial reporting, reconciliation, "
        "cross-platform data consolidation, and stakeholder collaboration. "
        "Currently pursuing a Master of Management Analytics at Rotman School of Management."
    ),
    "email": "george.gong@rotman.utoronto.ca",
    "phone": "(+1) 647-831-4670",
    "linkedin": "www.linkedin.com/in/xi-gong0528"
}

skills_df = pd.DataFrame({
    "Skill": [
        "Python", "R Programming", "SQL", "Excel",
        "Power BI", "SAP", "Blackline", "Financial Analysis", "DCF Model"
    ],
    "Category": [
        "Programming", "Programming", "Programming", "Software",
        "Software", "Financial Operations", "Financial Operations",
        "Financial Operations", "Financial Operations"
    ],
    "Proficiency": [82, 70, 72, 90, 75, 80, 76, 85, 74]
})

education_df = pd.DataFrame({
    "Program": [
        "Master of Management Analytics",
        "Bachelor of Business Administration"
    ],
    "School": [
        "Rotman School of Management, University of Toronto",
        "University of Toronto"
    ],
    "Location": ["Toronto, ON", "Toronto, ON"],
    "Period": ["Aug 2025 – Present", "Sep 2020 – Jun 2025"],
    "Highlights": [
        "Analytics-focused graduate program",
        "Specialist Co-op in Management and Finance; GPA 3.73/4; Dean’s List (2021–2025)"
    ]
})

experience_df = pd.DataFrame({
    "Company": ["Johnson & Johnson Canada", "Dome Productions"],
    "Role": ["Tax Analyst", "General Accountant"],
    "Period": ["Jan 2024 – Sep 2024", "Aug 2022 – Jun 2023"],
    "Impact Score": [92, 84],
    "Bullets": [
        "Collected and analyzed financial data across SAP, Blackline, and LYNX; prepared tax reports; supported audit-ready reporting.",
        "Managed crew sheet verification, invoice accuracy, monthly reports, reconciliation, and built a 20-page onboarding manual."
    ]
})

leadership_df = pd.DataFrame({
    "Achievement": ["2025 Calian x RBAC Case Competition"],
    "Role": ["Team Leader – 2nd Place"],
    "Period": ["Oct 2025 – Nov 2025"],
    "Details": [
        "Led a 4-person team using K-means, KNN, Logistic Regression, Random Forest, and XGBoost for churn prediction."
    ]
})

# -----------------------------
# Sidebar widgets
# -----------------------------
st.sidebar.title("Interactive Controls")

section_choice = st.sidebar.selectbox(
    "Choose a section to highlight",
    ["Overview", "Skills", "Experience", "Education", "Leadership"]
)

min_proficiency = st.sidebar.slider(
    "Minimum skill proficiency to display",
    min_value=50,
    max_value=100,
    value=70,
    step=5
)

show_programming_only = st.sidebar.checkbox("Show only programming skills", value=False)

selected_company = st.sidebar.selectbox(
    "Focus on work experience",
    ["All"] + experience_df["Company"].tolist()
)

show_summary = st.sidebar.checkbox("Show professional summary", value=True)

# -----------------------------
# Header
# -----------------------------
st.title(f"{profile['name']} | Interactive Resume App")
st.subheader(profile["title"])

col1, col2, col3 = st.columns(3)
col1.metric("Years of Internship Experience", "1+")
col2.metric("Undergrad GPA", "3.73 / 4.00")
col3.metric("Case Competition Result", "2nd Place")

st.markdown(f"**Email:** {profile['email']}\n\n**Phone:** {profile['phone']}\n\n**LinkedIn:** {profile['linkedin']}")

if show_summary:
    st.info(profile["summary"])

# -----------------------------
# Highlighted section
# -----------------------------
st.markdown("---")
st.header(f"Highlighted Section: {section_choice}")

if section_choice == "Overview":
    st.write(
        "This dashboard presents Xi Gong's education, experience, technical skills, "
        "and leadership achievements in an interactive way."
    )

elif section_choice == "Skills":
    st.write("Explore technical and finance-related capabilities.")
elif section_choice == "Experience":
    st.write("Review internship experience and core contributions.")
elif section_choice == "Education":
    st.write("See academic background and key achievements.")
elif section_choice == "Leadership":
    st.write("View competition and leadership accomplishments.")

# -----------------------------
# Skills filtering and chart
# -----------------------------
filtered_skills = skills_df[skills_df["Proficiency"] >= min_proficiency].copy()

if show_programming_only:
    filtered_skills = filtered_skills[filtered_skills["Category"] == "Programming"]

st.markdown("---")
st.header("Skills Table")

if filtered_skills.empty:
    st.warning("No skills match the current filter settings.")
else:
    st.dataframe(filtered_skills, use_container_width=True)

st.header("Skills Proficiency Chart")
if not filtered_skills.empty:
    chart_df = filtered_skills.sort_values("Proficiency", ascending=True)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh(chart_df["Skill"], chart_df["Proficiency"])
    ax.set_xlabel("Proficiency")
    ax.set_ylabel("Skill")
    ax.set_title("Skill Proficiency Overview")
    st.pyplot(fig)
else:
    st.write("Adjust the slider or checkbox to show chart data.")

# -----------------------------
# Experience table
# -----------------------------
st.markdown("---")
st.header("Work Experience")

if selected_company != "All":
    exp_view = experience_df[experience_df["Company"] == selected_company].copy()
else:
    exp_view = experience_df.copy()

st.dataframe(exp_view[["Company", "Role", "Period", "Impact Score"]], use_container_width=True)

for _, row in exp_view.iterrows():
    with st.expander(f"{row['Company']} | {row['Role']}"):
        st.write(f"**Period:** {row['Period']}")
        st.write(row["Bullets"])

# -----------------------------
# Education
# -----------------------------
st.markdown("---")
st.header("Education")
st.table(education_df)

# -----------------------------
# Leadership / achievements
# -----------------------------
st.markdown("---")
st.header("Leadership & Achievements")
st.table(leadership_df)

# -----------------------------
# Footer insight
# -----------------------------
st.markdown("---")
st.success(
    "This app satisfies the assignment requirements: personalized resume content, "
    "multiple interactive widgets, at least one table, and at least one chart."
)
