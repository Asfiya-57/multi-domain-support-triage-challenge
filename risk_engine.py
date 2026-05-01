def assess_risk(text, classification):

    text = text.lower()

    if "fraud" in text or "unauthorized" in text:
        return {
            "risk_level": "HIGH",
            "decision": "ESCALATE",
            "reason": "Security or fraud detected"
        }

    if classification["issue_type"] == "billing_issue":
        return {
            "risk_level": "MEDIUM",
            "decision": "ESCALATE",
            "reason": "Billing requires human verification"
        }

    if classification["domain"] == "Unknown":
        return {
            "risk_level": "MEDIUM",
            "decision": "ESCALATE",
            "reason": "Unknown domain"
        }

    return {
        "risk_level": "LOW",
        "decision": "ANSWER",
        "reason": "Safe request"
    }