def main():
    element = input("Enter an element or a common radical: ")
    val = valency(element)
    if val is not None:
        print(f"The valency of {element} is {val}")
    else:
        print(f"The valency of {element} is not available in the database.")

def valency(element):
    elements = {
        # First 20 elements in the periodic table
        "H": "1",
        "He": "0",
        "Li": "1",
        "Be": "2",
        "B": "3",
        "C": "4",
        "N": "3, 5",
        "O": "2",
        "F": "1",
        "Ne": "0",
        "Na": "1",
        "Mg": "2",
        "Al": "3",
        "Si": "4",
        "P": "3, 5",
        "S": "2, 4, 6",
        "Cl": "1",
        "Ar": "0",
        "K": "1",
        "Ca": "2",
        
        # Additional specific elements
        "Zn": "2",
        "Cu": "1, 2",
        "Pb": "2, 4",
        "Au": "1, 3",
        "Ag": "1",
        
        # Common radicals
        "OH": "-1",
        "SO4": "2",
        "NO3": "-1",
        "CO3": "-2",
        "NH4": "1",
        "PO4": "3",
        "C2H3O2": "-1",
        "HCO3": "-1",
        "HSO4": "-1",
        "CN": "-1",
        "MnO4": "-1",
        "ClO3": "-1",
        "CH3COO": "-1",
        "CLO4": "-1",
        "IO3": "-1"
    }

    val = elements.get(element, None)
    return val

if __name__ == "__main__":
    main()
