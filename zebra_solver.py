from constraint import Problem

def zebra_puzzle():
    # Initialize problem
    problem = Problem()
    
    # Define domains for each house (positions 1 through 5)
    houses = range(1, 6)
    
    # Add variables (Color, Nationality, Drink, Pet, Cigarette brand) for each house
    problem.addVariables(['Red', 'Green', 'Ivory', 'Yellow', 'Blue'], houses)
    problem.addVariables(['Englishman', 'Spaniard', 'Ukrainian', 'Norwegian', 'Japanese'], houses)
    problem.addVariables(['Tea', 'Coffee', 'Milk', 'Orange Juice', 'Water'], houses)
    problem.addVariables(['Dog', 'Snails', 'Fox', 'Horse', 'Zebra'], houses)
    problem.addVariables(['Old Gold', 'Kools', 'Chesterfields', 'Lucky Strike', 'Parliaments'], houses)

    # Constraints based on clues
    problem.addConstraint(lambda e, r: e == r, ('Englishman', 'Red'))  # 1. The Englishman lives in the red house.
    problem.addConstraint(lambda s, d: s == d, ('Spaniard', 'Dog'))    # 2. The Spaniard owns the dog.
    problem.addConstraint(lambda u, t: u == t, ('Ukrainian', 'Tea'))   # 3. The Ukrainian drinks tea.
    problem.addConstraint(lambda g, c: g == c - 1, ('Green', 'Ivory')) # 4. The green house is immediately to the right of the ivory house.
    problem.addConstraint(lambda g, c: g == c, ('Green', 'Coffee'))    # 5. The man who drinks coffee lives in the green house.
    problem.addConstraint(lambda o, k: o == k, ('Old Gold', 'Snails')) # 6. The Old Gold smoker owns snails.
    problem.addConstraint(lambda y, k: y == k, ('Yellow', 'Kools'))    # 7. Kools are smoked in the yellow house.
    problem.addConstraint(lambda n: n == 1, ('Norwegian',))            # 8. The Norwegian lives in the first house.
    problem.addConstraint(lambda m: m == 3, ('Milk',))                 # 9. Milk is drunk in the middle house.
    problem.addConstraint(lambda c, f: abs(c - f) == 1, ('Chesterfields', 'Fox'))  # 10. The man who smokes Chesterfields lives next to the man with the fox.
    problem.addConstraint(lambda k, h: abs(k - h) == 1, ('Kools', 'Horse'))        # 11. Kools are smoked in the house next to the house where the horse is kept.
    problem.addConstraint(lambda l, o: l == o, ('Lucky Strike', 'Orange Juice'))   # 12. The Lucky Strike smoker drinks orange juice.
    problem.addConstraint(lambda j, p: j == p, ('Japanese', 'Parliaments'))        # 13. The Japanese smokes Parliaments.
    problem.addConstraint(lambda n, b: abs(n - b) == 1, ('Norwegian', 'Blue'))     # 14. The Norwegian lives next to the blue house.
    
    # Solve the problem
    solution = problem.getSolution()
    
    return solution

# Get the result
result = zebra_puzzle()

# Print result
if result:
    for key, value in result.items():
        print(f"{key}: House {value}")
else:
    print("No solution found.")
