import keyword
import string

punct = set(string.punctuation) - {'_'}
test_data = ["_", "__", "___", "import", "Value", "x", "get_value", "get!value", "some_super_puper_value", "3m", "m3", "assert", "assert_exception"]

for test_variable_name in test_data:
    if test_variable_name in keyword.kwlist:
        print(f"incorrect test variable name: {test_variable_name}")
        continue
    if any(character in punct for character in test_variable_name):
        print(f"incorrect test variable name: {test_variable_name}")
        continue
    if '__' in test_variable_name:
        print(f"incorrect test variable name: {test_variable_name}")
        continue
    if test_variable_name != test_variable_name.lower():
        print(f"incorrect test variable name: {test_variable_name}")
        continue
    if test_variable_name[0].isdigit() :
        print(f"incorrect test variable name: {test_variable_name}")
        continue

    else:
       print(f"correct test variable name: {test_variable_name}")
