from jsonparser import JsonParser
import argparse

parser = argparse.ArgumentParser(description='Json Parser')
parser.add_argument("file")
args = parser.parse_args()

json_parser = JsonParser()

file = args.file
with open(file) as f:
    s = f.read()
    print(json_parser.parse_json(s))
