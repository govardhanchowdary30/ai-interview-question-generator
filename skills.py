SKILLS_DB = [
    "python", "sql", "machine learning", "data analysis",
    "excel", "power bi", "java", "html", "css", "javascript"
]

def extract_skills(text):
    text = text.lower()
    found_skills = []
    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)
    return found_skills