
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Xi Gong | Resume Dashboard", layout="wide")

profile = {
    "name": "Xi Gong",
    "title": "Financial Analyst / Management Analytics Candidate",
    "summary": (
        "Financial analyst with internship experience in tax, accounting, reconciliation, "
        "cross-system data work, and stakeholder coordination. Currently pursuing the "
        "Master of Management Analytics at the Rotman School of Management."
    ),
    "email": "george.gong@rotman.utoronto.ca",
    "phone": "(+1) 647-831-4670",
    "linkedin": "www.linkedin.com/in/xi-gong0528"
}

skills_df = pd.DataFrame({
    "Skill": [
        "Python", "R Programming", "SQL", "Excel",
        "Power BI", "SAP", "Blackline", "Financial Analysis", "DCF Modeling"
    ],
    "Category": [
        "Programming", "Programming", "Programming", "Software",
        "Software", "Finance Systems", "Finance Systems", "Finance", "Finance"
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
        "University of Toronto Scarborough"
    ],
    "Location": ["Toronto, ON", "Toronto, ON"],
    "Period": ["Aug 2025 - Present", "Sep 2020 - Jun 2025"],
    "Highlights": [
        "Graduate analytics program",
        "Finance specialist; GPA 3.73/4.00; Dean's List"
    ]
})

experience_df = pd.DataFrame({
    "Company": ["Johnson & Johnson Canada", "Dome Productions"],
    "Role": ["Tax Analyst", "General Accountant"],
    "Period": ["Jan 2024 - Sep 2024", "Aug 2022 - Jun 2023"],
    "Impact Score": [92, 84],
    "Summary": [
        "Analyzed financial and tax data across SAP, Blackline, and LYNX; prepared reports and supported reconciliations.",
        "Handled invoice checks, reconciliation, monthly reporting, and created a 20-page onboarding manual."
    ]
})

leadership_df = pd.DataFrame({
    "Achievement": ["Calian x RBAC Case Competition"],
    "Role": ["Team Leader - 2nd Place"],
    "Period": ["2025"],
    "Details": [
        "Led a 4-person team and used machine learning models including K-means, KNN, Logistic Regression, Random Forest, and XGBoost."
    ]
})

st.sidebar.title("Interactive Controls")

section_choice = st.sidebar.selectbox(
    "Choose a section to highlight",
    ["Overview", "Skills", "Experience", "Education", "Leadership"]
)

min_proficiency = st.sidebar.slider(
    "Minimum skill proficiency",
    min_value=50,
    max_value=100,
    value=70,
    step=5
)

show_programming_only = st.sidebar.checkbox("Show only programming skills", value=False)

selected_company = st.sidebar.selectbox(
    "Filter work experience",
    ["All"] + experience_df["Company"].tolist()
)

show_summary = st.sidebar.checkbox("Show professional summary", value=True)

st.title(f"{profile['name']} | Interactive Resume App")
st.subheader(profile["title"])

c1, c2, c3 = st.columns(3)
c1.metric("Internship Experience", "2 roles")
c2.metric("Undergrad GPA", "3.73 / 4.00")
c3.metric("Competition Result", "2nd Place")

st.markdown(
    f"**Email:** {profile['email']}  \n"
    f"**Phone:** {profile['phone']}  \n"
    f"**LinkedIn:** {profile['linkedin']}"
)

if show_summary:
    st.info(profile["summary"])

st.markdown("---")
st.header(f"Highlighted Section: {section_choice}")

if section_choice == "Overview":
    st.write("This dashboard presents Xi Gong's resume in an interactive format.")
elif section_choice == "Skills":
    st.write("Explore technical, analytical, and finance-related skills.")
elif section_choice == "Experience":
    st.write("Review internship experience and business impact.")
elif section_choice == "Education":
    st.write("View academic background and achievements.")
else:
    st.write("See leadership and competition accomplishments.")

filtered_skills = skills_df[skills_df["Proficiency"] >= min_proficiency].copy()

if show_programming_only:
    filtered_skills = filtered_skills[filtered_skills["Category"] == "Programming"]

st.markdown("---")
st.header("Skills Table")
if filtered_skills.empty:
    st.warning("No skills match the current filters.")
else:
    st.dataframe(filtered_skills, use_container_width=True)

st.header("Skills Proficiency Chart")
if not filtered_skills.empty:
    chart_df = (
        filtered_skills.sort_values("Proficiency", ascending=False)
        .set_index("Skill")[["Proficiency"]]
    )
    st.bar_chart(chart_df)
else:
    st.write("Adjust the controls to display chart data.")

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
        st.write(row["Summary"])

st.markdown("---")
st.header("Education")
st.table(education_df)

st.markdown("---")
st.header("Leadership & Achievements")
st.table(leadership_df)

st.markdown("---")
st.success(
    "This app includes personalized resume content, multiple interactive widgets, "
    "tables, and a chart."
)
