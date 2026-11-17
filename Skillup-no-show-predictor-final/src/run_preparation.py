import pandas as pd
from pathlib import Path
from prepare_data import clean_appointments

project_dir = Path(__file__).resolve().parents[1]

raw_file = project_dir / "data" / "raw" / "appointments.csv"
processed_dir = project_dir / "data" / "processed"
output_file = processed_dir / "cleaned_appointments.csv"

try:
    if not raw_file.exists():
        raise FileNotFoundError(
            f"Input file not found: {raw_file}"
        )

    appointments = pd.read_csv(raw_file)
    cleaned = clean_appointments(appointments)

    processed_dir.mkdir(parents=True, exist_ok=True)
    cleaned.to_csv(output_file, index=False)

    print("Data preparation completed successfully!")
    print(f"Input records: {len(appointments)}")
    print(f"Cleaned records: {len(cleaned)}")
    print(f"Output saved to: {output_file}")

except (ValueError, FileNotFoundError) as error:
    print(f"Data preparation failed: {error}")
