from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from flask_cors import CORS

# Initialize the Flask app
app = Flask(__name__)
CORS(app)
# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("t5-small")

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Text Summarization API!"})

@app.route("/summarize", methods=["POST"])
def summarize():
    try:
        data = request.get_json()

        text = data.get("text", "")
        max_length = data.get("max_length", 50)

        if not text:
            return jsonify({"error": "No text provided for summarization"}), 400

        input_ids = tokenizer(
            f"summarize: {text}",
            return_tensors="pt",
            max_length=512,
            truncation=True
        ).input_ids

        outputs = model.generate(
            input_ids,
            max_length=max_length,
            num_beams=5,
            early_stopping=True
        )

        summary = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return jsonify({"summary": summary})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
