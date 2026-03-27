from flask import Flask, render_template, request, jsonify
from solver import solve_lagrange
import google.generativeai as genai

app = Flask(__name__)


# Users will need to put their own Gemini API key here
genai.configure(api_key="YOUR_API_KEY_HERE")

model = genai.GenerativeModel("gemini-2.5-flash")

@app.route('/')
def home():
    return render_template('index.html')

# ================================
# SOLVE ROUTE
# ================================
@app.route('/solve', methods=['POST'])
def solve():
    try:
        data = request.json

        objective = data.get('objective')
        constraint = data.get('constraint')
        mode = data.get('mode')

        result = solve_lagrange(objective, constraint, mode)

        # 🔥 GENERATE AI EXPLANATION
        explanation = ""
        try:
            prompt = f"""
            Solve using Lagrange multipliers.
            Objective: {objective}
            Constraint: {constraint}
            Solution: {result}
            Explain step-by-step in simple terms.
            """

            response = model.generate_content(prompt)

            if hasattr(response, "text") and response.text:
                explanation = response.text
            else:
                explanation = "No explanation generated."

        except Exception as e:
            print("Explanation error:", e)
            explanation = "⚠️ Could not generate explanation"

        return jsonify({
            "solution": result,
            "explanation": explanation
        })

    except Exception as e:
        print("🚨 SERVER CRASH:", e)
        # ✅ FIXED: This safely handles errors without crashing Python
        return jsonify({
            "solution": {"error": f"Invalid math equation: {str(e)}"},
            "explanation": "No explanation generated."
        })

# ================================
# CHATBOT ROUTE (GEMINI)
# ================================
@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message')

        if not user_message:
            return jsonify({"reply": "Please type something."})

        prompt = f"""
        You are a helpful math assistant.
        Answer clearly and simply.
        Question:
        {user_message}
        """

        response = model.generate_content(prompt)

        if hasattr(response, "text") and response.text:
            reply = response.text
        else:
            reply = "⚠️ No response from AI"

        return jsonify({"reply": reply})

    except Exception as e:
        print("🔥 GEMINI ERROR:", e)
        return jsonify({"reply": f"⚠️ Error: {str(e)}"})

# ================================
# ================================
# RUN APP
# ================================
if __name__ == '__main__':
    # Changed to 5005 to dodge the background "ghost" process!
    app.run(debug=True, port=5005)