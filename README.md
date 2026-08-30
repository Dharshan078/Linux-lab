# Linux \& Python Automation Learning Journey

This repository documents my hands-on learning journey toward Linux, Cloud Operations, and Cloud Engineering.

The projects progress from basic Linux/Bash administration to Python automation, JSON processing, REST APIs, and eventually AWS automation with boto3.

\---

## Learning Progress

```text
Linux Commands
      ↓
Bash Scripting
      ↓
Linux Administration Automation
      ↓
Python
      ↓
subprocess
      ↓
psutil
      ↓
Functions \& Modular Programming
      ↓
Files \& JSON
      ↓
REST APIs
      ↓
boto3
      ↓
AWS Automation
```

## Project 01 — Linux Server Health Monitor

**Objective**  
Created a Bash script to collect and display basic Linux server health information directly using Linux commands.

**What I learned**

* Bash scripting basics (`#!/bin/bash`)
* Variables
* Command substitution using `$(command)`
* `echo`, `hostname`, `whoami`, `date`, `uname`, `top`, `free`, `df`, `ps`
* Basic command pipelines
* Using `awk` to extract command output

**Concepts**

* `hostname`, `whoami`, `date`, `uname -r`, `top`, `free -h`, `df -h`, `ps aux`

## Project 02 — Linux User Management Automation

**Objective**  
Created Bash scripts to automate Linux user creation and deletion. Two separate scripts were created:

1. User creation
2. User deletion

**What I learned**

* `if / else`, `while` loops, `break`, `read -p`
* Variables (`$EUID`)
* Root privilege checking (`sudo`)
* Exit codes (`exit 1`)
* Checking whether a user exists (`id username`)
* Redirecting output using `\&>/dev/null`
* `useradd -m`, `passwd`, `userdel -r`
* Quoting variables
* Confirmation before destructive operations

**Important concept**

```bash
if \[\[ "$EUID" -ne 0 ]]; then
    echo "This script must be run as root."
    exit 1
fi
```

*EUID = 0 means the script is running with root privileges.*

## Project 03 — Python + Linux Commands

**Objective**  
Started using Python to interact with Linux commands.

**What I learned**

* Python basics
* `import`, `subprocess`, `subprocess.run()`, `capture\_output=True`, `text=True`
* Executing Linux commands from Python
* Difference between Python code and Linux commands

**Example**

```python
import subprocess
result = subprocess.run(
    \["hostname"],
    capture\_output=True,
    text=True
)
print(result.stdout)
```

*This project introduced Python as an automation tool for Linux.*

## Project 04 — Python Linux Health Monitor

**Objective**  
Rebuilt the Linux health monitoring script using Python. The project evolved through multiple versions.

* **Version 1:** Used `subprocess` to execute Linux commands from Python.
* **Version 1.2:** Introduced functions to avoid repeatedly writing `subprocess.run()` logic.
* **Version 2.x:** Rebuilt the monitoring functionality using `psutil`. This allowed the script to use Python APIs instead of depending directly on Linux commands.

**What I learned**

**System Information**

* Hostname, Boot time, Uptime
* `socket`, `datetime`, `time`

**CPU**

* CPU utilization, Physical CPU cores, Logical CPU cores, Per-CPU utilization
* `psutil.cpu\_percent()`, `psutil.cpu\_count(logical=False)`, `psutil.cpu\_count(logical=True)`

**Memory**

* `psutil.virtual\_memory()`
* Learned to retrieve: Total memory, Used memory, Available memory, Memory utilization

**Disk**

* `psutil.disk\_usage("/")`, `psutil.disk\_partitions()`
* Learned: Total disk, Used disk, Free disk, Disk utilization, Partitions, Mount points, Filesystems

**Network**

* `psutil.net\_io\_counters(pernic=True)`, `psutil.net\_if\_addrs()`
* Learned: Network interfaces, Bytes sent, Bytes received, Packets, Errors, Drops, IP/MAC/interface information

**Processes**

* `psutil.process\_iter()`
* Learned: Process ID, Process name, CPU utilization, Memory utilization, Lists, Sorting, `lambda`, Selecting the top processes

**Python Functions**

* Defining functions, Parameters, Return values, Calling functions, Helper functions, Modular programming

**Important pattern:**  
`Function` → `Collect data` → `return` → `main()` → `organize/process data` → `print report`

**Error Handling**

* `try: ... except: ...`
* Specific exceptions such as `OSError`

**Logging**

* Learned Python's `logging` module to record execution status and errors in a log file.

**Main Guard**

```python
if \_\_name\_\_ == "\_\_main\_\_":
    main()
```

## Project 05 — Python File \& JSON Operations

**Objective**  
Learned how Python reads files, writes files, and works with structured JSON data.

**File Operations**

* `with open("file.txt", "r") as file:`
* `with open("file.txt", "w") as file:`

**Reading**

* `file.read()`: Reads the complete file as a string.
* `file.readlines()`: Returns lines as a list.
* `for line in file:`: Processes the file one line at a time.

**String Processing**

* `split()`, `strip()`
* Used these to process data read from files.

**JSON**  
Learned how to work with structured JSON data.

**JSON → Python**

* `data = json.load(file)`
* Converts JSON into Python data structures such as dictionaries and lists.

**Python → JSON**

* `json.dump(data, file)`
* Writes Python data into a JSON file.
* Also learned: `json.dump(data, file, indent=4)` for human-readable JSON.

**Nested Dictionaries**

* Learned how to access nested JSON data: `data\["server-1"]\["hostname"]`

**JSON Processing**  
Built a small server inventory program that:

* Reads multiple servers from JSON
* Loops through server records
* Extracts nested values
* Checks server status
* Counts running servers
* Stores stopped servers in a list

**Error Handling**

* `FileNotFoundError`, `json.JSONDecodeError`

## Project 06 — Python REST API

**Objective**  
Learned how Python communicates with external APIs and processes JSON responses.

**Library**

```python
import requests
```

**GET Request**

```python
response = requests.get(url)
```

*Returns a Response object.*

**Response Information**

* `response.status\_code`, `response.headers`, `response.text`, `response.json()`

**Status Codes**  
Basic understanding:

* 2xx → Success
* 4xx → Client/request error
* 5xx → Server-side error

**JSON API Response**

```python
data = response.json()
```

*Converts a JSON API response into Python data. Individual values can be accessed: `data\["key"]`*

**HTTP Error Handling**

* `response.raise\_for\_status()`: raises an HTTP exception for unsuccessful HTTP responses.

**API Exceptions**

* `requests.exceptions.HTTPError`, `requests.exceptions.ConnectionError`, `requests.exceptions.Timeout`

**Timeout**

* `requests.get(url, timeout=5)`: to prevent the program from waiting indefinitely.

\---

## Current Python Skills

At this point I have practiced:

* Variables, Strings, Lists, Dictionaries
* Conditions, Loops
* Functions, Parameters, Return values
* `try` / `except`
* File operations, JSON
* `subprocess`, `psutil`, `logging`, `requests`
* Basic REST APIs, Basic data processing, Basic modular programming

\---

## Next Stage — AWS Automation

The next major stage is AWS automation with `boto3`.
The goal is not to become a Python developer.
The goal is to use Python as a tool for Cloud Operations and Cloud Engineering.

**Planned progression:**

```text
Python
   ↓
boto3
   ↓
AWS APIs
   ↓
AWS resource discovery
   ↓
AWS automation
   ↓
IAM permissions
   ↓
CloudWatch / monitoring
   ↓
Infrastructure as Code
   ↓
Terraform
```

## Long-Term Cloud Engineering Project Plan

### Flagship Project: Infinite Storefront

*AWS AI Ideas 2025 finalist project.*  
This will be treated as the flagship project and documented with:

* Architecture
* AWS services
* Cost considerations
* IAM permissions
* Monitoring and logging
* Design decisions
* Bugs and troubleshooting
* Business value
* Technical decisions

### Additional Projects

**Project 2 — Traditional Infrastructure**

* Focus: Linux, Networking, AWS networking, Compute, Monitoring, Troubleshooting

**Project 3 — Infrastructure as Code**

* Focus: Terraform, AWS infrastructure, Automation, IAM, State management, Monitoring

**Project 4 — Python Cloud Automation**

* Focus: Python, boto3, AWS APIs, Automation, Error handling, Logging

*Each project should solve a realistic business problem while using different architecture and technologies.*

## Learning Philosophy

The projects are intentionally built incrementally.
Instead of memorizing syntax:

```text
Learn concept
    ↓
Try it independently
    ↓
Make mistakes
    ↓
Debug
    ↓
Look up documentation when necessary
    ↓
Implement
    ↓
Document what was learned
```

The objective is to develop the ability to reason about automation problems rather than simply reproduce code.

\---

