
import csv
import os

# Create reports directory
os.makedirs("reports", exist_ok=True)


# -------------------------------
# INPUT VALIDATION
# -------------------------------

def get_int(message, minimum=0):
    while True:
        try:
            value = int(input(message))
            if value >= minimum:
                return value
            print(f"Enter a value greater than or equal to {minimum}.")
        except ValueError:
            print("Invalid input. Enter an integer.")


def save_report(filename, headers, data):
    path = os.path.join("reports", filename)

    with open(path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

    print(f"\nReport saved: {path}")


# -------------------------------
# 1. CPU SCHEDULING
# -------------------------------

def cpu_scheduling():

    print("\n--- CPU SCHEDULING ---")

    n = get_int("Enter number of processes: ", 1)

    processes = []

    for i in range(n):
        print(f"\nProcess P{i+1}")

        at = get_int("Arrival Time: ")
        bt = get_int("Burst Time: ", 1)

        processes.append({
            "pid": f"P{i+1}",
            "at": at,
            "bt": bt
        })

    print("\n1. FCFS")
    print("2. SJF (Non-preemptive)")
    print("3. Round Robin")

    choice = get_int("Choose algorithm: ", 1)

    if choice not in (1, 2, 3):
        print("Invalid algorithm.")
        return

    quantum = 2

    if choice == 3:
        quantum = get_int("Enter time quantum: ", 1)

    if choice == 1:
        name = "FCFS"
    elif choice == 2:
        name = "SJF"
    else:
        name = "Round Robin"

    # Initialize process information
    remaining = {p["pid"]: p["bt"] for p in processes}
    first_start = {}
    completion = {}

    pending = sorted(processes, key=lambda p: (p["at"], p["pid"]))
    ready = []
    gantt = []
    time = 0

    while pending or ready:

        while pending and pending[0]["at"] <= time:
            ready.append(pending.pop(0))

        if not ready:
            next_time = pending[0]["at"]
            gantt.append(("IDLE", time, next_time))
            time = next_time
            continue

        if choice == 2:
            ready.sort(
                key=lambda p: (
                    p["bt"], p["at"], p["pid"]
                )
            )

        process = ready.pop(0)
        pid = process["pid"]

        if pid not in first_start:
            first_start[pid] = time

        start = time

        if choice == 3:
            run_time = min(quantum, remaining[pid])
        else:
            run_time = remaining[pid]

        time += run_time
        remaining[pid] -= run_time

        gantt.append((pid, start, time))

        while pending and pending[0]["at"] <= time:
            ready.append(pending.pop(0))

        if remaining[pid] > 0:
            ready.append(process)
        else:
            completion[pid] = time

    # Calculate performance metrics
    results = []

    for p in processes:
        pid = p["pid"]

        ct = completion[pid]
        tat = ct - p["at"]
        wt = tat - p["bt"]
        rt = first_start[pid] - p["at"]

        results.append([
            pid, p["at"], p["bt"],
            ct, tat, wt, rt
        ])

    print("\nGANTT CHART")
    print(" | ".join(
        f"{pid}[{start}-{end}]"
        for pid, start, end in gantt
    ))

    print("\nPID  AT  BT  CT  TAT  WT  RT")

    for row in results:
        print(*row)

    avg_wt = sum(r[5] for r in results) / n
    avg_tat = sum(r[4] for r in results) / n

    print("\nAverage Waiting Time:", round(avg_wt, 2))
    print("Average Turnaround Time:", round(avg_tat, 2))

    save_report(
        "cpu_scheduling.csv",
        ["PID", "AT", "BT", "CT", "TAT", "WT", "RT"],
        results
    )


# -------------------------------
# 2. MEMORY MANAGEMENT
# -------------------------------

def memory_management():

    print("\n--- MEMORY MANAGEMENT ---")

    blocks = list(map(
        int,
        input("Enter memory block sizes: ").split()
    ))

    processes = list(map(
        int,
        input("Enter process sizes: ").split()
    ))

    print("\n1. First Fit")
    print("2. Best Fit")
    print("3. Worst Fit")

    choice = get_int("Choose algorithm: ", 1)

    if choice not in (1, 2, 3):
        print("Invalid algorithm.")
        return

    free = blocks[:]
    results = []

    for i, size in enumerate(processes, 1):

        candidates = [
            j for j, block in enumerate(free)
            if block >= size
        ]

        if not candidates:
            results.append([
                f"P{i}", size, "Not Allocated", 0
            ])
            continue

        if choice == 1:
            index = candidates[0]

        elif choice == 2:
            index = min(candidates, key=lambda j: free[j])

        else:
            index = max(candidates, key=lambda j: free[j])

        free[index] -= size

        results.append([
            f"P{i}", size,
            f"Block {index+1}",
            free[index]
        ])

    print("\nPID  SIZE  ALLOCATION  REMAINING")

    for row in results:
        print(*row)

    allocated = sum(
        row[1] for row in results
        if row[2] != "Not Allocated"
    )

    print("\nTotal Memory Allocated:", allocated)
    print("Total Free Memory:", sum(free))

    save_report(
        "memory_allocation.csv",
        ["PID", "Size", "Allocation", "Remaining Block"],
        results
    )


# -------------------------------
# 3. DISK SCHEDULING
# -------------------------------

def disk_scheduling():

    print("\n--- DISK SCHEDULING ---")

    head = get_int("Enter initial head position: ")

    requests = list(map(
        int,
        input("Enter disk requests: ").split()
    ))

    print("\n1. FCFS")
    print("2. SSTF")
    print("3. SCAN (upward first)")

    choice = get_int("Choose algorithm: ", 1)

    if choice not in (1, 2, 3):
        print("Invalid algorithm.")
        return

    if choice == 1:
        order = requests[:]

    elif choice == 2:
        remaining = requests[:]
        order = []
        current = head

        while remaining:
            nearest = min(
                remaining,
                key=lambda x: abs(x - current)
            )

            order.append(nearest)
            remaining.remove(nearest)
            current = nearest

    else:
        higher = sorted(
            x for x in requests if x >= head
        )

        lower = sorted(
            (x for x in requests if x < head),
            reverse=True
        )

        order = higher + lower

    movement = 0
    current = head

    for request in order:
        movement += abs(request - current)
        current = request

    print("\nService Order:", order)
    print("Total Head Movement:", movement)

    if requests:
        print(
            "Average Head Movement:",
            round(movement / len(requests), 2)
        )

    save_report(
        "disk_scheduling.csv",
        ["Initial Head", "Service Order", "Total Movement"],
        [[head, " -> ".join(map(str, order)), movement]]
    )


# -------------------------------
# 4. PROCESS MANAGEMENT
# -------------------------------

def process_management():

    print("\n--- PROCESS MANAGEMENT ---")

    n = get_int("Enter number of processes: ", 1)

    results = []

    for i in range(1, n + 1):

        pid = f"P{i}"

        print(f"\n{pid}: NEW")

        print(f"{pid}: READY")

        print(f"{pid}: RUNNING")

        print(f"{pid}: TERMINATED")

        results.append([
            pid,
            "NEW",
            "READY",
            "RUNNING",
            "TERMINATED"
        ])

    save_report(
        "process_states.csv",
        ["PID", "State 1", "State 2", "State 3", "Final State"],
        results
    )


# -------------------------------
# MAIN APPLICATION
# -------------------------------

def main():

    while True:

        print("\n================================")
        print(" OS RESOURCE MANAGEMENT SYSTEM ")
        print("================================")

        print("1. CPU Scheduling")
        print("2. Memory Management")
        print("3. Disk Scheduling")
        print("4. Process Management")
        print("5. Exit")

        choice = get_int("\nEnter your choice: ", 1)

        if choice == 1:
            cpu_scheduling()

        elif choice == 2:
            memory_management()

        elif choice == 3:
            disk_scheduling()

        elif choice == 4:
            process_management()

        elif choice == 5:
            print("\nApplication terminated.")
            break

        else:
            print("Invalid choice. Select 1-5.")


if __name__ == "__main__":
    main()
