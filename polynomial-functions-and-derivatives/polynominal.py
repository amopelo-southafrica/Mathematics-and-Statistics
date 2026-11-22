
# Get user input
coefficient = float(input("Enter the coefficient of x: "))
power = float(input("Enter the power to raise x: "))
x_value = float(input("Enter the x-coordinate of the point where you would like to calculate the gradient: "))

# Apply the power rule: d/dx (a*x^n) = a*n*x^(n-1)
new_coefficient = coefficient * power
new_power = power - 1

# Calculate the gradient at the given x value
gradient = new_coefficient * (x_value ** new_power)

# Display results
print(f"The derivative of the polynomial {int(coefficient)}x^{int(power)} is {int(new_coefficient)}x^{int(new_power)}.")
print(f"The gradient at the point x = {x_value} is {int(gradient)}.")