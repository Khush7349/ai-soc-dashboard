import random
import pandas as pd

def generate_logs(n=1000):
    data = []

    for i in range(n):
        data.append({
            "timestamp": i,
            "src_ip": f"192.168.1.{random.randint(1,50)}",
            "dst_ip": f"10.0.0.{random.randint(1,10)}",
            "bytes": random.choice([100,500,1000,1000000]),
            "protocol": random.choice(["TCP","UDP"]),
            "src_port": random.randint(1000,5000),
            "dst_port": random.choice([80,443,22]),
            "flag": random.choice(["SF","REJ"])
        })

    return pd.DataFrame(data)


if __name__ == "__main__":
    df = generate_logs(1000)
    df.to_csv("logs.csv", index=False)
    print("Generated logs.csv")