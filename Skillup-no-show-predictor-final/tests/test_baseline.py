
import sys
from pathlib import Path
import pandas as pd

# Make src importable
project_dir = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_dir / "src"))

from baseline import evaluate_baseline


def test_majority_baseline_accuracy_and_no_show_recall():
    # Create a small sample with 90 attended and 10 no-show appointments
    df = pd.DataFrame({
        "booking_lead_days": range(100),
        "previous_no_shows": [0] * 100,
        "reminder_sent": [1] * 100,
        "attended": [1] * 90 + [0] * 10
    })

    results = evaluate_baseline(df)

    # The majority class is attended (1)
    assert results["accuracy"] == 0.90

    # The model should catch none of the no-shows
    assert results["no_show_recall"] == 0.0

    assert results["train_records"] == 80
    assert results["test_records"] == 20
