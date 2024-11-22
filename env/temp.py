import re

# Load the environment.yml file
with open("environment.yaml", "r") as file:
    lines = file.readlines()

# Remove build strings
updated_lines = []
for line in lines:
    # Use regex to remove build strings after the version (if present)
    updated_line = re.sub(r"(=.+?)=.*", r"\1", line)
    updated_lines.append(updated_line)

# Save the updated environment.yml file
with open("environment_updated.yml", "w") as file:
    file.writelines(updated_lines)

print("Build strings removed. Updated file saved as 'environment_updated.yml'.")
