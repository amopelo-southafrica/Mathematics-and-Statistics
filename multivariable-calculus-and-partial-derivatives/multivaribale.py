import sympy as sp
x, y = sp.symbols('x y')
f = x**2 + y**2
df_dx = sp.diff(f, x)
df_dy = sp.diff(f, y)

print(f"The gradient vector of the function f = {f} is ∇f = ({df_dx}, {df_dy}).")