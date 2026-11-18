# SkillUp Academy — Appointment No-Show Predictor

## Project Overview

This project prepares appointment data for a future machine learning model that will predict whether a student is likely to miss an appointment at SkillUp Academy.

The current stage focuses on data preparation, data validation, cleaning, and automated testing. It does not yet contain a trained prediction model.

## Dataset

The project uses 500 fictional appointment records created for development and testing.

The dataset includes:

- Appointment ID
- Student name
- Course
- Appointment type
- Appointment date
- Booking lead days
- Previous no-shows
- Whether a reminder was sent
- Attendance outcome

The sample data is synthetic and does not represent real academy attendance patterns.

## Project Structure

```text
skillup-no-show-predictor/
├── data/
│   ├── raw/
│   │   └── appointments.csv
│   └── processed/
│       └── cleaned_appointments.csv
├── src/
│   ├── prepare_data.py
│   └── run_preparation.py
├── tests/
│   └── test_data.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.10 or later
- pandas
- numpy
- pytest

## Installation

From the project directory, run:

`pip install -r requirements.txt`

## Run Data Preparation

`python src/run_preparation.py`

The script reads the raw appointment CSV, cleans and validates the records, and saves the result in `data/processed/cleaned_appointments.csv`.

## Run Tests

`python -m pytest -v`

The tests cover:

1. Normal data cleaning.
2. Missing-value handling.
3. Empty dataset handling.
4. Missing required columns.

## Data Quality and Validation

The cleaning pipeline checks required columns, removes duplicate records, handles missing values, converts dates and numeric columns, and rejects invalid values.

Invalid or empty input is handled with clear error messages.

## Performance and Security

Performance was checked using the original 500 records and a larger 10,000-record test dataset.

Basic privacy checks and a `.gitignore` file help prevent accidental publication of private files and credentials.

Only fictional sample data should be published. Never upload real student records, passwords, API keys, or confidential information.

## Current Project Status

Completed:

- Synthetic sample dataset creation.
- Data inspection and cleaning.
- Reusable data preparation module.
- Automated tests.
- Basic performance checks.
- Basic security checks.
- Project documentation.

A majority-class baseline model has been developed. A trained machine-learning prediction model will be developed in a later project stage.

## How to Use in Google Colab

1. Open the project notebook in Google Colab.
2. Make sure the project folder is available in the runtime.
3. Install dependencies:

   `!pip install -r skillup-no-show-predictor/requirements.txt`

4. Run the notebook cells in order.
5. Run the tests:

   `!python -m pytest -v skillup-no-show-predictor/tests`

## Disclaimer

This is an educational machine learning preparation project. Its fictional dataset and assumed relationships are not real-world findings or a validated prediction service.


## Task 2: Baseline Model

### Purpose
The baseline provides a simple reference score to compare with future machine-learning models. It uses a majority-class strategy and always predicts the most common attendance outcome.

### Class Imbalance
The synthetic dataset contains 500 appointments:
- Showed up (1): 436 (87.2%)
- No-show (0): 64 (12.8%)

This dataset is imbalanced because the showed-up class is much larger than the no-show class.

Accuracy alone can be misleading. A model that always predicts "showed up" can achieve high accuracy while failing to identify any no-shows.

### Baseline Metrics
- Full-dataset majority-class accuracy: 87.2%.
- No-show recall: 0%.

The baseline catches none of the actual no-shows. No-show recall is therefore important when evaluating future models.

### How to Run the Baseline

Run from the project root:

    python src/baseline.py

### Automated Tests

The project includes 7 automated tests:

- 4 data-preparation tests in `tests/test_data.py`.
- 3 baseline tests in `tests/test_baseline.py`, covering normal evaluation, a missing `attended` column, and an empty dataframe.

Run all tests from the project root:

    python -m pytest -v tests

### Install Dependencies

Run:

    pip install -r requirements.txt

Note: This project uses synthetic sample data. These results do not represent actual SkillUp Academy attendance records.

