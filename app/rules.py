import re

SUSPICIOUS_PATTERNS = [
    r"ignore\s+previous\s+instructions",
    r"ignore\s+all\s+previous\s+instructions",
    r"disregard\s+previous\s+instructions",
    r"reveal\s+the\s+system\s+prompt",
    r"show\s+me\s+the\s+hidden\s+prompt",
    r"developer\s+message",
    r"system\s+prompt",
    r"bypass\s+safety",
    r"do\s+not\s+follow\s+the\s+rules",
    r"jailbreak",
    r"override\s+instructions",
]

SUSPICIOUS_KEYWORDS = [
    "ignore previous instructions",
    "reveal system prompt",
    "hidden prompt",
    "developer message",
    "system prompt",
    "bypass safety",
    "jailbreak",
    "override",
]


def check_rules(text: str) -> dict:
    text_lower = text.lower()

    matched_patterns = []
    matched_keywords = []

    for pattern in SUSPICIOUS_PATTERNS:
        if re.search(pattern, text_lower):
            matched_patterns.append(pattern)

    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in text_lower:
            matched_keywords.append(keyword)

    rule_score = len(matched_patterns) * 2 + len(matched_keywords)

    if rule_score >= 4:
        risk_level = "high"
    elif rule_score >= 2:
        risk_level = "medium"
    else:
        risk_level = "low"

    return {
        "matched_patterns": matched_patterns,
        "matched_keywords": matched_keywords,
        "rule_score": rule_score,
        "risk_level": risk_level,
    }