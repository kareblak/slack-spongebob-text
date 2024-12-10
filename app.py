from flask import Flask, request, jsonify
import os

app = Flask(__name__)

def spongebob_text(text):
    return ''.join(
        char.upper() if i % 2 == 0 else char.lower()
        for i, char in enumerate(text)
    )

@app.route('/spongebob', methods=['POST'])
def spongebob():
    data = request.form
    text = data.get('text', '').strip()

    response_text = spongebob_text(text)

    return jsonify({
        "response_type": "in_channel",
        "text": response_text
    })

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5002))
    app.run(host='0.0.0.0', port=port)
