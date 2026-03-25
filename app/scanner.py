from app.rules import check_rules
from app.ml_model import predict_prompt

def scan_prompt(text: str) -> dict:
    rule_result = check_rules(text)
    ml_prediction = predict_prompt(text)

    rule_score = rule_result["rule_score"]

    if ml_prediction == 1:
        combined_score = rule_score + 2
    else:
        combined_score = rule_score

    if combined_score >= 4:
        action = "block"
        risk_level = "high"
    elif combined_score >= 2:
        action = "redact"
        risk_level = "medium"
    else:
        action = "allow"
        risk_level = "low"

    # explanation
    if action == "block":
        explanation = "Prompt classified as malicious due to rule matches and/or ML detection."
    elif action == "redact":
        explanation = "Prompt contains potentially unsafe patterns."
    else:
        explanation = "Prompt appears safe."

    return {
        "input_text": text,
        "rule_result": rule_result,
        "ml_prediction": ml_prediction,
        "combined_score": combined_score,
        "risk_level": risk_level,
        "action": action,
        "explanation": explanation,
    }