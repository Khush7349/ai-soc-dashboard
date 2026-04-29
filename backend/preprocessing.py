import pandas as pd
PROTOCOL_MAP = {
    "TCP": 0,
    "UDP": 1,
    "ICMP": 2
}
def preprocess(df):
    df = df.copy()
    df["protocol"] = df["protocol"].fillna("UNKNOWN")
    df["bytes"] = pd.to_numeric(df["bytes"], errors="coerce").fillna(0)
    df["protocol"] = df["protocol"].map(PROTOCOL_MAP).fillna(-1)
    df["bytes"] = df["bytes"] / (df["bytes"].max() + 1)
    return df[["bytes", "protocol"]]