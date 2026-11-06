import sys

from backend import run_travel_agent

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

user_input = input("Enter your travel request: ").strip()
if not user_input:
    raise ValueError("Travel request cannot be empty.")

res = run_travel_agent(user_input)
print(res)