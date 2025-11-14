#!/usr/bin/env python3
import os, re, json, subprocess
from datetime import datetime

def log(msg):
    print(f"[AUTO_EDITOR] {datetime.utcnow().isoformat()} :: {msg}")

def verify_security(code):
    """Filtra ordres perilloses i evita execució arbitrària."""
    banned = ["os.system", "subprocess.Popen", "eval(", "exec(", "open('/etc"]
    for b in banned:
        if b in code:
            log(f"⚠️ Codi rebutjat per ús de '{b}'")
            return False
    return True

def run_safe_command(command):
    """Executa una ordre segura i captura sortida."""
    try:
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, timeout=30
        )
        return result.stdout.strip()
    except Exception as e:
        log(f"Error executant: {e}")
        return None

def main():
    log("Validant cicle autònom META-F⁴/D₄...")
    files = run_safe_command("git diff --name-only HEAD~1 HEAD")
    if not files:
        log("No hi ha canvis nous.")
        return

    modified_files = files.split("\n")
    log(f"Fitxers modificats: {modified_files}")

    for f in modified_files:
        if not f.endswith(".py"):
            continue

        with open(f, "r", encoding="utf-8") as file:
            code = file.read()
            if not verify_security(code):
                log(f"Fitxer rebutjat per seguretat: {f}")
                continue

            log(f"Fitxer verificat correctament: {f}")

    log("Validació completada sense incidents ✅")

if __name__ == "__main__":
    main()