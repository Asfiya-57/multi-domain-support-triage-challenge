from classifier import classify_ticket
from risk_engine import assess_risk
from retriever import Retriever
from decision_engine import decide
from generator import generate_answer

# ----------------------------
# INIT SYSTEM
# ----------------------------
retriever = Retriever()

retriever.load_docs({
    "HackerRank": "data/hackerrank.txt",
    "Claude": "data/claude.txt",
    "Visa": "data/visa.txt"
})

print("\n===================================")
print("   SUPPORT TRIAGE AGENT v1.0")
print("   Multi-Domain AI System")
print("===================================\n")

print("System Ready 🚀 Enter support tickets below:\n")

# ----------------------------
# MAIN LOOP
# ----------------------------
while True:

    ticket = input("🧾 Enter Issue: ")

    # STEP 1: CLASSIFY
    classification = classify_ticket(ticket)

    # STEP 2: RISK ANALYSIS
    risk = assess_risk(ticket, classification)

    # STEP 3: RETRIEVAL
    docs = retriever.retrieve(ticket)

    # STEP 4: DECISION
    decision = decide(risk, docs)

    # ----------------------------
    # OUTPUT FORMAT (CLEAN)
    # ----------------------------
    print("\n==============================")
    print("📊 TRIAGE RESULT")
    print("==============================")

    print("Domain      :", classification["domain"])
    print("Issue Type  :", classification["issue_type"])
    print("Urgency     :", classification["urgency"])
    print("Risk Level  :", risk["risk_level"])
    print("Decision    :", decision)

    # ----------------------------
    # ESCALATION PATH
    # ----------------------------
    if decision == "ESCALATE":

        print("\n🚨 ESCALATION REQUIRED")
        print("Reason  :", risk["reason"])
        print("Action  : Forwarded to human support team")

    # ----------------------------
    # ANSWER PATH
    # ----------------------------
    else:

        response = generate_answer(ticket, classification, docs)

        print("\n📌 SUPPORT RESPONSE")
        print("--------------------------------")
        print(response)
        print("--------------------------------")

    print("\n===================================\n")