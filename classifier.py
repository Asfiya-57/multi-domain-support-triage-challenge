def classify_ticket(text):
    text = text.lower()

    # Domain detection
    if "hackerrank" in text or "test" in text or "assessment" in text:
        domain = "HackerRank"
    elif "claude" in text or "api" in text or "anthropic" in text:
        domain = "Claude"
    elif "visa" in text or "card" in text or "payment" in text:
        domain = "Visa"
    else:
        domain = "Unknown"

    # Issue type detection
    if "login" in text or "sign in" in text:
        issue_type = "login_issue"
    elif "payment" in text or "billing" in text:
        issue_type = "billing_issue"
    elif "fraud" in text or "unauthorized" in text:
        issue_type = "fraud_issue"
    elif "error" in text or "bug" in text:
        issue_type = "bug_issue"
    else:
        issue_type = "general_faq"

    # urgency
    if issue_type == "fraud_issue":
        urgency = "high"
    elif issue_type in ["billing_issue", "login_issue"]:
        urgency = "medium"
    else:
        urgency = "low"

    return {
        "domain": domain,
        "issue_type": issue_type,
        "urgency": urgency
    }