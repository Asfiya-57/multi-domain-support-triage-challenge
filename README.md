# AI Support Triage Agent (Fail-Safe)

## Overview
This project is a multi-domain support triage system for tickets related to **HackerRank**, **Claude API**, and **Visa payments**.

It performs five steps:
1. Classifies ticket domain and issue type
2. Assesses risk level
3. Retrieves relevant support snippets
4. Decides whether to auto-answer or escalate
5. Generates a final response

## Why this is useful
In support systems, speed matters, but safety matters more.  
This agent follows a fail-safe policy:
- risky or uncertain tickets -> **ESCALATE**
- safe known tickets -> **ANSWER**

This helps reduce unsafe automated replies in fraud, billing, or unknown cases.

## Approach / Architecture
- `classifier.py` -> domain + issue type + urgency
- `risk_engine.py` -> risk scoring and escalation reason
- `retriever.py` -> TF-IDF retrieval from support docs
- `decision_engine.py` -> final `ANSWER` / `ESCALATE`
- `generator.py` -> final response text
- `main.py` -> CLI entrypoint

## Setup Instructions (Windows PowerShell)

```powershell
cd "C:\Users\Lenovo\OneDrive\Desktop\triage-agent"
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install scikit-learn pytest

```

## Run Instructions

```powershell
.\.venv\Scripts\python.exe main.py
```


## Test Instructions

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

## Sample Inputs
- I cannot login to HackerRank test
- Claude API is giving error
- my visa card was charged without permission
- hello

## Sample Expected Behavior
- Known low-risk issues -> ANSWER
- Unknown or policy-sensitive issues -> ESCALATE

## Limitations
- Rule-based classification (keyword matching)
- Small local document set
- No external API integration yet

## Future Improvements
- Better fraud phrase coverage and confidence scoring
- Larger knowledge base
- FastAPI endpoint for deployment
- Monitoring and analytics
