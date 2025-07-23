from flask import Flask, jsonify
from flask_cors import CORS
from agent import call_agent
from assemblyAI import stop_event
from threading import Thread


app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])


@app.route("/agentcall", methods=['POST'])
def agent():
    def run_agent():
        try:
            result = call_agent()
            print("Agent finished with result:", result)
        except Exception as e:
            print("Agent failed:", e)

    Thread(target=run_agent).start()
    return jsonify({'message': 'Agent started'})


@app.route("/stoprecording", methods=['POST'])
def stop():
    stop_event.set()
    return jsonify({'message': 'Recording stopped'})
 

# app.run(port=5000)
if __name__ == "__main__":
    app.run(port=5000, threaded=True)
