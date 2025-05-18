import requests
import re
import unicodedata

url = "https://raw.githubusercontent.com/inspirationlinks/m3u/refs/heads/live/FreeStreaming.m3u"
response = requests.get(url)

# Lista de termos a serem filtrados (adicione ou remova conforme necessário)
blocked_terms = [
    "adult", "erotic", "xxx", "porn", "sexo", "18+", "hot", "onlyfans", "nsfw"
]

def normalize(text):
    # Remove acentos, transforma em minúsculo e remove caracteres especiais
    text = unicodedata.normalize('NFKD', text)
    text = ''.join([c for c in text if not unicodedata.combining(c)])
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    return text.lower()

def is_blocked(line):
    norm_line = normalize(line)
    return any(term in norm_line for term in blocked_terms)

filtered_lines = [line for line in response.text.split('\n') if not is_blocked(line)]

with open("Freetv-filtered.m3u", "w") as f:
    f.write('\n'.join(filtered_lines))
