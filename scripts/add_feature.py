import os
import sys

from rich import print as rprint

# This script creates a new feature folder structure for a FastAPI project.
# Usage: python add_feature.py <feature_name>

if len(sys.argv) < 2:
    rprint(f"[red]Usage:[/red] {sys.argv[0]} <feature_name>")
    sys.exit(1)

feature_name = sys.argv[1]
folder_path = os.path.join("src", feature_name)
test_folder_path = os.path.join("tests", feature_name)

os.makedirs(folder_path, exist_ok=True)
os.makedirs(test_folder_path, exist_ok=True)

files = [
    "__init__.py",
    "router.py",
    "schemas.py",
    "models.py",
    "dependencies.py",
    "config.py",
    "constants.py",
    "exceptions.py",
    "service.py",
    "utils.py",
]

for file in files:
    folder_file_path = os.path.join(folder_path, file)
    if os.path.exists(folder_file_path):
        rprint(f"[yellow]File already exists:[/yellow] {file} in {folder_path}")
        continue
    with open(folder_file_path, "w") as f:
        rprint(f"[blue]Creating file:[/blue] {folder_file_path}")
        f.write("")


rprint(f"[green]Success created folder  and files in:[/green] {folder_path}")

test_files = ["conftest.py"]
for test_file in test_files:
    test_file_path = os.path.join(test_folder_path, test_file)
    if os.path.exists(test_file_path):
        rprint(
            f"[yellow]Test file already exists:[/yellow] {test_file} in {test_folder_path}"
        )
        continue
    with open(test_file_path, "w") as f:
        rprint(f"[blue]Creating test file:[/blue] {test_file_path}")
        f.write("")

rprint(
    f"[green]Success created test folder for {feature_name} in:[/green] {test_folder_path}"
)
