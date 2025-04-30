import subprocess
import time
import os
import sys

EXAMPLES_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(EXAMPLES_DIR)

# Dynamically find all .py files in the examples directory, except this script itself
EXAMPLES = [
    f for f in os.listdir(EXAMPLES_DIR)
    if f.endswith('.py') and f != os.path.basename(__file__)
]

print("TextFlowThon Showoff: Running all example scripts...")
print("Starting in 3 seconds. Press Ctrl+C to cancel.")
time.sleep(3)

for ex in sorted(EXAMPLES):
    ex_path = os.path.join(EXAMPLES_DIR, ex)
    print(f"\n--- Running: {ex} ---\n")
    env = os.environ.copy()
    env["PYTHONPATH"] = PROJECT_ROOT + os.pathsep + env.get("PYTHONPATH", "")
    subprocess.run([sys.executable, ex_path], cwd=EXAMPLES_DIR, env=env)
    print(f"\n--- Finished: {ex} ---\n")

print("\nAll examples complete!")
