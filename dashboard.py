import csv
import matplotlib.pyplot as plt
from datetime import datetime

METRICS_FILE = "logs/metrics.csv"

def read_metrics():
    timestamps, builds, tests, deploys, totals = [], [], [], [], []
    with open(METRICS_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            timestamps.append(datetime.strptime(row["Timestamp"], "%Y-%m-%d %H:%M:%S"))
            builds.append(float(row["BuildTime"]))
            tests.append(float(row["TestTime"]))
            deploys.append(float(row["DeployTime"]))
            totals.append(float(row["TotalTime"]))
    return timestamps, builds, tests, deploys, totals

def plot_metrics():
    timestamps, builds, tests, deploys, totals = read_metrics()

    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, builds, marker='o', label='Build Time (s)')
    plt.plot(timestamps, tests, marker='o', label='Test Time (s)')
    plt.plot(timestamps, deploys, marker='o', label='Deploy Time (s)')
    plt.plot(timestamps, totals, marker='o', label='Total Pipeline Time (s)', linewidth=2)

    plt.title("CI/CD Pipeline Observability Dashboard")
    plt.xlabel("Pipeline Run Timestamp")
    plt.ylabel("Duration (seconds)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_metrics()
