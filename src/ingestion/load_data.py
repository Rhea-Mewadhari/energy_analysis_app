import pandas as pd


def load_datasets(
    employee_path="data/raw/question1_2_employee_survey_data.csv",
    company_path="data/raw/question1_company_retention_data.csv"
):
    # Load datasets
    employee_df = pd.read_csv(employee_path)
    company_df = pd.read_csv(company_path)

    print("✅ Datasets Loaded")

    # -----------------------------
    # Employee Data Checks
    # -----------------------------
    print("\n📊 Employee Dataset")
    print(f"Shape: {employee_df.shape}")

    print("\nMissing values:")
    print(employee_df.isnull().sum())

    print("\nSample:")
    print(employee_df.head())

    # -----------------------------
    # Company Data Checks
    # -----------------------------
    print("\n📊 Company Dataset")
    print(f"Shape: {company_df.shape}")

    print("\nMissing values:")
    print(company_df.isnull().sum())

    print("\nSample:")
    print(company_df.head())

    return employee_df, company_df


if __name__ == "__main__":
    employee_df, company_df = load_datasets()