# peppy
 Python Implementation of the Pepp*erdine Esoteric Programming Language
 https://esolangs.org/wiki/Pepp*erdine
 
 Code is mostly adapted from https://github.com/kosayoda/chickenpy/

 Pepp*erdine is a language in which the only valid tokens are "pep", "erdine", "\n", and concatenations of 'p' with itself. 
 'pep' is the start command, 'erdine' is the halt command. Each line of a .ppd program corresponds to an opcode denoted
 by the number of 'p' characters in that line. This is directly analogous to the Chicken esolang by Torbjörn Söderstedt.
 You can read more about the implementation of chicken here: https://esolangs.org/wiki/Chicken


# Install

I am currently getting acquainted with PyPl, so until I figure it out please use this by cloning the repository. Once the repository is cloned and all required dependencies are installed, you can write a source .ppd file and run it using:

```
$ poetry install
$ poetry run peppy -f path
```

# Dependencies & Requirements

- [Click](https://github.com/pallets/click)
- [Poetry](https://github.com/python-poetry/poetry)

# Examples

Example programs can be found in the example directory. 




 
