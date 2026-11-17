
import pandas as pd


def clean_appointments(df):

    """
    Clean and validate SkillUp Academy appointment data.

    Parameters:
        df: Raw appointment DataFrame.

    Returns:
        A cleaned appointment DataFrame.
    """

    # Work on a copy of original data
    df = df.copy()

    # Required columns
    required_columns = [
        "appointment_id",
        "student_name",
        "course",
        "appointment_type",
        "appointment_date",
        "booking_lead_days",
        "previous_no_shows",
        "reminder_sent",
        "attended"
    ]

    # Check required columns
    missing_columns = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    # Reject empty datasets
    if df.empty:
        raise ValueError("The dataset is empty.")

    # Remove exact duplicate rows
    df = df.drop_duplicates()

    # Clean appointment IDs
    df = df.dropna(subset=["appointment_id"])

    df["appointment_id"] = (
        df["appointment_id"].astype(str).str.strip()
    )

    df = df[df["appointment_id"] != ""]

    # Keep only the first record for duplicate IDs
    df = df.drop_duplicates(
        subset=["appointment_id"],
        keep="first"
    )

    # Clean text columns
    text_columns = [
        "student_name",
        "course",
        "appointment_type"
    ]

    for col in text_columns:

        df[col] = (
            df[col].astype("string").str.strip()
        )

        df[col] = df[col].replace("", pd.NA)

    # Convert appointment dates
    df["appointment_date"] = pd.to_datetime(
        df["appointment_date"],
        errors="coerce"
    )

    # Remove records missing essential information
    essential_columns = [
        "student_name",
        "course",
        "appointment_type",
        "appointment_date",
        "attended"
    ]

    df = df.dropna(subset=essential_columns)

    # Convert numerical columns
    numeric_columns = [
        "booking_lead_days",
        "previous_no_shows",
        "reminder_sent",
        "attended"
    ]

    for col in numeric_columns:

        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

    # Attendance is the target.
    # Never guess a missing attendance result.
    df = df.dropna(subset=["attended"])

    # Fill missing numerical input values
    for col in [
        "booking_lead_days",
        "previous_no_shows"
    ]:

        median_value = df[col].median()

        if pd.isna(median_value):
            raise ValueError(
                f"Cannot impute {col}: no valid values."
            )

        df[col] = df[col].fillna(median_value)

    # Fill missing reminder values with the mode
    reminder_mode = df["reminder_sent"].mode()

    if reminder_mode.empty:
        raise ValueError(
            "Cannot determine a valid reminder value."
        )

    df["reminder_sent"] = df["reminder_sent"].fillna(
        reminder_mode.iloc[0]
    )

    # Check valid business rules
    valid_records = (
        (df["booking_lead_days"] >= 0) &
        (df["previous_no_shows"] >= 0) &
        (df["booking_lead_days"] % 1 == 0) &
        (df["previous_no_shows"] % 1 == 0) &
        (df["reminder_sent"].isin([0, 1])) &
        (df["attended"].isin([0, 1]))
    )

    df = df.loc[valid_records].copy()

    # Reject datasets with no valid records
    if df.empty:
        raise ValueError(
            "No valid appointment records remain."
        )

    # Convert numerical columns to integers
    integer_columns = [
        "booking_lead_days",
        "previous_no_shows",
        "reminder_sent",
        "attended"
    ]

    for col in integer_columns:
        df[col] = df[col].astype(int)

    # Return cleaned data
    return df
