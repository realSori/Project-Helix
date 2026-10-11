from pathlib import Path


def create_directory(name: str) -> str:
    path = Path(name)

    if path.exists():
        return f"O caminho já existe: {path}"

    path.mkdir(parents=True)
    return f"Pasta criada: {path}"


def create_file(name: str) -> str:
    path = Path(name)

    if path.exists():
        return f"O arquivo já existe: {path}"

    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch()
    return f"Arquivo criado: {path}"