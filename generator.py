def generate_answer(ticket, classification, docs):

    if not docs:
        return "No relevant support info found. Escalating to human."

    top = docs[0]["text"]

    return f"""
Domain: {classification['domain']}
Issue: {classification['issue_type']}
Urgency: {classification['urgency']}

Answer:
{top}
"""