import os
from flask import Flask, render_template_string, request

app = Flask(__name__)

MY_NAME = "John"
MY_SURNAME = "Doe"

HTML_PAGE = """
<!doctype html>
<html>
<head>
    <title>GKE Simple Web App</title>
</head>
<body style="font-family: Arial; text-align: center; margin-top: 50px;">
    <h2>Enter 1 for Name or 2 for Surname</h2>
    <form method="POST">
        <input type="text" name="choice" placeholder="Enter 1 or 2" required autofocus>
        <button type="submit">Submit</button>
    </form>
    {% if result %}
        <h3 style="color: blue; margin-top: 20px;">{{ result }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        choice = request.form.get("choice", "").strip()
        if choice == "1":
            result = f"Name: {MY_NAME}"
        elif choice == "2":
            result = f"Surname: {MY_SURNAME}"
        else:
            result = "Invalid input! Please enter only 1 or 2."
    return render_template_string(HTML_PAGE, result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
