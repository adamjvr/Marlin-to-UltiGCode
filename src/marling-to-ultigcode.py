import re
import sys
import argparse

def convert_marlin_to_ultigcode(marlin_gcode):
    """
    Converts Marlin-flavored G-code to UltiGCode flavor.
    
    :param marlin_gcode: List of lines in Marlin G-code
    :return: List of lines in UltiGCode
    """
    # Initialize an empty list to store the converted G-code lines
    ultigcode = []
    
    # Iterate over each line in the input Marlin G-code
    for line in marlin_gcode:
        # Remove comments from the line (anything after a ';' character)
        line = re.sub(r';.*', '', line).strip()
        
        # Skip empty lines after removing comments
        if not line:
            continue

        # Remove temperature setting commands, as UltiGCode handles temperatures separately
        if line.startswith('M104') or line.startswith('M109'):
            continue

        # Convert extrusion length to volumetric extrusion if the line is a movement command
        if line.startswith('G1') and 'E' in line:
            # Search for the extrusion parameter (E) in the line
            match = re.search(r'E(\d+\.\d+)', line)
            if match:
                # Extract the extrusion value and convert it to float
                e_value = float(match.group(1))
                # Convert to volumetric extrusion (this is a placeholder conversion factor)
                e_volumetric = e_value * 1.0
                # Replace the original extrusion value with the volumetric value in the line
                line = line.replace(f'E{e_value}', f'E{e_volumetric}')

        # Append the processed line to the list of UltiGCode lines
        ultigcode.append(line)
    
    # Return the list of converted UltiGCode lines
    return ultigcode

def main(input_file, output_file):
    # Open the input Marlin G-code file for reading
    with open(input_file, 'r') as f:
        # Read all lines from the file
        marlin_gcode = f.readlines()
    
    # Convert the Marlin G-code lines to UltiGCode flavor
    ultigcode = convert_marlin_to_ultigcode(marlin_gcode)
    
    # Open the output file for writing
    with open(output_file, 'w') as f:
        # Write the converted UltiGCode lines to the file
        f.write('\n'.join(ultigcode))
    
    # Print a message indicating that the conversion is complete
    print(f"Conversion complete. Output saved to {output_file}")

if __name__ == "__main__":
    # Set up argument parser for command-line arguments
    parser = argparse.ArgumentParser(description='Convert Marlin-flavored G-code to UltiGCode flavor.')
    # Add argument for the input file
    parser.add_argument('input_file', type=str, help='The input Marlin G-code file to be converted')
    # Add argument for the output file
    parser.add_argument('output_file', type=str, help='The output file for the converted UltiGCode')
    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Call the main function with the parsed input and output file arguments
    main(args.input_file, args.output_file)
