# 🚀 Locust Load Testing with GitHub Actions

Automate API stress testing using Locust and GitHub Actions.

---

## 📌 Project Overview

This project demonstrates how to perform automated load testing using **Locust** and integrate it into a **GitHub Actions CI/CD pipeline**.

Whenever code is pushed to the `main` branch, GitHub Actions automatically:

* Sets up the Python environment
* Installs Locust dependencies
* Executes a headless Locust stress test
* Generates performance reports in CSV format
* Uploads the reports as workflow artifacts

The tests target the public JSONPlaceholder API to simulate realistic API workloads.

---

## 🏗️ Project Structure

```text
Locust-test-main/
├── .github/
│   └── workflows/
│       └── locust-test.yml
├── locustfile.py
└── requirements.txt
```

---

## ⚙️ Technologies Used

* Python 3.13
* Locust 2.42.2
* GitHub Actions
* JSONPlaceholder API

---

## 🧪 Load Testing Scenario

The Locust users perform two different tasks:

### 1. Fetch Posts

Sends GET requests to:

```http
GET /posts
```

Purpose:

* Simulate users browsing content.
* Measure API response performance under load.

---

### 2. Create Posts

Sends POST requests to:

```http
POST /posts
```

Payload:

```json
{
  "title": "bikramtest",
  "body": "testbody",
  "userId": 1
}
```

Purpose:

* Simulate write operations.
* Evaluate API behavior during concurrent submissions.

---

## 📄 Locust Configuration

The test configuration used in GitHub Actions:

| Parameter  | Value                                |
| ---------- | ------------------------------------ |
| Users      | 1000                                 |
| Spawn Rate | 100 users/sec                        |
| Duration   | 2 minutes                            |
| Host       | https://jsonplaceholder.typicode.com |
| Mode       | Headless                             |
| Reports    | CSV                                  |

Equivalent command:

```bash
locust -f locustfile.py \
--headless \
-u 1000 \
-r 100 \
--run-time 2m \
-H https://jsonplaceholder.typicode.com \
--csv=locust_report
```

---

## ⚡ GitHub Actions Workflow

The CI pipeline performs the following steps:

### Checkout Repository

```yaml
uses: actions/checkout@v5
```

### Setup Python

```yaml
uses: actions/setup-python@v6
```

Python Version:

```yaml
3.13
```

### Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Execute Load Test

Runs the Locust stress test in headless mode.

### Upload Reports

Generated CSV files are preserved as workflow artifacts for later analysis.

Artifacts uploaded:

```text
locust_report_*.csv
```

---

## 📊 Generated Reports

Locust generates multiple CSV reports, including:

### Statistics Report

```text
locust_report_stats.csv
```

Contains:

* Request counts
* Failure counts
* Average response times
* Minimum and maximum latency
* Percentiles

---

### Failures Report

```text
locust_report_failures.csv
```

Contains:

* Failed requests
* Error details
* Failure frequency

---

### History Report

```text
locust_report_stats_history.csv
```

Contains:

* Historical performance metrics over time
* Throughput trends
* Response time evolution

---

## ▶️ Running Locally

### Clone Repository

```bash
git clone https://github.com/<your-username>/Locust-test.git
cd Locust-test
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run Stress Test

```bash
locust -f locustfile.py \
--headless \
-u 1000 \
-r 100 \
--run-time 2m \
-H https://jsonplaceholder.typicode.com \
--csv=locust_report
```

---

## 🔍 Learning Outcomes

This project demonstrates:

* Writing Locust user behaviors
* Simulating concurrent API users
* Performing GET and POST load testing
* Running headless Locust tests
* Integrating performance testing into CI/CD pipelines
* Generating automated performance reports
* Uploading artifacts through GitHub Actions

---

## 🚀 Future Enhancements

Potential improvements include:

* Scheduled nightly stress tests
* Slack or email notifications
* Threshold-based pipeline failures
* HTML performance report generation
* Multi-environment testing
* Integration with Grafana dashboards
* Performance trend analysis over time

---

# 👨‍💻 Author

**Bikramjit Roy**

DevOps & Cloud Engineering Enthusiast passionate about automation, CI/CD, cloud-native practices, and building reliable software delivery pipelines.

GitHub:
https://github.com/Bikramjit2212

---

## ⭐ If you found this project useful, consider giving it a star.
