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
        "details": scan_result["rule_result"],
    }