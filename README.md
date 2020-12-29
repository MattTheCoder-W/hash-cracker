##Hash Cracker - MD5
    
Using this script you can brute force any MD5 hashed password/text!

To get started firstly install all requirements specified in *requirements.txt* file:

> pip install requirements.txt

Then simply run program by typing:

![cmd line](https://raw.githubusercontent.com/MattTheCoder-W/hash-cracker/main/.github/cmd1.png)

> python main.py -p HASHED -d DICTIONARY [-v] [--hash TEXT]

Two last arguments are optional.

Arguments stands for:

| Argument | Description |
| --- | --- |
| `-p` | Hashed password to break |
| `-d` | Dictionary with list of possible passwords |
| `-v` | Verbose mode |
| `--hash` | this will display hashed version of given text |

### When brute forcing is completed you will see:

*(With your cracked password ofcourse ;D)*

![finished](https://raw.githubusercontent.com/MattTheCoder-W/hash-cracker/main/.github/cmd2.png)
