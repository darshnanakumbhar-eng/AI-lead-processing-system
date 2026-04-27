# main.py
print("Script is running...")
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------
# 1. Lead Classification Logic
# -----------------------------
def classify_lead(budget, timeline, message):
    if budget and "urgent" in message.lower():
        return "Hot"
    elif budget:
        return "Warm"
    else:
        return "Cold"

# -----------------------------
# 2. Response Generation
# -----------------------------
def generate_response(name, category, message):
    if category == "Hot":
        return f"Hi {name}, thanks for reaching out! Your requirement sounds exciting. We can help you quickly. Let’s schedule a call to get started."
    
    elif category == "Warm":
        return f"Hi {name}, thanks for your interest. We’d love to understand your needs better. Let’s connect and explore how we can help."
    
    else:
        return f"Hi {name}, thanks for reaching out. Could you please share more details about your requirement?"

# -----------------------------
# 3. Similarity Matching
# -----------------------------
def find_most_similar(query, inputs):
    best_match = None
    best_score = -1

    for key, vec in inputs.items():
        score = cosine_similarity([query], [vec])[0][0]
        if score > best_score:
            best_score = score
            best_match = key

    return best_match

# -----------------------------
# 4. Sample Run
# -----------------------------
if __name__ == "__main__":
    # Sample lead
    lead = {
        "name": "Sakshi",
        "budget": "5000 USD",
        "timeline": "2 weeks",
        "message": "Need a landing page urgently"
    }

    category = classify_lead(lead["budget"], lead["timeline"], lead["message"])
    response = generate_response(lead["name"], category, lead["message"])

    print("Lead Category:", category)
    print("Response:", response)

    # Similarity Example
    inputs = {
        "Lead1": [0.1, 0.2, 0.3],
        "Lead2": [0.9, 0.8, 0.7],
        "Lead3": [0.2, 0.1, 0.4]
    }

    query = [0.1, 0.2, 0.25]
    match = find_most_similar(query, inputs)

    print("Most Similar Lead:", match)