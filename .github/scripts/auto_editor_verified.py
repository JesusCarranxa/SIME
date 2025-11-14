#!/usr/bin/env python3
# ==========================================================
# META-F⁴ / D₄ — Auto Editor Verified Script
# Validació simbòlica i registre d’estat del cicle autònom
# ==========================================================

import os
import json
import datetime
import hashlib
import sys

LOG_PATH = "cycle_log.txt"
SUMMARY_PATH = "summary.json"


def hash_file(path):
    """Calcula hash SHA256 d'un fitxer per verificar integritat."""
    if not os.path.exists(path):
        return None
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(4096), b""):
            h.update(block)
    return h.hexdigest()


def read_last_lines(path, n=20):
    """Llegeix les últimes n línies d’un fitxer de registre."""
    if not os.path.exists(path):
        return ["[Sense registre disponible]"]
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
    return lines[-n:]


def validate_cycle():
    """Valida si el cicle s’ha executat amb èxit."""
    if not os.path.exists(LOG_PATH):
        return {"status": "missing_log", "message": "No s’ha trobat el registre del cicle."}

    last_lines = read_last_lines(LOG_PATH)
    text = "".join(last_lines).lower()

    if "error" in text or "failed" in text or "exception" in text:
        status = "failed"
    else:
        status = "success"

    return {
        "status": status,
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "hash": hash_file(LOG_PATH),
        "summary": last_lines
    }


def save_summary(data):
    """Desa un resum JSON per ús del workflow i auditories."""
    with open(SUMMARY_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"[OK] Resum desat a {SUMMARY_PATH}")


def main():
    print("🧠 Executant validació automàtica del cicle META-F⁴_D₄...")
    result = validate_cycle()
    save_summary(result)
    print(f"Estat final: {result['status']}")
    if result["status"] != "success":
        sys.exit(1)  # Permet al workflow detectar error i activar autorecuperació


if __name__ == "__main__":
    main()
