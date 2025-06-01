import shutil
from pathlib import Path
import os

def remove_python_artifacts(repo_path):
    # folders to remove (exact names)
    folders_to_remove = [
        "__pycache__",
        "build",
        "dist",
        ".pytest_cache",
        ".mypy_cache",
        ".tox",
        ".coverage"
    ]

    # glob patterns for files/folders
    file_patterns = ["*.pyc", "*.pyo", "*.pyd"]
    egg_info_pattern = "*.egg-info"

    # Remove exact folders
    for folder_name in folders_to_remove:
        for folder_path in repo_path.rglob(folder_name):
            if folder_path.is_dir():
                try:
                    shutil.rmtree(folder_path)
                    print(f"Deleted directory: {folder_path}")
                except Exception as e:
                    print(f"Failed to delete {folder_path}: {e}")

    # Remove files by pattern
    for pattern in file_patterns:
        for file_path in repo_path.rglob(pattern):
            if file_path.is_file():
                try:
                    file_path.unlink()
                    print(f"Deleted file: {file_path}")
                except Exception as e:
                    print(f"Failed to delete file {file_path}: {e}")

    # Remove egg-info folders
    for egg_info_folder in repo_path.glob(egg_info_pattern):
        if egg_info_folder.is_dir():
            try:
                shutil.rmtree(egg_info_folder)
                print(f"Deleted directory: {egg_info_folder}")
            except Exception as e:
                print(f"Failed to delete {egg_info_folder}: {e}")

def main():
    repo_path = Path.cwd()  # or specify your repo path here

    if not (repo_path / ".git").exists():
        print("Warning: Not a git repository.")
    
    remove_python_artifacts(repo_path)
    print("Cleanup complete.")

if __name__ == "__main__":
    main()

