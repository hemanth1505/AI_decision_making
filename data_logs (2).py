import pandas as pd

# Sample security alerts
data = {
    "Alert": ["Brute-force Attack", "SQL Injection", "Phishing Email", "DDoS Attack"],
    "Severity": ["High", "Critical", "Medium", "High"]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save sample logs as CSV
df.to_csv("logs.csv", index=False)

# Example usage
if __name__ == "__main__":
    print(df)
