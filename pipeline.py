import os
import subprocess
import time
from datetime import datetime
import csv

LOG_FILE = "logs/pipeline.log"
METRICS_FILE = "logs/metrics.csv"

def log_message(stage, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{stage}] {message}\n"
    print(log_entry.strip())
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)

def simulate_commit():
    log_message("GIT", "Simulating code commit...")
    subprocess.run(["git", "add", "."], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["git", "commit", "-m", "Automated commit for demo"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    log_message("GIT", "Code committed successfully.")

def build_stage():
    log_message("BUILD", "Starting build process...")
    start = time.time()
    time.sleep(2)  
    duration = round(time.time() - start, 2)
    log_message("BUILD", f"Build completed successfully in {duration}s.")
    return duration

def test_stage():
    log_message("TEST", "Running tests...")
    start = time.time()
    result = subprocess.run(["python", "-m", "unittest", "discover", "-s", ".", "-p", "test_*.py"], capture_output=True, text=True)
    duration = round(time.time() - start, 2)

    if result.returncode == 0:
        log_message("TEST", f"All tests passed in {duration}s.")
    else:
        log_message("TEST", f"Tests failed in {duration}s:\n{result.stdout}\n{result.stderr}")
    return duration

def deploy_stage():
    log_message("DEPLOY", "Starting deployment simulation...")
    start = time.time()
    time.sleep(2)
    duration = round(time.time() - start, 2)
    log_message("DEPLOY", f"Application deployed successfully in {duration}s.")
    return duration

def save_metrics(run_time, build_time, test_time, deploy_time):
    os.makedirs("logs", exist_ok=True)
    file_exists = os.path.isfile(METRICS_FILE)
    with open(METRICS_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Timestamp", "BuildTime", "TestTime", "DeployTime", "TotalTime"])
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), build_time, test_time, deploy_time, run_time])

if __name__ == "__main__":
    os.makedirs("logs", exist_ok=True)
    start_time = time.time()

    log_message("PIPELINE", "=== CI/CD Pipeline Run Started ===")
    simulate_commit()
    build_time = build_stage()
    test_time = test_stage()
    deploy_time = deploy_stage()

    total_time = round(time.time() - start_time, 2)
    save_metrics(total_time, build_time, test_time, deploy_time)
    log_message("SUMMARY", f"Pipeline completed in {total_time}s.")
    log_message("PIPELINE", "=== CI/CD Pipeline Run Finished ===")
