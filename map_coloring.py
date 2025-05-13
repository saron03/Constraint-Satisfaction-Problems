# horn_map_coloring.py
# Constraint Satisfaction Problem: Horn of Africa Map Coloring
# Uses a backtracking algorithm to assign colors to countries such that no neighboring countries share the same color.
# Written by: 
#       Saron Yitbareck 
#       UGR/3774/15


# Four available colors as required by the problem
available_shades = ["Red", "Green", "Blue", "Yellow"]

# Countries in the Horn of Africa region
region_countries = [
    "Ethiopia", "Kenya", "Sudan", "Somalia", 
    "Eritrea", "Djibouti", "South Sudan"
]

# Define which countries share borders (neighbor relationships)
neighbors = {
    "Ethiopia": ["Eritrea", "Djibouti", "Somalia", "Kenya", "Sudan", "South Sudan"],
    "Kenya": ["Ethiopia", "Somalia", "South Sudan"],
    "Sudan": ["Ethiopia", "Eritrea", "South Sudan"],
    "Somalia": ["Ethiopia", "Kenya", "Djibouti"],
    "Eritrea": ["Ethiopia", "Sudan", "Djibouti"],
    "Djibouti": ["Ethiopia", "Eritrea", "Somalia"],
    "South Sudan": ["Ethiopia", "Sudan", "Kenya"]
}

# Dictionary to store color assignments for each country
color_assignments = {}

# Checks if a color can be assigned to a country without conflicting with its neighbors
# Returns True if the color is valid, False otherwise
def satisfies_constraints(target_country, chosen_color):
    for neighbor in neighbors[target_country]:
        if neighbor in color_assignments and color_assignments[neighbor] == chosen_color:
            return False
    return True

# Recursive backtracking algorithm to assign colors to all countries
# Returns True if a valid coloring is found, False if no solution exists
def assign_colors():
    if len(color_assignments) == len(region_countries):
        return True  # All countries have been colored

    # Choose the next uncolored country
    for country in region_countries:
        if country not in color_assignments:
            for color in available_shades:
                if satisfies_constraints(country, color):
                    color_assignments[country] = color
                    # Recursively attempt to color remaining countries
                    if assign_colors():
                        return True
                    # Backtrack by removing the color assignment
                    del color_assignments[country]
            return False  # No valid color found for this country
    return True

# Execute the coloring algorithm and display results
# Prints each country and its assigned color, or an error message if no solution is found
if assign_colors():
    print("Valid map coloring found:\n")
    for country in region_countries:
        print(country + " → " + color_assignments[country])

else:
    print("No valid coloring configuration could be found.")
