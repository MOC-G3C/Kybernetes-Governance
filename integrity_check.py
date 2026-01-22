import random

def run_zoo_simulation(iterations=10000):
    print("--- L'AXE HYBRIDE : INITIALISATION DU ZOO ENTROPIC ---")
    
    success = 0
    errors = {"Thermique": 0, "Éthique": 0, "Signal": 0, "Biologique": 0}

    for _ in range(iterations):
        if random.random() < 0.05: # 5% de surchauffe
            errors["Thermique"] += 1
        elif random.random() < 0.10: # 10% d'interférence
            errors["Signal"] += 1
        elif random.random() < 0.02: # 2% de dérive éthique
            errors["Éthique"] += 1
        elif random.random() < 0.01: # 1% de rejet physique
            errors["Biologique"] += 1
        else:
            success += 1

    rate = (success / iterations) * 100
    print(f"Stabilité : {rate:.2f}%")
    
    if rate >= 95:
        print("VERDICT : VALIDÉ PAR L'AXE.")
    else:
        print("VERDICT : ÉCHEC. RÉÉCRITURE REQUISE.")

run_zoo_simulation()
