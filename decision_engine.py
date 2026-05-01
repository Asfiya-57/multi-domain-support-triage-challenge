def decide(risk, docs):

    if risk["decision"] == "ESCALATE":
        return "ESCALATE"

    if not docs:
        return "ESCALATE"

    return "ANSWER"