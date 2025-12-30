from flask import Flask, render_template, Response
import subprocess
import sys

app = Flask(__name__)

def run_game():
    process = subprocess.Popen(
        [sys.executable, "what_the_hack.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )

    for line in process.stdout:
        yield f"data: {line}\n\n"

    process.stdout.close()
    process.wait()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/stream")
def stream():
    return Response(run_game(), mimetype="text/event-stream")

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
