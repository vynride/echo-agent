from flask import Flask, request, jsonify
from agent import call_agent
from assemblyAI import stop_event

app = Flask(__name__)

@app.route("/agentcall", methods=['POST'])
def agent():
    data = request.json
    result = call_agent()

    if result == 0:
        print("Received response from Agent")

    else:
        print(f"There was an error in Agent response. Error Code: {result}")

    return jsonify({'result': result})

@app.route("/stoprecording", methods=['POST'])
def stop():
    stop_event.set()
    return jsonify({'message': 'Recording stopped'})
 
# app.run(port=5000)
if __name__ == "__main__":
    app.run(port=5000, threaded=True)
