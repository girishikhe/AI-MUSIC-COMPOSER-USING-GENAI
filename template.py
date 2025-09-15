
import os
from pathlib import Path 

project_name = "app"

list_of_files = [
  f"{project_name}/__init__.py",
  f"{project_name}/main.py",
  f"{project_name}/utils.py",
  f".gitlab-ci.yml",
  "Dockerfile",
  "app.py",
  "requirements.txt",
  "kubernetes-deployment.yaml",
  "requirements.txt",
  "setup.py",
  ".env"
  
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")