def format_input(input_file, output_file):
    # Read the input from the input file
    with open(input_file, 'r') as f:
        input_string = f.read()

    # Format the input
    formatted_input = []
    lines = input_string.strip().split('\n')
    for line in lines:
        vertex, edges = line.split(':')
        formatted_input.append(f"{vertex}: [{', '.join(edges.split())}],\n")
    formatted_content = ''.join(formatted_input)

    # Write the formatted content to the output file
    with open(output_file, 'w') as f:
        f.write(formatted_content)

    print(f"Formatted content has been written to {output_file}")

# Input and output file paths
input_file = input('enter input: ')
input_file = input_file.replace('"', '')
output_file = input('enter output: ')
output_file = output_file.replace('"', '')


# Format the input and write to the output file
format_input(input_file, output_file)
