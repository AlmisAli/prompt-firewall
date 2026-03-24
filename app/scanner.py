from app.rules import check_rules


def scan_prompt(text: str) -> dict:
    rule_result = check_rules(text)

    if rule_result["risk_level"] == "high":
        action = "block"
    elif rule_result["risk_level"] == "medium":
        action = "redact"
    else:
        action = "allow"

    return {
        "input_text": text,
        "rule_result": rule_result,
        "action": action,
    }