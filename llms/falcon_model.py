import subprocess

def generate_article_falcon(prompt):
    result = subprocess.run(
        ["ollama", "run", "falcon", prompt],
        capture_output=True,
        text=True
    )
    return result.stdout
