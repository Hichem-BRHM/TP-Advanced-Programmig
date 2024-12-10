"""
# solution 1.........................................................................

nmbr_people = int(input("How many people need a ride? "))
nmbr_poeple_1taxi = int(input("How many people fit in one taxi? "))

if nmbr_people % nmbr_poeple_1taxi == 0:
    print(f"Number of taxis needed: {nmbr_people // nmbr_poeple_1taxi}")
else :
    print(f"Number of taxis needed: {nmbr_people // nmbr_poeple_1taxi +1}")
    
"""

# solutin 2 ........................................................................

# Ask the user how many people need a ride
nmbr_people = int(input("How many people need a ride? "))

# Ask the user how many people fit in one taxi
nmbr_poeple_1taxi = int(input("How many people fit in one taxi? "))

# Calculate the number of taxis needed
taxis_needed = (nmbr_people + nmbr_poeple_1taxi - 1) // nmbr_poeple_1taxi 

# Print the number of taxis required
print(f"Number of taxis needed: {taxis_needed}")
