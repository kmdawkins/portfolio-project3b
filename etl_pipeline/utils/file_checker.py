import os

def check_file_exists(filepath: str) -> bool:
    """Check if the file exists at the given path."""
    return os.path.isfile(filepath)

def validate_file_extension(filepath: str, allowed_extensions: list) -> bool:
    """Check if the file has a valid extension."""
    _, ext = os.path.splitext(filepath)
    return ext.lower() in [e.lower() for e in allowed_extensions]