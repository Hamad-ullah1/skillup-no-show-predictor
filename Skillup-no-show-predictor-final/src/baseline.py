
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, recall_score


def evaluate_baseline(df):
    X = df.drop(columns=["attended"])
    y = df["attended"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    model = DummyClassifier(strategy="most_frequent")
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    no_show_recall = recall_score(
        y_test,
        predictions,
        pos_label=0,
        zero_division=0
    )

    return {
        "accuracy": accuracy,
        "no_show_recall": no_show_recall,
        "train_records": len(X_train),
        "test_records": len(X_test),
    }


if __name__ == "__main__":
    project_dir = Path(__file__).resolve().parents[1]
    data_file = project_dir / "data" / "processed" / "cleaned_appointments.csv"

    df = pd.read_csv(data_file)
    results = evaluate_baseline(df)

    print("=== SkillUp Academy: Baseline Results ===")
    print(f"Total records: {len(df)}")
    print(f"Training records: {results['train_records']}")
    print(f"Testing records: {results['test_records']}")
    print(f"Accuracy: {results['accuracy']:.2%}")
    print(f"No-show recall: {results['no_show_recall']:.2%}")
