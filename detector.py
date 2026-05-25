def analyze_logs(logs):
    failed_logins = 0
    threats = []

    for log in logs:
        log = log.lower()

        # 1. Failed login detection
        if "failed login" in log:
            failed_logins += 1

        # 2. Privilege escalation
        if "privilege escalation" in log:
            threats.append({
                "type": "Privilege Escalation",
                "severity": "CRITICAL",
                "log": log
            })

        # 3. Successful login after failures
        if "successful login" in log and failed_logins > 2:
            threats.append({
                "type": "Brute Force Success",
                "severity": "HIGH",
                "log": log
            })

    # final brute force check
    if failed_logins >= 3:
        threats.append({
            "type": "Brute Force Attack",
            "severity": "HIGH",
            "log": f"{failed_logins} failed logins detected"
        })

    return threats