import os
import sys

from rich import print as rprint

# This script creates a new external service folder structure for a FastAPI project.
# Usage: python add_external_service.py <external_service_name> e.g aws, gcs, supabase

if len(sys.argv) < 2:
    rprint(f"[red]Usage:[/red] {sys.argv[0]} <external_service_name>")
    sys.exit(1)

service_name = sys.argv[1]
folder_path = os.path.join("src", service_name)
test_folder_path = os.path.join("tests", service_name)

os.makedirs(folder_path, exist_ok=True)
os.makedirs(test_folder_path, exist_ok=True)

files = [
    "client.py",  # client model for external service communication
    "schemas.py",
    "config.py",
    "constants.py",
    "exceptions.py",
    "utils.py",
    "__init__.py",
]

for file in files:
    folder_file_path = os.path.join(folder_path, file)
    if os.path.exists(folder_file_path):
        rprint(f"[yellow]File already exists:[/yellow] {file} in {folder_path}")
        continue
    with open(folder_file_path, "w") as f:
        rprint(f"[blue]Creating file:[/blue] {folder_file_path}")
        f.write("")


rprint(f"[green]Success created folder and files in:[/green] {folder_path}")

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
    f"[green]Success created test folder for {service_name} in:[/green] {test_folder_path}"
)
