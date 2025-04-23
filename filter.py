import requests

url = "https://raw.githubusercontent.com/inspirationlinks/m3u/refs/heads/live/Freetv.m3u"
response = requests.get(url)

# Lista de termos a serem filtrados (adicione ou remova conforme necessário)
blocked_terms = [
    "adult", "erotic", "xxx", "porn", "sexo", "18+", "hot", "onlyfans", "nsfw"
]

def is_blocked(line):
    return any(term in line.lower() for term in blocked_terms)

filtered_lines = [line for line in response.text.split('\n') if not is_blocked(line)]

with open("Freetv-filtered.m3u", "w") as f:
    f.write('\n'.join(filtered_lines))
