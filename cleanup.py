#!/usr/bin/env python3
import shutil
from pathlib import Path
import sys

# ---------------------------------------------------------
# Path resolution (authoritative)
# ---------------------------------------------------------
THIS_FILE = Path(__file__).resolve()

PROJECT_ROOT = THIS_FILE.parents[1]          # <project-root>
ML_ROOT = PROJECT_ROOT / "ml-test-synthesis"

DATA_DIR = ML_ROOT / "data"
TRAIN_FILE = DATA_DIR / "train" / "long_method_training_dataset.csv"
VALID_FILE = DATA_DIR / "validation" / "long_method_validation_dataset.csv"
PROCESSED_DIR = DATA_DIR / "processed"

MODELS_DIR = ML_ROOT / "models"
WORKSPACE_DIR = PROJECT_ROOT / "workspace"

# ---------------------------------------------------------
# Helpers
# ---------------------------------------------------------
def remove_path(path: Path):
    if not path.exists():
        print(f"⚠️  NOT FOUND: {path}")
        return

    if path.is_file():
        print(f"🗑️  Removing file: {path}")
        path.unlink()
    elif path.is_dir():
        print(f"🗑️  Removing directory: {path}")
        shutil.rmtree(path)


def remove_dir_contents_preserve_gitkeep(dir_path: Path):
    if not dir_path.exists():
        print(f"⚠️  Directory not found: {dir_path}")
        return

    for p in dir_path.iterdir():
        if p.name == ".gitkeep":
            print(f"🔒 Preserving: {p}")
            continue
        remove_path(p)

# ---------------------------------------------------------
# Cleanup logic
# ---------------------------------------------------------
def main():
    print("🧭 cleanup.py location :", THIS_FILE)
    print("🧭 project root        :", PROJECT_ROOT)
    print("🧭 ml-test-synthesis   :", ML_ROOT)
    print()

    # Hard sanity check
    if not ML_ROOT.exists() or not DATA_DIR.exists():
        print("❌ FATAL: ml-test-synthesis layout not detected correctly.")
        sys.exit(1)

    print("⚠️  WARNING: Destructive cleanup operation")
    print("This will DELETE:")
    print(f" - {TRAIN_FILE}")
    print(f" - {VALID_FILE}")
    print(" - contents of ml-test-synthesis/data/processed/ (except .gitkeep)")
    print(" - coverage artifacts under ml-test-synthesis/data/")
    print(" - contents of ml-test-synthesis/models/ (except .gitkeep)")
    print(" - entire <project-root>/workspace/\n")

    resp = input("Type 'yes' to continue: ").strip().lower()
    if resp != "yes":
        print("❌ Aborted. No files were deleted.")
        return

    print("\n🧹 Cleaning project artifacts...\n")

    # 1️⃣ Training / validation datasets
    remove_path(TRAIN_FILE)
    remove_path(VALID_FILE)

    # 2️⃣ Clean processed directory contents (preserve folder + .gitkeep)
    remove_dir_contents_preserve_gitkeep(PROCESSED_DIR)

    # 3️⃣ Remove coverage artifacts under data/
    for pattern in ["*_coverage.json", "coverage.json", ".coverage"]:
        for p in DATA_DIR.rglob(pattern):
            remove_path(p)

    # 4️⃣ Clean models directory contents (preserve folder + .gitkeep)
    remove_dir_contents_preserve_gitkeep(MODELS_DIR)

    # 5️⃣ Remove entire workspace
    remove_path(WORKSPACE_DIR)

    print("\n✨ Cleanup complete. Fresh pipeline ready.")

# ---------------------------------------------------------
if __name__ == "__main__":
    main()
