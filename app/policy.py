def apply_policy(scan_result: dict) -> dict:
    action = scan_result["action"]
    text = scan_result["input_text"]

    if action == "redact":
        redacted_text = text.replace("system prompt", "[REDACTED]")
    else:
        redacted_text = text

    return {
        "final_action": action,
        "output_text": redacted_text,
        "explanation": scan_result["explanation"],
        "details": {
            "rule_result": scan_result["rule_result"],
            "ml_prediction": scan_result["ml_prediction"],
            "combined_score": scan_result["combined_score"],
            "risk_level": scan_result["risk_level"],
        },
    }