# Lagrangian Method Solver (NLPP)

## Overview
This project implements the **Lagrangian Method** to solve **Non-Linear Programming Problems (NLPP)** with one constraint.
It is a **web-based application built using Flask** that allows users to input an objective function and constraint, compute the optimal solution, and visualize results. The system also provides **AI-generated step-by-step explanations** to help users understand the solution process.

## Objective
To develop an interactive application that demonstrates how Lagrange multipliers can be used to solve constrained optimization problems using Python.


## Features
* Solve constrained optimization problems using Lagrange multipliers
* Supports both **maximization** and **minimization**
* Accepts dynamic user input for functions and constraints
* Generates **AI-based explanations** using Gemini API
* Provides **interactive 3D visualization** using Plotly
* Includes a **chatbot assistant** for mathematical queries

## Input Format
### Objective Function

Enter as a valid mathematical expression:

x*y
x**2 + y**2
x*y*z

### Constraint
Must be written in the form:
g(x, y, ...) = 0

Enter as:
* x+y-10
* x+y+z-20

Do NOT use:
* x+y=10 (incorrect)
* 
### Mode
* max → for maximization
* min→ for minimization


## How to Run the Project
  Installation Requirements
- Python 3.8 or above
- pip (Python package manager)

### 1. Clone the Repository
git clone <your-repository-link>
cd EM4-Lagrangian-Optimization

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Add Gemini API Key
Open app.py and replace:

genai.configure(api_key="YOUR_API_KEY_HERE")
with your actual API key.

### 4. Run the Application
python app.py

### 5. Open in Browser
http://127.0.0.1:5005


## Example Usage
### Input:

* Objective: x*y
* Constraint: x+y-10
* Mode:`max

### Output:
* x = 5
* y = 5
* Maximum Value = 25


 ## Working
1. User enters objective function and constraint
2. Input is sent to Flask backend
3. The solver converts expressions using SymPy
4. Lagrangian function is formed
5. Partial derivatives are computed
6. Equations are solved to get optimal values
7. Result is displayed on UI
8. AI generates explanation using Gemini API
9. Plotly generates visualization (if applicable)


## Theory
The Lagrangian Method is used to solve optimization problems with constraints.
A new function called the Lagrangian is formed:
L(x, y, λ) = f(x, y) + λ(g(x, y))

Where:
- f(x, y) is the objective function
- g(x, y) = 0 is the constraint
- λ is the Lagrange multiplier

The optimal solution is obtained by solving:
∂L/∂x = 0  
∂L/∂y = 0  
∂L/∂λ = 0  

This converts a constrained problem into an unconstrained one.


## Project Structure

EM4-Lagrangian-Optimization/
│
├── app.py                 # Flask backend
├── solver.py              # Lagrangian computation logic
├── requirements.txt       # Dependencies
│
├── templates/
│   └── index.html         # Frontend UI
│
├── static/
│   ├── style.css          # Styling
│   ├── script.js          # Frontend logic
│   └── image.png          # Assets
│
├── .gitignore


## Technologies Used

* Python
* Flask
* SymPy
* NumPy
* Plotly
* Google Gemini API

## Notes

* AI explanation feature requires a valid **Gemini API key**
* Ensure all dependencies are installed before running
* Input must follow correct mathematical syntax

## Future Scope

* Extend support to multiple constraints
* Add 2D graph visualization
* Improve UI/UX design
* Deploy application online (Render/Vercel)


## Team Members

*Kavita Gupta
*Shravni Andhale
*Srushti Banugude
*Nikhil Sakpal
*Yash Patil
*Gaurav Ghude

## Contributions

Each team member contributed through GitHub commits, including:
- Backend development
- UI design
- Documentation
- Testing and debugging

## References

- Engineering Mathematics-IV Notes
- SymPy Documentation: https://docs.sympy.org/
- Flask Documentation: https://flask.palletsprojects.com/
- Plotly Documentation: https://plotly.com/python/

## Conclusion

This project demonstrates how mathematical optimization techniques like the **Lagrangian Method** can be effectively implemented using programming. It bridges the gap between theoretical concepts and practical applications through an interactive and user-friendly interface.
