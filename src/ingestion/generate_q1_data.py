import os
import numpy as np
import pandas as pd

np.random.seed(42)

OUTPUT_DIR = "data/raw"
os.makedirs(OUTPUT_DIR, exist_ok=True)

N_EMPLOYEES = 300


def clamp(values, min_value=1, max_value=5):
    return np.clip(values, min_value, max_value)


def generate_employee_data():
    roles = ["Engineer", "Project Manager", "Energy Analyst", "Research Specialist"]
    skill_levels = ["Mid", "Senior", "Expert"]

    remote_policy = np.random.choice(
        ["Full Remote", "Hybrid", "Mostly On-site"],
        size=N_EMPLOYEES,
        p=[0.30, 0.40, 0.30]
    )

    data = []

    for i in range(N_EMPLOYEES):
        policy = remote_policy[i]

        role = np.random.choice(roles)
        skill_level = np.random.choice(skill_levels, p=[0.35, 0.45, 0.20])

        gender = np.random.choice(
            ["Female", "Male", "Other/Prefer not to say"],
            p=[0.42, 0.55, 0.03]
        )

        age_group = np.random.choice(
            ["20-29", "30-39", "40-49", "50+"],
            p=[0.28, 0.38, 0.24, 0.10]
        )

        job_level = np.random.choice(
            ["Junior", "Mid", "Senior", "Manager", "Executive"],
            p=[0.15, 0.35, 0.30, 0.15, 0.05]
        )

        company_scope = (
            "International"
            if policy == "Full Remote"
            else np.random.choice(["Local", "International"], p=[0.75, 0.25])
        )

        work_location = np.random.choice(
            ["Lithuania", "Outside Lithuania"],
            p=[0.88, 0.12]
        )

        if policy == "Full Remote":
            remote_score = np.random.normal(4.5, 0.5)
            turnover_probability = 0.12
            daily_hours = np.random.normal(8.4, 0.8)
            commute_time = np.random.normal(5, 5)
            flexibility_score = np.random.normal(4.6, 0.4)
            stress_score = np.random.normal(2.4, 0.7)
        elif policy == "Hybrid":
            remote_score = np.random.normal(3.5, 0.6)
            turnover_probability = 0.18
            daily_hours = np.random.normal(8.2, 0.7)
            commute_time = np.random.normal(25, 12)
            flexibility_score = np.random.normal(3.8, 0.6)
            stress_score = np.random.normal(2.8, 0.7)
        else:
            remote_score = np.random.normal(2.0, 0.7)
            turnover_probability = 0.30
            daily_hours = np.random.normal(8.6, 0.9)
            commute_time = np.random.normal(45, 18)
            flexibility_score = np.random.normal(2.1, 0.7)
            stress_score = np.random.normal(3.6, 0.8)

        compensation_score = np.random.normal(3.2, 0.9)
        career_score = np.random.normal(3.0, 0.8)

        work_life_balance = (
            0.45 * remote_score
            + 0.35 * flexibility_score
            + 0.20 * (6 - stress_score)
            + np.random.normal(0, 0.5)
        )

        if policy == "Full Remote":
            belonging = np.random.normal(3.0, 0.8)
            cohesion = np.random.normal(3.1, 0.7)
            values_alignment = np.random.normal(3.2, 0.7)
            engagement = np.random.normal(3.3, 0.7)
        elif policy == "Hybrid":
            belonging = np.random.normal(3.8, 0.6)
            cohesion = np.random.normal(3.9, 0.6)
            values_alignment = np.random.normal(3.7, 0.6)
            engagement = np.random.normal(3.8, 0.6)
        else:
            belonging = np.random.normal(3.6, 0.7)
            cohesion = np.random.normal(3.7, 0.6)
            values_alignment = np.random.normal(3.5, 0.7)
            engagement = np.random.normal(3.6, 0.7)

        manager_support = np.random.normal(3.5, 0.7)
        communication_effectiveness = np.random.normal(3.6, 0.7)

        # engagement boosted by good leadership even in remote
        engagement = (
            0.4 * engagement
            + 0.3 * manager_support
            + 0.3 * communication_effectiveness
            + np.random.normal(0, 0.3)
        )

        participates_in_events = "Yes" if np.random.random() < 0.65 else "No"
        uses_tools = "Yes" if np.random.random() < 0.75 else "No"

        family_life_impact = (
            0.60 * flexibility_score
            + 0.40 * (6 - stress_score)
            + np.random.normal(0, 0.4)
        )

        base_salary_by_level = {
            "Junior": 1800,
            "Mid": 2800,
            "Senior": 4200,
            "Manager": 5200,
            "Executive": 7000
        }

        role_salary_adjustment = {
            "Engineer": 1.10,
            "Project Manager": 1.15,
            "Energy Analyst": 1.00,
            "Research Specialist": 1.05
        }

        current_salary = (
            base_salary_by_level[job_level]
            * role_salary_adjustment[role]
            * np.random.normal(1.0, 0.12)
        )

        if company_scope == "International":
            international_offer_salary = current_salary * np.random.normal(1.20, 0.10)
            benefits_satisfaction = np.random.normal(4.0, 0.6)
            health_benefits = np.random.normal(4.1, 0.5)
            pension_benefits = np.random.normal(3.8, 0.6)
            bonus_satisfaction = np.random.normal(3.9, 0.7)
            training_budget = np.random.normal(4.2, 0.5)
            perceived_pay_advantage = np.random.normal(3.7, 0.7)
        else:
            international_offer_salary = current_salary * np.random.normal(1.40, 0.15)
            benefits_satisfaction = np.random.normal(3.2, 0.8)
            health_benefits = np.random.normal(3.4, 0.7)
            pension_benefits = np.random.normal(3.5, 0.7)
            bonus_satisfaction = np.random.normal(2.9, 0.8)
            training_budget = np.random.normal(3.0, 0.8)
            perceived_pay_advantage = np.random.normal(4.3, 0.6)

        expected_salary = current_salary * np.random.normal(1.15, 0.10)
        salary_gap = international_offer_salary - current_salary
        salary_gap_percent = (salary_gap / current_salary) * 100

        long_term_stay_intention = (
            2.0
            + 0.35 * compensation_score
            + 0.25 * benefits_satisfaction
            + 0.20 * career_score
            + 0.15 * work_life_balance
            - 0.02 * salary_gap_percent
            + np.random.normal(0, 0.5)
        )

        weekly_hours = daily_hours * 5
        overtime_hours = max(0, weekly_hours - 40)

        tenure_years = {
            "Full Remote": np.random.normal(4.5, 1.4),
            "Hybrid": np.random.normal(4.2, 1.3),
            "Mostly On-site": np.random.normal(3.1, 1.2)
        }[policy]

        tenure_years = max(float(tenure_years), 0.3)

        if tenure_years < 1:
            tenure_level = "<1 year"
        elif tenure_years < 4:
            tenure_level = "1-3 years"
        elif tenure_years < 7:
            tenure_level = "4-6 years"
        else:
            tenure_level = "7+ years"

        intention_score = (
            6.5
            - 0.75 * remote_score
            - 0.45 * compensation_score
            - 0.35 * career_score
            + np.random.normal(0, 0.8)
        )

        intention_to_leave = "Yes" if intention_score > 2.8 else "No"

        actual_turnover = (
            "Left"
            if np.random.random() < turnover_probability
            else "Stayed"
        )

        joined_remote_company = (
            "Yes"
            if actual_turnover == "Left" and np.random.random() < 0.62
            else "No"
        )

        promotion_received = (
            "Yes"
            if np.random.random() < {
                "Full Remote": 0.12,
                "Hybrid": 0.15,
                "Mostly On-site": 0.08
            }[policy]
            else "No"
        )

        salary_increase_received = (
            "Yes"
            if np.random.random() < {
                "Full Remote": 0.56,
                "Hybrid": 0.64,
                "Mostly On-site": 0.50
            }[policy]
            else "No"
        )

        data.append({
            "employee_id": f"EMP{i + 1:03d}",
            "role": role,
            "skill_level": skill_level,
            "gender": gender,
            "age_group": age_group,
            "job_level": job_level,
            "company_scope": company_scope,
            "work_location": work_location,
            "remote_policy": policy,
            "remote_access_score": round(float(clamp(remote_score)), 1),
            "remote_flexibility_score": round(float(clamp(flexibility_score)), 1),
            "compensation_satisfaction": round(float(clamp(compensation_score)), 1),
            "career_growth_score": round(float(clamp(career_score)), 1),
            "work_life_balance_score": round(float(clamp(work_life_balance)), 1),
            "sense_of_belonging_score": round(float(clamp(belonging)), 1),
            "team_cohesion_score": round(float(clamp(cohesion)), 1),
            "values_alignment_score": round(float(clamp(values_alignment)), 1),
            "engagement_score": round(float(clamp(engagement)), 1),
            "manager_support_score": round(float(clamp(manager_support)), 1),
            "communication_effectiveness": round(float(clamp(communication_effectiveness)), 1),
            "participates_in_team_events": participates_in_events,
            "uses_collab_tools_frequently": uses_tools,
            "stress_level_score": round(float(clamp(stress_score)), 1),
            "family_life_impact_score": round(float(clamp(family_life_impact)), 1),
            "daily_work_hours": round(max(float(daily_hours), 6), 1),
            "weekly_work_hours": round(max(float(weekly_hours), 30), 1),
            "overtime_hours_weekly": round(float(overtime_hours), 1),
            "commute_time_minutes": round(max(float(commute_time), 0), 0),
            "promotion_received": promotion_received,
            "salary_increase_received": salary_increase_received,
            "tenure_years": round(tenure_years, 1),
            "tenure_level": tenure_level,
            "intention_to_leave": intention_to_leave,
            "actual_turnover": actual_turnover,
            "joined_remote_company": joined_remote_company,
            "current_monthly_salary_eur": round(float(current_salary), 2),
            "expected_monthly_salary_eur": round(float(expected_salary), 2),
            "international_offer_salary_eur": round(float(international_offer_salary), 2),
            "salary_gap_eur": round(float(salary_gap), 2),
            "salary_gap_percent": round(float(salary_gap_percent), 1),
            "benefits_satisfaction_score": round(float(clamp(benefits_satisfaction)), 1),
            "health_benefits_score": round(float(clamp(health_benefits)), 1),
            "pension_benefits_score": round(float(clamp(pension_benefits)), 1),
            "bonus_satisfaction_score": round(float(clamp(bonus_satisfaction)), 1),
            "training_budget_satisfaction": round(float(clamp(training_budget)), 1),
            "perceived_international_pay_advantage": round(float(clamp(perceived_pay_advantage)), 1),
            "long_term_stay_intention_score": round(float(clamp(long_term_stay_intention)), 1)
        })

    return pd.DataFrame(data)


def generate_company_data():
    companies = [
        ("C001", "Nordic Green Energy", "International Energy", "Full Remote"),
        ("C002", "Baltic Renewables", "International Energy", "Full Remote"),
        ("C003", "EnerTech Global", "Tech-Energy", "Full Remote"),
        ("C004", "Energija Lietuva", "Local Energy", "Hybrid"),
        ("C005", "Vilnius Grid Systems", "Local Energy", "Hybrid"),
        ("C006", "Lithuanian Solar Works", "Local Energy", "Hybrid"),
        ("C007", "Kaunas Infrastructure Energy", "Local Energy", "Mostly On-site"),
        ("C008", "Baltic Thermal Power", "Local Energy", "Mostly On-site"),
        ("C009", "RenewGrid Europe", "International Energy", "Hybrid"),
        ("C010", "FutureWind Analytics", "Tech-Energy", "Full Remote"),
    ]

    rows = []

    for company_id, name, company_type, policy in companies:
        if policy == "Full Remote":
            turnover = np.random.normal(0.11, 0.02)
            promotion = np.random.normal(0.12, 0.02)
            tenure = np.random.normal(4.6, 0.5)
            raise_rate = np.random.normal(0.56, 0.04)
        elif policy == "Hybrid":
            turnover = np.random.normal(0.16, 0.03)
            promotion = np.random.normal(0.15, 0.03)
            tenure = np.random.normal(4.2, 0.5)
            raise_rate = np.random.normal(0.64, 0.04)
        else:
            turnover = np.random.normal(0.24, 0.04)
            promotion = np.random.normal(0.08, 0.02)
            tenure = np.random.normal(3.1, 0.4)
            raise_rate = np.random.normal(0.50, 0.05)

        rows.append({
            "company_id": company_id,
            "company_name": name,
            "company_type": company_type,
            "remote_policy": policy,
            "annual_turnover_rate": round(turnover * 100, 1),
            "promotion_rate": round(promotion * 100, 1),
            "average_tenure_years": round(tenure, 1),
            "raise_frequency_rate": round(raise_rate * 100, 1),
            "new_employees_2024": np.random.randint(20, 90),
            "new_remote_employees_2024": (
                np.random.randint(10, 70)
                if policy != "Mostly On-site"
                else np.random.randint(0, 15)
            )
        })

    return pd.DataFrame(rows)


if __name__ == "__main__":
    employee_df = generate_employee_data()
    company_df = generate_company_data()

    employee_df.to_csv(
        f"{OUTPUT_DIR}/question1_2_employee_survey_data.csv",
        index=False
    )

    company_df.to_csv(
        f"{OUTPUT_DIR}/question1_company_retention_data.csv",
        index=False
    )

    print("Fake data generated successfully.")
    print(f"Employee rows: {len(employee_df)}")
    print(f"Company rows: {len(company_df)}")