
import sys
from pathlib import Path

import pandas as pd
import pytest

# Make src folder accessible
sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "src")
)

from prepare_data import clean_appointments


# Create sample appointment data for testing
def sample_data():

    return pd.DataFrame({
        "appointment_id": [
            "SKA-0001",
            "SKA-0002",
            "SKA-0003"
        ],
        "student_name": [
            "Ali Khan",
            "Sara Ali",
            "Ahmed Raza"
        ],
        "course": [
            "Python Programming",
            "Data Science",
            "Web Development"
        ],
        "appointment_type": [
            "Demo Class",
            "Course Counseling",
            "Admission Interview"
        ],
        "appointment_date": [
            "2025-12-01",
            "2025-12-02",
            "2025-12-03"
        ],
        "booking_lead_days": [
            3, 5, 2
        ],
        "previous_no_shows": [
            0, 1, 0
        ],
        "reminder_sent": [
            1, 0, 1
        ],
        "attended": [
            1, 0, 1
        ]
    })


# Test 1: Normal data cleaning
def test_normal_data_cleaning():

    df = sample_data()

    result = clean_appointments(df)

    assert len(result) == 3

    assert result["appointment_id"].is_unique

    assert result["attended"].isin([0, 1]).all()


# Test 2: Missing numerical values
def test_missing_value_handling():

    df = sample_data()

    df.loc[0, "booking_lead_days"] = None

    df.loc[1, "previous_no_shows"] = None

    df.loc[2, "reminder_sent"] = None

    result = clean_appointments(df)

    assert result["booking_lead_days"].notna().all()

    assert result["previous_no_shows"].notna().all()

    assert result["reminder_sent"].notna().all()


# Test 3: Empty dataset failure
def test_empty_dataset():

    df = pd.DataFrame()

    with pytest.raises(
        ValueError,
        match="Missing required columns"
    ):

        clean_appointments(df)


# Test 4: Missing required column
def test_missing_required_column():

    df = sample_data()

    df = df.drop(columns=["course"])

    with pytest.raises(
        ValueError,
        match="Missing required columns"
    ):

        clean_appointments(df)
