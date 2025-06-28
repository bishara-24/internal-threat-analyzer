#!/usr/bin/env python3
import os
import datetime

logfile = "threat_log.txt"

def log(message):
    with open(logfile, "a") as f:
        f.write(f"{datetime.datetime.now()} - {message}\n")

def check_logged_in_users():
    users = os.popen("who").read()
    log("=== Logged In Users ===")
    log(users)

def check_auth_logs():
    logs = os.popen("journalctl -n 20").read()
    log("=== Recent Journal Logs ===")
    log(logs)

def check_suspicious_processes():
    processes = os.popen("ps aux | grep -i ssh").read()
    log("=== Suspicious Processes (SSH) ===")
    log(processes)

if __name__ == "__main__":
    log("Starting Internal Threat Analysis...")
    check_logged_in_users()
    check_auth_logs()
    check_suspicious_processes()
    log("Analysis Completed.\n")

