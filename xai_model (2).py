import random

def explain_decision(decision):
    """Generate a simple explanation for AI's decision"""
    explanations = {
        "POSITIVE": "The system detects a strong security posture.",
        "NEGATIVE": "Potential security risk detected. Immediate action required!"
    }
    return explanations.get(decision, "Unknown decision.")

# Example usage
if __name__ == "__main__":
    decision = "NEGATIVE"
    print(explain_decision(decision))
