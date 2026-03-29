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



### Mode
* max → for maximization
* min→ for minimization

## How to Run the Project

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

## Conclusion

This project demonstrates how mathematical optimization techniques like the **Lagrangian Method** can be effectively implemented using programming. It bridges the gap between theoretical concepts and practical applications through an interactive and user-friendly interface.
