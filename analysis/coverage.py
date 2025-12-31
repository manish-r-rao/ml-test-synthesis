import subprocess
import json
import os
from pathlib import Path


class CoverageError(Exception):
    pass


def collect_coverage(repo_path: str) -> dict:
    repo_path = Path(repo_path).resolve()

    if not repo_path.exists():
        raise CoverageError(f"Repo path does not exist: {repo_path}")

    # Run coverage using pytest
    try:
        subprocess.run(
            ["coverage", "run", "-m", "pytest"],
            cwd=repo_path,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except subprocess.CalledProcessError as e:
        raise CoverageError(
            f"Coverage execution failed:\n{e.stderr.decode()}"
        )

    # Generate JSON report
    try:
        subprocess.run(
            ["coverage", "json", "-o", "coverage.json"],
            cwd=repo_path,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except subprocess.CalledProcessError as e:
        raise CoverageError(
            f"Coverage JSON generation failed:\n{e.stderr.decode()}"
        )

    coverage_file = repo_path / "coverage.json"

    if not coverage_file.exists():
        raise CoverageError("coverage.json not generated")

    with open(coverage_file, "r") as f:
        coverage_data = json.load(f)

    return coverage_data