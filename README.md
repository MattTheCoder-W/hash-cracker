##Hash Cracker - MD5
    
Using this script you can brute force any MD5 hashed password/text!

To get started firstly install all requirements specified in *requirements.txt* file:

> pip install requirements.txt

Then simply run program by typing:

> python main.py -p HASHED -d DICTIONARY [-v] [--hash TEXT]

Two last arguments are optional.

Arguments stands for:

| Argument | Description |
| --- | --- |
| `-p` | Hashed password to break |
| `-d` | Dictionary with list of possible passwords |
| `-v` | Verbose mode |
| `--hash` | this will display hashed version of given text |
