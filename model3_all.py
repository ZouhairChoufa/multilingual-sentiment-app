from flask import Flask, request, jsonify, render_template
import torch
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from transformers import AutoTokenizer, AutoModelForSequenceClassification

app = Flask(__name__)

# Load model directly
tokenizer = AutoTokenizer.from_pretrained("tabularisai/multilingual-sentiment-analysis")
model = AutoModelForSequenceClassification.from_pretrained("tabularisai/multilingual-sentiment-analysis")

# Set the model to evaluation mode.
model.eval()

@app.route("/")
@app.route("/home")
def home():
    return render_template("homePage.html")

@app.route("/model", methods=["GET", "POST"])
def model_page():
    if request.method == "POST":
        try:
            # Retrieve the text input from the form.
            user_input = request.form["user_input"]

            if not user_input:
                return jsonify({"error": "No input provided"})
            # Tokenize the user input.
            inputs = tokenizer(
                user_input,
                return_tensors="pt",
                padding=True,
                truncation=True,
                max_length=512
            )
            # Get the model prediction.
            with torch.no_grad():
                outputs = model(**inputs)
                logits = outputs.logits
            # Convert logits to the predicted label.
            prediction = torch.argmax(logits, dim=-1).item()

            # Map the predicted label to a sentiment string.
            # Adjust the mapping based on your model's label order.prediction = torch.argmax(logits, dim=-1)
            label_map = {
                0: "Very Negative", 
                1: "Negative", 
                2: "Neutral", 
                3: "Positive", 
                4: "Very Positive"
                }
            result = label_map.get(prediction, "Unknown")
            print(f"Prédiction: {result}")

            # Return the result as JSON so the JavaScript on the page can update it.
            return jsonify({"result": result})
        except Exception as e:
            # Return any errors as JSON.
            return jsonify({"error": str(e)})

    # For GET requests, render the main HTML page.
    return render_template("index.html", result="")

if __name__ == "__main__":
    app.run(debug=True)
