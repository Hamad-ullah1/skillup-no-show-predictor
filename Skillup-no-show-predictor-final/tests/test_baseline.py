import sys
from pathlib import Path
import pandas as pd
import pytest

# Make src importable
project_dir = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_dir / "src"))

from baseline import evaluate_baseline


def test_majority_baseline_accuracy_and_no_show_recall():
    df = pd.DataFrame({
        "booking_lead_days": range(100),
        "previous_no_shows": [0] * 100,
        "reminder_sent": [1] * 100,
        "attended": [1] * 90 + [0] * 10
    })

    results = evaluate_baseline(df)

    assert results["accuracy"] == 0.90
    assert results["no_show_recall"] == 0.0
    assert results["train_records"] == 80
    assert results["test_records"] == 20


def test_missing_attended_column():
    df = pd.DataFrame({
        "booking_lead_days": [1, 2, 3],
        "previous_no_shows": [0, 0, 1],
        "reminder_sent": [1, 1, 0]
    })

    with pytest.raises(ValueError, match="Missing required column"):
        evaluate_baseline(df)


def test_empty_dataframe():
    df = pd.DataFrame()

    with pytest.raises(ValueError, match="Input dataframe is empty"):
        evaluate_baseline(df)
