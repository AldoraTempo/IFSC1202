def ParseDegreeString(ddmmss):
    """
    Parses a degree string in the format DD°MM'SS" and returns the degrees, minutes, and seconds.
    
    Inputs:
    ddmmss - A string representing the angle in the format 'DD°MM'SS"'.
    
    Returns:
    degrees - Floating point value of degrees.
    minutes - Floating point value of minutes.
    seconds - Floating point value of seconds.
    """
   
    degree_symbol = chr(176)  
    minute_symbol = "'"
    second_symbol = '"'
    
    degree_pos = ddmmss.index(degree_symbol)
    minute_pos = ddmmss.index(minute_symbol)
    second_pos = ddmmss.index(second_symbol)
    
    degrees = float(ddmmss[:degree_pos].strip())
    minutes = float(ddmmss[degree_pos + 1:minute_pos].strip())
    seconds = float(ddmmss[minute_pos + 1:second_pos].strip())
    
    return degrees, minutes, seconds

def DDMMSStoDecimal(degrees, minutes, seconds):
    """
    Converts degrees, minutes, and seconds to decimal degrees.
    
    Inputs:
    degrees - Floating point value of degrees.
    minutes - Floating point value of minutes.
    seconds - Floating point value of seconds.
    
    Returns:
    decimal_degrees - Floating point value of the decimal degrees.
    """
  
    decimal_degrees = degrees + (minutes / 60) + (seconds / 3600)
    return decimal_degrees

def processFile(input_file, output_file):
    """
    Reads a file containing angles in DD°MM'SS" format, converts them to decimal degrees, and writes the result to another file.
    
    Inputs:
    input_file - The name of the input file containing angles in DD°MM'SS" format.
    output_file - The name of the output file where the decimal degrees will be written.
    """
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            line = line.strip()  
            if line:  
                degrees, minutes, seconds = ParseDegreeString(line)
                
                decimal_degrees = DDMMSStoDecimal(degrees, minutes, seconds)
                
                outfile.write(f"{decimal_degrees}\n")


input_file = 'angles.txt'  
output_file = 'decimal_degrees.txt' 

processFile(input_file, output_file)
