from transformers import pipeline

# Load pre-trained AI model
ai_model = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def get_ai_decision(input_text):
    """Function to classify input text using AI model"""
    result = ai_model(input_text)
    return result[0]['label']  # Returns 'POSITIVE' or 'NEGATIVE'

# Example usage
if __name__ == "__main__":
    print(get_ai_decision("Brute-force attack detected"))
