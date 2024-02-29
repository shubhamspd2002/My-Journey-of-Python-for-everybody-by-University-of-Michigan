fruit = 'banana'
pos = fruit.find('na')
print(pos)

def count_na(word):
    count = 0
    start_index = 0
    
    while True:
        # Find the next occurrence of 'na' starting from the current index
        index = word.find('na', start_index) 
        # If no more occurrences are found, break the loop
        if index == -1:
            break
        print('the positions are : ', index)
        # Increment the count and update the starting index for the next search
        count += 1
        start_index = index + 2  # Move the starting index to the next position after the current match
    
    return count

# Example usage
word = 'banananananana'
result = count_na(word)
print(f"The number of 'na' in '{word}' is: {result}")