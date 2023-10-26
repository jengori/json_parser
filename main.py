from jsonparser import JsonParser

json_parser = JsonParser()

file = input("Enter a file name: ")
with open(file) as f:
    s = f.read()
    print(json_parser.parse_json(s))
