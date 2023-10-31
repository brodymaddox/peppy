#Primarily Adapted From https://github.com/kosayoda/chickenpy/

from peppy_esolang.vm import OPCODE


class ParseError(Exception):
    def __init__(self, message):
        super().__init__(message)


def compile(code: str):
    """Compiles source code into a list of tokens."""
    lines = code.splitlines()
    tokens = []
    for line_no, line in enumerate(lines, start=1):

        # Check for start character
        # There is no requirement in it for running the virtual machine
        if line_no==1 and not line.strip() == 'pep':
            print("Program must start with pep")
            break
        
        #Avoid logic calculation for start character
        if line.strip() == 'pep':
            continue 

        # Check for halt character
        if line.strip() == 'erdine':
            tokens.append(OPCODE.EXIT)
            continue

        words = line.split()
        # Raise syntax error if any word other than 'p' or whitespace is found
        if word_set := {word for word in words if not all(char == 'p' or char == ' ' for char in word)} - {""}:
            raise ParseError(f"Invalid token(s) on line {line_no}: {' '.join(word_set)}")
            return False

        # Count 'p' characters
        num_p = line.count('p')
        # Any number of p's > 9 is used as is
        if num_p > 9:
            tokens.append(num_p)
        else:
            tokens.append(OPCODE(num_p))
    return tokens