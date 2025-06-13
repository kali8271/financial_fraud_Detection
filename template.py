import os

structure = {
    "data": [],
    "notebooks": [],
    "src": [
        "data_loader.py",
        "preprocessing.py",
        "model_training.py",
        "evaluation.py",
        "utils.py",
        "__init__.py"
    ],
    "": ["main.py", "requirements.txt", "README.md"]
}

for folder, files in structure.items():
    if folder and not os.path.exists(folder):
        os.makedirs(folder)
    for file in files:
        filepath = os.path.join(folder, file) if folder else file
        with open(filepath, "w") as f:
            f.write(f"# {file}\n\n")

print("✅ Folders and template files created.")
