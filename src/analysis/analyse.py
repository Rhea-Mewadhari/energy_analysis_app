import pandas as pd
import statsmodels.api as sm
from scipy import stats

from src.ingestion.load_data import load_datasets


# -----------------------------
# DESCRIPTIVE STATS
# -----------------------------
def descriptive_stats(df):
    print("\n📊 DESCRIPTIVE STATISTICS")
    print(df.describe())


# -----------------------------
# RQ1: Remote Work vs Retention
# -----------------------------
def rq1_regression(df):
    print("\n📉 RQ1: Turnover Drivers (Employee Level)")

    X = df[[
        "remote_access_score",
        "compensation_satisfaction",
        "career_growth_score",
        "work_life_balance_score"
    ]]

    y = df["intention_to_leave"].map({"Yes": 1, "No": 0})

    X = sm.add_constant(X)

    model = sm.OLS(y, X).fit()
    print(model.summary())


# -----------------------------
# RQ1 (Company-Level Validation)
# -----------------------------
def rq1_company_analysis(company_df):
    print("\n🏢 RQ1: Company-Level Retention Analysis")

    X = company_df[["promotion_rate", "raise_frequency_rate"]]
    y = company_df["annual_turnover_rate"]

    X = sm.add_constant(X)

    model = sm.OLS(y, X).fit()
    print(model.summary())


# -----------------------------
# RQ2: Work-Life Balance
# -----------------------------
def rq2_anova(df):
    print("\n📊 RQ2: Work-Life Balance by Remote Policy")

    groups = df.groupby("remote_policy")["work_life_balance_score"].apply(list)

    f_stat, p_value = stats.f_oneway(*groups)

    print(f"F-statistic: {f_stat}")
    print(f"P-value: {p_value}")


# -----------------------------
# RQ3: Salary Gap vs Retention
# -----------------------------
def rq3_regression(df):
    print("\n📉 RQ3: Salary Gap Impact")

    X = df[[
        "salary_gap_percent",
        "benefits_satisfaction_score",
        "bonus_satisfaction_score"
    ]]

    y = df["long_term_stay_intention_score"]

    X = sm.add_constant(X)

    model = sm.OLS(y, X).fit()
    print(model.summary())


# -----------------------------
# RQ4: Culture & Engagement
# -----------------------------
def rq4_anova(df):
    print("\n📊 RQ4: Engagement by Remote Policy")

    groups = df.groupby("remote_policy")["engagement_score"].apply(list)

    f_stat, p_value = stats.f_oneway(*groups)

    print(f"F-statistic: {f_stat}")
    print(f"P-value: {p_value}")


# -----------------------------
# BONUS
# -----------------------------
def correlation_matrix(df):
    print("\n📊 Correlation Matrix (Key Variables)")

    corr_df = df.copy()

    corr_df["intention_to_leave_binary"] = corr_df["intention_to_leave"].map({
        "Yes": 1,
        "No": 0
    })

    cols = [
        "remote_access_score",
        "work_life_balance_score",
        "stress_level_score",
        "salary_gap_percent",
        "engagement_score",
        "intention_to_leave_binary"
    ]

    corr = corr_df[cols].corr()

    print(corr)


# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
    employee_df, company_df = load_datasets()

    descriptive_stats(employee_df)

    rq1_regression(employee_df)
    rq1_company_analysis(company_df)

    rq2_anova(employee_df)
    rq3_regression(employee_df)
    rq4_anova(employee_df)

    correlation_matrix(employee_df)