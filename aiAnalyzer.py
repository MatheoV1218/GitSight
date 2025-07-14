# aiAnalyzer.py
def analyze_github_summary(summary, client):
    print("\nSending data to GPT-3.5 for analysis...\n")

    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
                "content": (
                    "You are a professional GitHub profile reviewer. "
                    "Your job is to evaluate GitHub accounts based on their activity, codebase, and documentation. You should also make a comment about the languages they use and which repositories stand out for their stars if any "
                    "Always respond using the following strict format:\n\n"
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
                    "Always base your analysis only on the provided GitHub summary. Be specific and constructive."
                )},
            {"role": "user", "content": f"Here's a GitHub profile summary:\n\n{summary}\n\nPlease provide feedback on this GitHub account, including strengths, weaknesses, and suggestions for improvement."}
        ]
    )

    return chat_completion.choices[0].message.content
