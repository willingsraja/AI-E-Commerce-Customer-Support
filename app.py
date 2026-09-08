from flask import Flask, render_template, request, session

from agent import run_agent


app = Flask(__name__)

# Secret key for session memory
app.secret_key = "ecommerce-agent-secret"


# Home page
@app.route("/")
def home():

    return render_template("index.html")


# Chat route
@app.route("/chat", methods=["POST"])
def chat():

    message = request.form["message"]


    # Create memory if it doesn't exist
    if "memory" not in session:

        session["memory"] = {}


    memory = session["memory"]


    # Send message to agent
    response = run_agent(
        message,
        memory
    )


    # Save updated memory
    session["memory"] = memory

    session.modified = True


    return response


# Run application
if __name__ == "__main__":

    app.run(debug=True)