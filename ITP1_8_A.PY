data = [
  "fAIR, LATER, OCCASIONALLY CLOUDY.",
]

def input():
  return data.pop(0)

input_string = input()
separated_input_strings = list(input_string)


for i in range(0, len(separated_input_strings)):
  if separated_input_strings[i].islower():
    separated_input_strings[i] = separated_input_strings[i].upper()
  elif separated_input_strings[i].isupper():
    separated_input_strings[i] = separated_input_strings[i].lower()
    
print("".join(list(separated_input_strings)))