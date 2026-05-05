import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from src.ingestion.load_data import load_datasets

sns.set(style="whitegrid")


# -----------------------------
# RQ1: Remote Access vs Leaving
# -----------------------------
def plot_remote_vs_leave(df):
    plt.figure()

    plot_df = df.copy()
    plot_df["intention_to_leave_numeric"] = plot_df["intention_to_leave"].map({"Yes": 1, "No": 0})

    sns.regplot(
        x="remote_access_score",
        y="intention_to_leave_numeric",
        data=plot_df,
        logistic=True
    )

    plt.title("Remote Access vs Probability of Leaving")
    plt.xlabel("Remote Access Score")
    plt.ylabel("Probability of Leaving")

    plt.savefig("outputs/charts/rq1_remote_vs_leave.png")
    plt.close()


# -----------------------------
# RQ2: Work-Life Balance by Policy
# -----------------------------
def plot_wlb_by_policy(df):
    plt.figure()

    sns.boxplot(
        x="remote_policy",
        y="work_life_balance_score",
        data=df
    )

    plt.title("Work-Life Balance Across Remote Policies")
    plt.xlabel("Remote Policy")
    plt.ylabel("Work-Life Balance Score")

    plt.savefig("outputs/charts/rq2_wlb.png")
    plt.close()


# -----------------------------
# RQ3: Salary Gap vs Retention
# -----------------------------
def plot_salary_gap(df):
    plt.figure()

    sns.regplot(
        x="salary_gap_percent",
        y="long_term_stay_intention_score",
        data=df
    )

    plt.title("Salary Gap vs Long-Term Retention")
    plt.xlabel("Salary Gap (%)")
    plt.ylabel("Stay Intention Score")

    plt.savefig("outputs/charts/rq3_salary_gap.png")
    plt.close()


# -----------------------------
# RQ4: Engagement by Policy
# -----------------------------
def plot_engagement(df):
    plt.figure()

    sns.boxplot(
        x="remote_policy",
        y="engagement_score",
        data=df
    )

    plt.title("Engagement Across Remote Policies")
    plt.xlabel("Remote Policy")
    plt.ylabel("Engagement Score")

    plt.savefig("outputs/charts/rq4_engagement.png")
    plt.close()


# -----------------------------
# RUN ALL
# -----------------------------
if __name__ == "__main__":
    employee_df, _ = load_datasets()

    plot_remote_vs_leave(employee_df)
    plot_wlb_by_policy(employee_df)
    plot_salary_gap(employee_df)
    plot_engagement(employee_df)

    print("✅ Charts generated")