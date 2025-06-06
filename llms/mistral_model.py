import subprocess

def generate_article_mistral(prompt):
    response = subprocess.run(
        ["ollama", "run", "mistral", prompt],
        capture_output=True,
        text=True
    )
    return response.stdout
