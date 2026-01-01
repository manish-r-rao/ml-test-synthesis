import subprocess
import sys
from pathlib import Path

from config.paths import PROJECT_ROOT

def run(script: Path):
    print(f"→ Running {script.name}")
    subprocess.run([sys.executable, str(script)], check=True)

def main():
    print("🛠 Step 1: Building Training Dataset...")
    run(PROJECT_ROOT / "ml" / "build_training_dataset.py")

    print("🛠 Step 2: Building Validation Dataset...")
    run(PROJECT_ROOT / "ml" / "build_validation_dataset.py")

    print("🧠 Step 3: Training Model...")
    run(PROJECT_ROOT / "ml" / "train_model.py")

    print("🔮 Step 4: Running Inference...")
    run(PROJECT_ROOT / "ml" / "inference.py")

    print("📊 Step 5: Running Post-ML Analysis Pipeline...")
    run(PROJECT_ROOT / "analysis" / "from_ml.py")

    print("✅ All steps completed successfully!")

if __name__ == "__main__":
    main()
