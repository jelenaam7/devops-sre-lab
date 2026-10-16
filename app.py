from flask import Flask, jsonify

app=Flask(__name__)

@app.get("/")
def home():
	return jsonify(message="Devops Sre lab is running")


@app.get("/health")
def health():
	return jsonify(status="ok"), 200

@app.get("/simulate-error")
def simulate_error():
    app.logger.error("Simulated HTTP 500 error triggered")
    return jsonify(error="Simulated internal server 500 error"), 500

if __name__=="__main__":
	app.run(host="127.0.0.1", port=5000)
