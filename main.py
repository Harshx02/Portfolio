input_file = "static/javascript/script.js"
output_file = "static/javascript/script.js"

with open(input_file, "r", encoding="utf-8") as f:
    lines = [line.lstrip("+-") for line in f]

with open(input_file, "w", encoding="utf-8") as f:
    f.writelines(lines)
