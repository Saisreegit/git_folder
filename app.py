from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/service")
def service():
    return render_template("service.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/student_details")
def student_details():
    return render_template("student_details.html")

@app.route("/student_marks")
def student_marks():
    return render_template("student_marks.html")

@app.route("/student_skills")
def student_skills():
    return render_template("student_skills.html")

@app.route("/student_poy")
def student_poy():
    return render_template("student_poy.html")

if __name__ == "__main__":
    app.run(debug=True)
