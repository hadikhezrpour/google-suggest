from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_keywords', methods=['POST'])
def get_keywords():
    data = request.json
    keyword = data['keyword']
    depth = data['depth']
    use_alphabet = data['useAlphabet']
    use_numbers = data['useNumbers']
    manual_keywords = data['manualKeywords']

    keywords = fetch_keywords(keyword, depth, use_alphabet, use_numbers, manual_keywords)
    return jsonify(keywords)

def fetch_keywords(keyword, depth, use_alphabet, use_numbers, manual_keywords):
    url = f"https://suggestqueries.google.com/complete/search?client=firefox&hl=fa&gl=IR&q={keyword}"
    response = requests.get(url)
    data = response.json()
    
    keywords = data[1] if len(data) > 1 else []
    
    extended_keywords = []
    persian_alphabet = 'اآبپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی'
    numbers = '123456789'

    for kw in keywords:
        extended_keywords.append(kw)
        if len(kw) <= 15:
            if use_alphabet:
                for char in persian_alphabet:
                    extended_keywords.append(f"{kw} {char}")
            if use_numbers:
                for num in numbers:
                    extended_keywords.append(f"{kw} {num}")
            for prefix in manual_keywords:
                extended_keywords.append(f"{prefix} {kw}")
                extended_keywords.append(f"{kw} {prefix}")

    return list(set(extended_keywords))  # Remove duplicates

if __name__ == '__main__':
    app.run(debug=True)