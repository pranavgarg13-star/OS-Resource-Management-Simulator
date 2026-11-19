# OS Resource Management Simulator

An integrated **Python and Bash-based Operating System Resource Management Simulator** designed to demonstrate and analyse major OS resource-management techniques.

The application simulates CPU scheduling, memory allocation, disk scheduling, and process management. It also calculates performance metrics and generates CSV reports for analysis.

## Features

### 1. CPU Scheduling
Implements three CPU scheduling algorithms:
- First Come First Served (FCFS)
- Shortest Job First (SJF – Non-preemptive)
- Round Robin (RR)

Performance metrics:
- Completion Time (CT)
- Turnaround Time (TAT)
- Waiting Time (WT)
- Response Time (RT)
- Average Waiting Time
- Average Turnaround Time

### 2. Memory Management
Implements three memory allocation strategies:
- First Fit
- Best Fit
- Worst Fit

Displays memory allocation decisions, allocated memory, and remaining free memory.

### 3. Disk Scheduling
Implements:
- First Come First Served (FCFS)
- Shortest Seek Time First (SSTF)
- SCAN (elevator algorithm, simplified)

Calculates total disk head movement and average head movement per request.

### 4. Process Management
Demonstrates the basic process lifecycle:
- NEW
- READY
- RUNNING
- TERMINATED

### 5. Report Generation
Automatically generates CSV reports for:
- CPU scheduling results
- Memory allocation results
- Disk scheduling results
- Process state transitions

## Technologies Used

- Python 3
- Bash Shell Scripting
- CSV
- Linux / Ubuntu / WSL
- Visual Studio Code
- Git and GitHub

## Project Structure

```text
OS-Resource-Management-Simulator/
│
├── app.py
├── run.sh
├── README.md
├── .gitignore
│
└── reports/
    ├── cpu_scheduling.csv
    ├── memory_allocation.csv
    ├── disk_scheduling.csv
    └── process_states.csv
```

## Installation and Execution

### Requirements
- Python 3.8 or later
- Bash terminal
- Linux, macOS, or Windows Subsystem for Linux (WSL)

### Step 1: Clone the repository

```bash
git clone https://github.com/USERNAME/OS-Resource-Management-Simulator.git
```

Replace `USERNAME` with your GitHub username.

### Step 2: Open the project directory

```bash
cd OS-Resource-Management-Simulator
```

### Step 3: Give execution permission

```bash
chmod +x run.sh
```

### Step 4: Run the application

```bash
./run.sh
```

Alternatively, execute the Python application directly:

```bash
python3 app.py
```

## Application Menu

```text
================================
 OS RESOURCE MANAGEMENT SYSTEM
================================

1. CPU Scheduling
2. Memory Management
3. Disk Scheduling
4. Process Management
5. Exit

Enter your choice:
```

## Learning Outcomes

- Understand CPU scheduling and process execution.
- Compare different memory allocation algorithms.
- Analyse disk scheduling strategies.
- Understand process states and transitions.
- Calculate and interpret OS performance metrics.
- Integrate Python programming with Bash scripting.
- Generate structured analytical reports.

## Project Limitations

This is an educational simulation. It models OS resource-management behaviour without directly modifying physical memory, hardware disk operations, or actual operating-system process priorities.

## Author

**Your Name**

Operating Systems Project

## License

This project is available for educational and learning purposes.