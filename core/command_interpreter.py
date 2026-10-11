import re

from actions.directories  import create_directory, create_file

text = input("Comando: ")

PATTERNS = [
    (
        re.compile(r"^(?:crie|criar|cria)\s+uma\s+pasta|diretorio\s+chamada\s+(.+)$", re.IGNORECASE),
        create_directory,
    ),
    (
        re.compile(r"^(?:crie|criar|cria)\s+um\s+arquivo\s+chamado\s+(.+)$", re.IGNORECASE),
        create_file,
    ),
]


def interpret_command(text: str) -> str:
    text = text.strip()

    for pattern, action in PATTERNS:
        match = pattern.fullmatch(text)

        if match:
            argument = match.group(1)
            return action(argument)

    return "Comando não reconhecido."


if __name__ == "__main__":
    while True:
        text = input("Comando: ")

        if text.strip().lower() in {"sair", "exit"}:
            break

        print(interpret_command(text))