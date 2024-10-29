# Testing the model

# 2. Test within the script by using subprocess
import subprocess
shell_script = "./curl.sh"

# 3. Run the shell script using subprocess
try:
    result = subprocess.run([shell_script], capture_output=True, text=True, check=True)
    print("Shell script output:\n", result.stdout)
except subprocess.CalledProcessError as e:
    print("Error occurred:\n", e.stderr)
