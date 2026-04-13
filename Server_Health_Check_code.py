import psutil
import time
"""psutil is a cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors) in Python. It is mainly used for system monitoring, profiling, and limiting process resources and management of running processes."""
"""I am using infinite loop to continuously monitor the CPU usage and print an alert if it exceeds the defined threshold. The user can stop the monitoring by pressing Ctrl+C, which will raise a KeyboardInterrupt exception that we catch to gracefully exit the program."""

THRESHOLD = 80

def check_server_health():
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        
        if cpu_usage > THRESHOLD:
            print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
        else:
            print(f"CPU Usage: {cpu_usage}%")
            
    except Exception as e:
        print("Error while checking CPU:", e)


print("Monitoring CPU usage... Press Ctrl+C to stop.\n")

try:
    while True:
        check_server_health()
        time.sleep(1)

except KeyboardInterrupt:
    print("\nMonitoring stopped by user.")