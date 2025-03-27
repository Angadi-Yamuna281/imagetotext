from flask import Flask, render_template, request
import os
from image_to_text import image_to_text  # Import the function from image_to_text.py
from PIL import Image

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # ✅ Create folder if not exists
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def home():
    description = None  # Store extracted description

    if request.method == "POST":
        if "file" not in request.files:
            return "No file part"

        file = request.files["file"]

        if file.filename == "":
            return "No selected file"

        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            try:
                # ✅ Generate description from image
                description = image_to_text(filepath)  # Call your function from image_to_text.py
            except Exception as e:
                description = f"Error processing image: {e}"

    return render_template("index.html", description=description)


if __name__ == "__main__":
    app.run(debug=True)
