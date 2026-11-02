def simular_fila(alunos):
    tempo_atual = 0
    esperas = []
    for nome, duracao in alunos:
        esperas.append((nome, tempo_atual))
        tempo_atual += duracao
    return esperas

alunos_na_fila = [("Ana", 15), ("Beto", 20), ("Carla", 10), ("Diego", 25)]
resultados = simular_fila(alunos_na_fila)

for nome, espera in resultados:
    print(f"{nome}: {espera} min")

maior_espera = max(resultados, key=lambda x: x[1])
print(f"Maior espera: {maior_espera[0]} ({maior_espera[1]} min)")