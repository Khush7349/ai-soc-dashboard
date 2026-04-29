def compute_severity(anomaly, anomaly_score, rules):
    score = 0
    reasons = []
    if anomaly == -1:
        score += 2
        reasons.append("ML detected anomaly")
    if anomaly_score < -0.2:
        score += 2
        reasons.append("High anomaly score")
    for rule in rules:
        sev = rule.get("severity", "Low")
        if sev == "High":
            score += 2
        elif sev == "Medium":
            score += 1
        else:
            score += 0.5
        reasons.append(rule.get("name", "rule_triggered"))
    if score >= 4:
        level = "Critical"
    elif score >= 3:
        level = "High"
    elif score >= 2:
        level = "Medium"
    else:
        level = "Low"
    return level, {
        "score": score,
        "reasons": reasons
    }