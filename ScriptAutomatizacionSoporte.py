# parse_logs.py
import os
import re
import csv
from collections import Counter

LOG_DIR = "logs"
OUTPUT = "reportes/errores_resumen.csv"
os.makedirs("reportes", exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

PATTERN = re.compile(r"(ERROR|WARN|INFO)")

def procesar_logs():
    counter = Counter()
    for fname in os.listdir(LOG_DIR):
        if not fname.endswith(".log"):
            continue
        with open(os.path.join(LOG_DIR, fname), encoding="utf-8", errors="ignore") as f:
            for line in f:
                m = PATTERN.search(line)
                if m:
                    counter[m.group(1)] += 1
    return counter

def escribir_csv(counter):
    with open(OUTPUT, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["nivel", "cantidad"])
        for nivel, cant in counter.items():
            w.writerow([nivel, cant])
    print(f"Reporte generado: {OUTPUT}")

if __name__ == "__main__":
    c = procesar_logs()
    if not c:
        print("No se encontraron logs (.log) en la carpeta 'logs'.")
    else:
        escribir_csv(c)
