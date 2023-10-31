from jsonparser import JsonParser, JsonException
import argparse

parser = argparse.ArgumentParser(description='Json Parser')
parser.add_argument("file")
args = parser.parse_args()

json_parser = JsonParser()

file = args.file
with open(file) as f:
    s = f.read()

    try:
        result = json_parser.parse_json(s)
    except JsonException as e:
        import sys
        print("The program failed with an error.")
        print(f"[ERROR] - {e}", file=sys.stderr)
        sys.exit(1)

    print(result)

