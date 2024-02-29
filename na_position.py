def find_na_positions(word):
    positions = []
    start_index = 0
    
    while True:
        # Find the next occurrence of 'na' starting from the current index
        index = word.find('na', start_index)
        
        # If no more occurrences are found, break the loop
        if index == -1:
            break
        
        # Append the position to the list and update the starting index for the next search
        positions.append(index)
        start_index = index + 2  # Move the starting index to the next position after the current match
    
    return positions

# Example usage
word = 'banananana'  #if u use baNANa, the program will not find na because it is case sensitive
positions = find_na_positions(word)

if positions:
    print(f"The number of 'na' in '{word}' is: {len(positions)}")
    print(f"The positions of 'na' in '{word}' are: {positions}")
else:
    print(f"No occurrences of 'na' found in '{word}'")
