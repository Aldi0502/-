import random

def measure_quantum_pair():
    # Твой идеальный квантовый генератор!
    particle_1 = random.choice(["ВВЕРХ", "ВНИЗ"])
    particle_2 = "ВНИЗ" if particle_1 == "ВВЕРХ" else "ВВЕРХ"
    return particle_1, particle_2

print("Запуск квантового измерения...\n")

for i in range(1, 6):
    # Распаковываем наши запутанные частицы (та самая магия с запятой!)
    p1, p2 = measure_quantum_pair()
    print(f"Измерение #{i}: Частица 1 в Алматы = {p1} | Частица 2 в космосе = {p2}")

print("\n[УСПЕХ] Эксперимент завершен! Скорость передачи состояния: МГНОВЕННО!")
