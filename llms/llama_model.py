import subprocess

def generate_article_llama(prompt):
    result = subprocess.run(
        ["ollama", "run", "llama2", prompt],
        capture_output=True,
        text=True
    )
    return result.stdout
