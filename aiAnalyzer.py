import re

def analyze_github_summary(summary, client):
    print("\nSending data to GPT-3.5 for analysis...\n")

    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a professional GitHub profile reviewer and career mentor. "
                    "You will receive a GitHub summary and must analyze it without contradicting yourself. "
                    "Only mention stars, languages, or README files in either strengths or weaknesses, based on whether more than half of the repositories meet that criteria. "
                    "In addition, at the end of your evaluation, recommend 3 specific project ideas tailored to the user's experience and skills. "
                    "Use this exact format:\n\n"
                    "### GitHub Profile Evaluation\n\n"
                    "**1. Strengths:**\n"
                    "- Bullet point 1\n"
                    "- Bullet point 2\n"
                    "- Bullet point 3\n\n"
                    "**2. Weaknesses:**\n"
                    "- Bullet point 1\n"
                    "- Bullet point 2\n"
                    "- Bullet point 3\n\n"
                    "**3. Suggestions for Improvement:**\n"
                    "- Bullet point 1\n"
                    "- Bullet point 2\n"
                    "- Bullet point 3\n\n"
                    "**4. What to Build Next:**\n"
                    "- Project idea 1\n"
                    "- Project idea 2\n"
                    "- Project idea 3\n\n"
                    "Base everything only on the provided GitHub summary. Be specific and do not contradict across sections."
                )
            },
            {
                "role": "user",
                "content": f"Here's a GitHub profile summary:\n\n{summary}\n\nPlease provide feedback and project ideas."
            }
        ]
    )

    ai_text = chat_completion.choices[0].message.content

    def extract_section(title):
        pattern = rf"\*\*{title}:\*\*\n((?:- .+\n)+)"
        match = re.search(pattern, ai_text)
        if match:
            return [line[2:] for line in match.group(1).strip().split("\n")]
        return []

    return {
        "strengths": extract_section("1. Strengths"),
        "weaknesses": extract_section("2. Weaknesses"),
        "suggestions": extract_section("3. Suggestions for Improvement"),
        "projects": extract_section("4. What to Build Next"),
        "raw_text": ai_text
    }
