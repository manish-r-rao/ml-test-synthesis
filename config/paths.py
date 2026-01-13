from pathlib import Path

# __file__ is <project-root>/ml-test-synthesis/config/paths.py
_this_file = Path(__file__).resolve()

# PROJECT_ROOT = <project-root>/ml-test-synthesis/
PROJECT_ROOT = _this_file.parents[1]

# GLOBAL_ROOT = <project-root>/
GLOBAL_ROOT = PROJECT_ROOT.parent

# WORKSPACE_DIR = <project-root>/workspace/
WORKSPACE_DIR = GLOBAL_ROOT / "workspace"

# TARGET_REPOS_DIR = <project-root>/workspace/target-repos/
TARGET_REPOS_DIR = WORKSPACE_DIR / "target-repos"

# VENVS_DIR = <project-root>/workspace/venvs/
VENVS_DIR = WORKSPACE_DIR / "venvs"

# Data and Models remain inside the project repository
DATA_DIR = PROJECT_ROOT / "data"
TRAINING_DATA_DIR = DATA_DIR / "train"
VALIDATION_DATA_DIR = DATA_DIR / "validation"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
MODELS_DIR = PROJECT_ROOT / "models"

# Repos for dataset
TRAINING_REPOS = {
    "requests": ("https://github.com/psf/requests.git", "v2.31.0"),
    "flask": ("https://github.com/pallets/flask.git", "2.3.3"),
    "click": ("https://github.com/pallets/click.git", "8.1.7"),
    "numpy": ("https://github.com/numpy/numpy.git", "v1.26.4"),
    "django": ("https://github.com/django/django.git", "stable/4.2.x"),
}

VALIDATION_REPOS = {
    "attrs": ("https://github.com/python-attrs/attrs.git", "23.2.0"),
    "jinja2": ("https://github.com/pallets/jinja.git", "3.1.3"),
    "itsdangerous": ("https://github.com/pallets/itsdangerous.git", "2.1.2"),
}