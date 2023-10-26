# JSON Parser

### A JSON parser built using Python

This is a response to John Crickett's Write Your Own JSON Parser Coding Challenge.

See the challenge specification [here](https://codingchallenges.fyi/challenges/challenge-json-parser).

 

### To run the program in the Python console (e.g. in Pycharm)
- execute main.py
- input name of file containing the JSON to be parsed
- program will return the parsed JSON if valid; otherwise an exception will be raised.

### To use the command line interface (in virtual environment)
- First install the argparse module: `pip install argparse` and create a virtual environment
- In the terminal, enter `python pyparse.py [filename]` (replacing [filename] with the name of the file containing the JSON to be parsed
- program will return the parsed JSON if valid; otherwise an exception will be raised
- This can be tested using the provided files validjson.json (enter command `python pyparse.py validjson.json`) and invalidjson.json (enter command `python pyparse.py invalidjson.json`)

### testing.py
In the file testing.py, you can see how the program was tested against the test suite from http://www.json.org/JSON_checker
