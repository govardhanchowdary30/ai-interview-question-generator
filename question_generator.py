QUESTION_BANK = {
    "python": [
        "What is Python and where is it used?",
        "Explain the difference between list and tuple in Python.",
        "What is exception handling in Python?"
    ],
    "sql": [
        "What is INNER JOIN?",
        "Difference between WHERE and HAVING?",
        "What is normalization in SQL?"
    ],
    "machine learning": [
        "What is supervised learning?",
        "Explain overfitting and underfitting.",
        "What is train-test split?"
    ],
    "data analysis": [
        "What are KPIs?",
        "What is EDA?",
        "Explain data cleaning."
    ],
    "excel": [
        "What is a pivot table?",
        "Difference between VLOOKUP and XLOOKUP?"
    ],
    "power bi": [
        "What is Power BI?",
        "What are measures and calculated columns?"
    ]
}

def generate_questions(skills):
    questions = []
    for skill in skills:
        if skill in QUESTION_BANK:
            questions.extend(QUESTION_BANK[skill])
    return questions