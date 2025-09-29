from pathlib import Path

def init_project(project_name: str):
    base_dir = Path("projects")
    project_path = base_dir / project_name

    # subfolders we always want
    subfolders = ["images", "animations", "audio"]

    # make the base + subfolders
    (project_path).mkdir(parents=True, exist_ok=True)
    for sub in subfolders:
        (project_path / sub).mkdir(parents=True, exist_ok=True)

    # pre-create empty files if they don't exist
    for filename in ["script.txt", "beats.txt", "prompts.txt"]:
        file_path = project_path / filename
        if not file_path.exists():
            file_path.write_text("")

    print(f"Projects initialized as {project_path}\n")
    return project_path