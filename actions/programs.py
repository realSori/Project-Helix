import subprocess

def run_program(process: str):
    subprocess.Popen(process)
    return f"Program {process} foi aberto com sucesso!"

def close_program(process: str):
    subprocess.call(["taskkill", "/F", "/IM", process])
    return f"Programa {process} foi fechado com sucesso!"

def check_program_running(process: str):
    try:
        output = subprocess.check_output(["tasklist", "/FI", f"IMAGENAME eq {process}"])
        if process in output.decode():
            return f"O programa {process} está em execução."
        else:
            return f"O programa {process} não está em execução."
    except subprocess.CalledProcessError:
        return f"Erro ao verificar o status do programa {process}."
