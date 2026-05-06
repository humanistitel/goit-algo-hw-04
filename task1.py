import argparse
import shutil
from pathlib import Path


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Recursively copy and sort files by extension into a destination directory."
    )
    parser.add_argument("source", type=Path, help="Path to the source directory")
    parser.add_argument(
        "destination",
        type=Path,
        nargs="?",
        default=Path("dist"),
        help="Path to the destination directory (default: dist)",
    )
    return parser.parse_args()


def read_and_copy(source_dir: Path, destination_dir: Path) -> None:
    try:
        for item in source_dir.iterdir():
            if item.is_dir():
                read_and_copy(item, destination_dir)
            elif item.is_file():
                copy_file(item, destination_dir)
    except PermissionError as e:
        print(f"Permission denied: {e}")
    except OSError as e:
        print(f"Error reading directory {source_dir}: {e}")


def copy_file(file_path: Path, destination_dir: Path) -> None:
    extension = file_path.suffix.lstrip(".").lower() or "no_extension"
    target_dir = destination_dir / extension
    try:
        target_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(file_path, target_dir / file_path.name)
        print(f"Copied: {file_path} -> {target_dir / file_path.name}")
    except PermissionError as e:
        print(f"Permission denied when copying {file_path}: {e}")
    except OSError as e:
        print(f"Error copying file {file_path}: {e}")


def main():
    args = parse_arguments()
    source_dir = args.source
    destination_dir = args.destination

    if not source_dir.exists():
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return
    if not source_dir.is_dir():
        print(f"Error: '{source_dir}' is not a directory.")
        return

    destination_dir.mkdir(parents=True, exist_ok=True)
    read_and_copy(source_dir, destination_dir)
    print(f"\nDone! Files have been sorted into '{destination_dir}'.")


if __name__ == "__main__":
    main()
