PROTOCOL_MAP = {"TCP": 0, "UDP": 1, "ICMP": 2}
THRESHOLDS = {
    "high_traffic": 500_000,
    "udp_flood": 200_000,
}
def apply_rules(row):
    """
    Returns a list of rule hits with structure:
    [
      {"name": "...", "description": "...", "severity": "Low|Medium|High"}
    ]
    """
    alerts = []
    bytes_val = float(row.get("bytes", 0))
    protocol = row.get("protocol")
    if isinstance(protocol, str):
        protocol_val = PROTOCOL_MAP.get(protocol, -1)
    else:
        protocol_val = int(protocol) if protocol is not None else -1
    if bytes_val > THRESHOLDS["high_traffic"]:
        alerts.append({
            "name": "high_traffic_spike",
            "description": "Unusually large data transfer observed",
            "severity": "Medium"
        })
    if protocol_val == PROTOCOL_MAP["UDP"] and bytes_val > THRESHOLDS["udp_flood"]:
        alerts.append({
            "name": "udp_flood",
            "description": "High UDP traffic may indicate flooding attack",
            "severity": "High"
        })
    return alerts