import subprocess


result = subprocess.run(
    'ipconfig',
    capture_output=True,
    text=True
)

print(result.stdout)
print(result.returncode)



# -------- run python code -----------
import sys
subprocess.run([sys.executable,'main_hello.py'])
# ["python","hello.py"] also use

