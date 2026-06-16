
from flask import Flask,render_template,request,jsonify
from flask_cors import CORS
from agent import agent_executor
app=Flask(__name__)
CORS(app)
@app.get("/")
def home(): return render_template("index.html")
@app.post("/chat")
def chat():
    msg=(request.get_json() or {}).get("message","")
    if not msg.strip():
        return jsonify({"error":"Empty message"}),400
    out=agent_executor.invoke({"input":msg})
    return jsonify({"response":out["output"]})
if __name__=="__main__":
    app.run(debug=True)
