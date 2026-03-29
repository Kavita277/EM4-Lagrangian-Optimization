import sympy as sp
import numpy as np
import plotly.graph_objects as go

def solve_lagrange(objective_str, constraint_str, mode):
    try:
        original_objective = sp.sympify(objective_str)
        constraint = sp.sympify(constraint_str)

        variables = sorted(
            list(original_objective.free_symbols.union(constraint.free_symbols)),
            key=lambda x: str(x)
        )

        if not variables:
            return {"error": "No variables detected"}

        lam = sp.symbols('lam')
        objective = original_objective if mode != "min" else -original_objective
        L = objective + lam * constraint

        equations = [sp.diff(L, var) for var in variables]
        equations.append(sp.diff(L, lam))

        solutions = sp.solve(equations, variables + [lam], dict=True)

        if not solutions:
            return {"error": "No solution found"}

        sol = solutions[0]
        Z_val = original_objective.subs(sol)

        result = {}
        for var in variables:
            result[str(var)] = float(sol[var])
        result["Z"] = float(Z_val)

        
        try:
            if len(variables) == 3:
                x_var, y_var, z_var = variables[0], variables[1], variables[2]
                x_opt, y_opt, z_opt = float(sol[x_var]), float(sol[y_var]), float(sol[z_var])

                # Solve constraint for the 3rd variable to plot the surface plane
                z_exprs = sp.solve(constraint, z_var)
                if z_exprs:
                    z_expr = z_exprs[0]
                    
                    # Create grid for X and Y axes
                    x_vals = np.linspace(x_opt - 5, x_opt + 5, 50)
                    y_vals = np.linspace(y_opt - 5, y_opt + 5, 50)
                    X, Y = np.meshgrid(x_vals, y_vals)

                    # Calculate Z values on the constraint plane
                    z_func = sp.lambdify((x_var, y_var), z_expr, 'numpy')
                    Z_grid = z_func(X, Y)
                    if isinstance(Z_grid, (int, float)): Z_grid = np.full_like(X, Z_grid)

                    # Calculate Objective Function Value to color the plane
                    obj_func = sp.lambdify((x_var, y_var, z_var), original_objective, 'numpy')
                    Color_grid = obj_func(X, Y, Z_grid)
                    if isinstance(Color_grid, (int, float)): Color_grid = np.full_like(X, Color_grid)

                    fig = go.Figure()

                    # Plot the Constraint Plane (colored by Objective Value)
                    # Plot the Constraint Plane (colored by Objective Value)
                    fig.add_trace(go.Surface(
                        x=X, y=Y, z=Z_grid,
                        surfacecolor=Color_grid,
                        colorscale='electric', 
                        opacity=0.8,
                        name='Constraint Plane',
                        colorbar=dict(
                            title=dict(text="Objective (Z)", font=dict(color="white")), 
                            tickfont=dict(color="white")
                        )
                    ))

                    # Plot the Optimal Solution Point
                    fig.add_trace(go.Scatter3d(
                        x=[x_opt], y=[y_opt], z=[z_opt],
                        mode='markers',
                        marker=dict(size=8, color='#ff0055', symbol='diamond'),
                        name='Optimal Point'
                    ))

                    fig.update_layout(
                        title=dict(text="3D Lagrange Landscape (Drag to Rotate)", font=dict(color='white')),
                        scene=dict(
                            xaxis_title=str(x_var),
                            yaxis_title=str(y_var),
                            zaxis_title=str(z_var),
                            xaxis=dict(gridcolor="rgba(255,255,255,0.2)", backgroundcolor="rgba(0,0,0,0)"),
                            yaxis=dict(gridcolor="rgba(255,255,255,0.2)", backgroundcolor="rgba(0,0,0,0)"),
                            zaxis=dict(gridcolor="rgba(255,255,255,0.2)", backgroundcolor="rgba(0,0,0,0)")
                        ),
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)',
                        margin=dict(l=0, r=0, b=0, t=40)
                    )

                    result["plotly_json"] = fig.to_json()

            elif len(variables) == 2:
                # Fallback for 2 Variables (Plots X, Y, and Objective as Z)
                x_var, y_var = variables[0], variables[1]
                x_opt, y_opt = float(sol[x_var]), float(sol[y_var])
                z_opt = float(Z_val)

                x_vals = np.linspace(x_opt - 5, x_opt + 5, 50)
                y_vals = np.linspace(y_opt - 5, y_opt + 5, 50)
                X, Y = np.meshgrid(x_vals, y_vals)

                obj_func = sp.lambdify((x_var, y_var), original_objective, 'numpy')
                Z_grid = obj_func(X, Y)
                if isinstance(Z_grid, (int, float)): Z_grid = np.full_like(X, Z_grid)

                fig = go.Figure()
                fig.add_trace(go.Surface(x=X, y=Y, z=Z_grid, colorscale='electric', opacity=0.8)) 
                fig.add_trace(go.Scatter3d(
                    x=[x_opt], y=[y_opt], z=[z_opt],
                    mode='markers', marker=dict(size=8, color='#ff0055', symbol='diamond'), name='Optimal Point'
                ))
                fig.update_layout(
                    title=dict(text="3D Objective Surface (Drag to Rotate)", font=dict(color='white')),
                    scene=dict(xaxis_title=str(x_var), yaxis_title=str(y_var), zaxis_title="Objective (Z)"),
                    paper_bgcolor='rgba(0,0,0,0)'
                )
                result["plotly_json"] = fig.to_json()

        except Exception as graph_e:
            print("Plotly Graphing error:", graph_e)
            pass

        return result

    except Exception as e:
        return {"error": str(e)}
