from classifier import classify_ticket
from risk_engine import assess_risk
from decision_engine import decide


def test_hackerrank_login():
    c = classify_ticket("I cannot login to HackerRank assessment")
    assert c["domain"] == "HackerRank"
    assert c["issue_type"] == "login_issue"


def test_claude_bug():
    c = classify_ticket("Claude API gives error")
    assert c["domain"] == "Claude"
    assert c["issue_type"] == "bug_issue"


def test_visa_billing():
    c = classify_ticket("Visa payment failed")
    assert c["domain"] == "Visa"
    assert c["issue_type"] == "billing_issue"


def test_unknown_domain():
    c = classify_ticket("Need support for random platform")
    assert c["domain"] == "Unknown"


def test_fraud_escalates():
    c = classify_ticket("Unauthorized card transaction detected")
    r = assess_risk("Unauthorized card transaction detected", c)
    assert r["decision"] == "ESCALATE"


def test_billing_escalates():
    c = classify_ticket("Payment billed twice")
    r = assess_risk("Payment billed twice", c)
    assert r["decision"] == "ESCALATE"


def test_unknown_escalates():
    c = classify_ticket("hello")
    r = assess_risk("hello", c)
    assert r["decision"] == "ESCALATE"


def test_safe_answer_path():
    c = classify_ticket("HackerRank login issue")
    r = assess_risk("HackerRank login issue", c)
    assert r["decision"] == "ANSWER"


def test_decision_escalate_from_risk():
    d = decide({"decision": "ESCALATE"}, [{"text": "x"}])
    assert d == "ESCALATE"


def test_decision_escalate_no_docs():
    d = decide({"decision": "ANSWER"}, [])
    assert d == "ESCALATE"