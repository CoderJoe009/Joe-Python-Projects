def balance_equation(equation):
  """
  Balances a given chemical equation.

  Args:
      equation: The unbalanced chemical equation as a string.

  Returns:
      The balanced equation as a string, or None if balancing fails.
  """
  # Split the equation into reactants and products
  reactants, products = equation.split("->")
  reactants = reactants.strip().split(" + ")
  products = products.strip().split(" + ")

  # Create a dictionary to store element counts
  element_counts = {}
  for compound in reactants + products:
    # Split compound by coefficients and element
    coeff, element = compound.split(maxsplit=1)
    count = int(coeff) if coeff else 1
    # Update element count in dictionary
    if element in element_counts:
      element_counts[element] += count
    else:
      element_counts[element] = count

  # Check if all elements have equal counts on both sides
  for element, count in element_counts.items():
    if count % len(reactants) != 0:
      return None

  # Balance the equation by finding the least common multiple (LCM) for coefficients
  coefficients = []
  for element, count in element_counts.items():
    lcm = count
    for reactant in reactants:
      coeff, _ = reactant.split(maxsplit=1)
      coeff = int(coeff) if coeff else 1
      if element in reactant:
        lcm = lcm // coeff * coeff if lcm % (coeff * count) else lcm
    coefficients.append(lcm // count)

  # Balance the equation string
  balanced_reactants = []
  for i, reactant in enumerate(reactants):
    coeff = coefficients[i]
    balanced_reactants.append(f"{coeff}{reactant}" if coeff > 1 else reactant)
  balanced_products = []
  for i, product in enumerate(products):
    coeff = coefficients[len(reactants) + i]
    balanced_products.append(f"{coeff}{product}" if coeff > 1 else product)

  return f" + ".join(balanced_reactants) + " -> " + f" + ".join(balanced_products)

# Example usage
equation = "H2 + O2 -> H2O"
balanced_equation = balance_equation(equation)

if balanced_equation:
  print(f"Balanced equation: {balanced_equation}")
else:
  print("Balancing failed!")
