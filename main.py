import math
c=299792458

def electric_potential_energy(q, V):
    return q*V

def binding_energy(Z, m_p, m_nucleus):    
    return Z*m_p*c**2 - m_nucleus*c**2

def kinetic_energy(p, m_0):
  return math.sqrt(p**2*c**2 + m_0**2*c**4) - m_0*c**2

def photon_energy(h, f):
  return h*f

def energy_from_mass(m):
  return m*c**2

def combined_equation(m, g, h, q, V, Z, m_p, m_nucleus, p, m_0, h, f):
  E_g = m*g*h
  E_e = q*V
  E_b = Z*m_p*c**2 - m_nucleus*c**2
  E_k = math.sqrt(p**2*c**2 + m_0**2*c**4) - m_0*c**2
  E = h*f
  E_total = E + E_g + E_e + E_b + E_k
  return E_total

###
# Bruteforcing the solution :)
###

import itertools

# Create a list of the characters
# characters = ["E_g", "=", "m","*","g","*","h","E_e", "=", "q","*","V", "E_b", "=", "Z","*","m_p","*","c","**","2", "-", "m_nucleus","*","c","**","2","E_k", "=", "math.sqrt","(","p","**","2","*","c","**","2", "+", "m_0","**","2","*","c","**","4",")", "-", "m_0","*","c","**","2", "E", "=", "h","*","f","E_total", "=", "E", "+", "E_g", "+", "E_e", "+", "E_b", "+", "E_k",]

# Generate all the permutations of length 4 of the characters
# combinations = itertools.permutations(characters, len(characters))

# # Print the combinations
# for combination in combinations:
#     print(combination)

import itertools

def check_equation(equation):
  # Create a list of all possible combinations of operators
  operator_combinations = itertools.product(['+', '-', '*', '/'], repeat=len(equation)-1)

  # Iterate through all operator combinations
  for operator_combo in operator_combinations:
  # Insert the operator combination into the equation
    modified_equation = equation[0]
  for i in range(len(operator_combo)):
    modified_equation += operator_combo[i] + equation[i+1]

  # Try to evaluate the modified equation and catch any exceptions
  try:
    result = eval(modified_equation)
  except:
  # If an exception is raised, it means there is a mathematical error in the equation
    print(f"Error in equation: {modified_equation}")
  else:
  # If no exception is raised, the equation is valid
    print(f"Valid equation: {modified_equation} = {result}")
