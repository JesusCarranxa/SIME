#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
META-F⁴_D₄ — Autonomous Cycle Launcher
Autor: J. P. Carranza Font
Descripció: Inicialitza i executa el nucli D₄ amb configuració dinàmica.
"""

import os
import sys
import traceback

# --- Afegim el path de d4_core per assegurar la importació ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CORE_PATH = os.path.join(BASE_DIR, "d4_core")
if CORE_PATH not in sys.path:
    sys.path.append(CORE_PATH)

try:
    from core_d4 import D4Core
except ModuleNotFoundError as e:
    print("⚠️ Error: No s'ha pogut importar el mòdul D4Core.")
    print("Verifica que el fitxer 'core_d4.py' existeix dins la carpeta 'd4_core'.")
    print("Detall tècnic:", e)
    sys.exit(1)

# --- Execució principal ---
if __name__ == "__main__":
    print("Inicialitzant sistema META-F⁴ / D₄...")
    try:
        core = D4Core()
        core.run_cycle()
        print("✅ Cicle D₄ completat correctament.")
    except Exception as err:
        print("❌ Error durant l'execució del cicle D₄:")
        traceback.print_exc()
        sys.exit(1)