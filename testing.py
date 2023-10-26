from jsonparser import JsonParser
parser = JsonParser()
print("Testing against test suite from http://www.json.org/JSON_checker/\n")
# invalid json tests
print("Tests for invalid JSON")
print("======================")
tests_passed = 0

for n in range(1, 33):
    file = f"test_suite/fail{n}.json"
    with open(file) as f:
        s = f.read()
        try:
            result = parser.parse_json(s)
            print(f"Test {n} FAILED: Did not recognise invalid json, parsed test file content as: {result}")

        except Exception as e:
            print(f"Test {n} PASSED: Recognised invalid json, exception: {e}")
            tests_passed += 1

print(f"\nPASSED {tests_passed}/32 TESTS")

# Valid json tests
print("Tests for valid JSON")
print("======================")

tests_passed = 0

for n in range(1, 4):
    file = f"test_suite/pass{n}.json"
    with open(file) as f:
        s = f.read()
        try:
            result = parser.parse_json(s)
            print(f"Test {n} PASSED: Parsed valid json, parsed test file content as: {result}")
            tests_passed += 1

        except Exception as e:
            print(f"Test {n} FAILED: Failed to parse valid json, exception: {e}")

print(f"\nPASSED {tests_passed}/3 TESTS")
