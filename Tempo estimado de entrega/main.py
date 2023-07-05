import sys

print('Digite o nome do restaurante')
nomeRestaurante = sys.stdin.readline()

print('Digite o tempo de entrega (em minutos)')
tempoEstimadoEntrega = int(sys.stdin.readline())

print(f"O restaurante {nomeRestaurante} entrega em {tempoEstimadoEntrega} minutos.")


