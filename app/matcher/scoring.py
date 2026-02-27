import json
from app.matcher.embeddings import similarity

def score_job(parsed_job):
    with open("master_profile.json") as f:
        profile = json.load(f)

    required = parsed_job.get("required_skills", [])
    skills = profile["skills"]

    if not required:
        return 0.0

    matched = len(set(required) & set(skills))
    keyword_score = matched / len(required)

    semantic_score = similarity(
        str(profile["experience"]),
        str(parsed_job)
    )

    final_score = 0.7 * keyword_score + 0.3 * semantic_score
    return final_score