# Marlin-to-UltiGCode
G-code Converter: Marlin to UltiGCode

This Python script converts G-code files from the Marlin flavor to the UltiGCode flavor. It removes comments, skips temperature setting commands, and converts extrusion length to volumetric extrusion for compatibility with UltiGCode.

## Features

- Removes comments from the G-code.
- Skips temperature setting commands (`M104` and `M109`).
- Converts extrusion length (`E` parameter) to volumetric extrusion.

## Requirements

- Python 3.x

## Usage

To use this script, you need to provide two command-line arguments:

1. The path to the input Marlin G-code file.
2. The path to the output file where the converted UltiGCode will be saved.

### Example

```bash
python convert_gcode.py input_file.gcode output_file.gcode
```

Replace `input_file.gcode` with the path to your Marlin G-code file and `output_file.gcode` with the desired path for the converted UltiGCode file.

### Command-Line Arguments

- `input_file` (str): The input Marlin G-code file to be converted.
- `output_file` (str): The output file for the converted UltiGCode.

### Detailed Description of the Script

#### Script Structure

- **Importing Modules**:
    - `re`: For regular expressions.
    - `sys` and `argparse`: For handling command-line arguments.

- **convert_marlin_to_ultigcode Function**:
    - Converts Marlin G-code to UltiGCode by:
        - Removing comments.
        - Skipping temperature setting commands.
        - Converting extrusion length to volumetric extrusion.

- **main Function**:
    - Reads the input Marlin G-code file.
    - Converts the read lines using `convert_marlin_to_ultigcode`.
    - Writes the converted lines to the output file.

- **Command-line Argument Parsing**:
    - Uses `argparse` to define and parse command-line arguments for the input and output files.
    - Calls `main` with the parsed arguments.

### Additional Notes

- The script assumes a placeholder conversion factor of `1.0` for converting extrusion length to volumetric extrusion. You may need to adjust this factor based on your specific filament diameter and other parameters.
- The script removes all comments and temperature setting commands to match the UltiGCode requirements.

Feel free to modify the script as needed for your specific use case and printer requirements.


## License
Released under GPL V3 License 