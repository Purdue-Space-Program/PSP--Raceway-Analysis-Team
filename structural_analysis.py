#this is max i'm a bum at code
#i'm kinda bad at coding so imma just pseudo code this based on the example\

#import math, plotting, optimization, and material libraries 

#

#fatigue_equation

#function: calculate_strains_stresses
#input: loads, material_properties, geometry
#   loop over the segements of the structure grabbing from each part:
#      material_properties, like yield strength 
#      thermal stresses, calculating based on temperature changes
#      Pressure Stresses, stress from internal and bulk pressures
#    combine these stresses(thermal and pressure) to get the total strains
#    use the von mises stress criterion(tough name) to see if it yields
#    use the coffin manson relation and the "custom fatigue equation" to calcluate cycles to failure
#    return the total strains, stresses, and cycles to failure
#    append all those results to arrays for analysis