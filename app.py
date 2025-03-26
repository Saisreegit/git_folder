from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/github-webhook", methods=["POST"])
def github_webhook():
    data = request.json
    if "ref" in data and data["ref"] == "refs/heads/main":
        subprocess.run(["/home/ec2-user/update_flask.sh"], shell=True)
        return "Updated Successfully", 200
    return "No update", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
