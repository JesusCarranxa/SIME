#!/usr/bin/env python3
# Verifica estructura, permisos i importacions bàsiques del projecte.
import os, sys, stat

ROOT = os.getenv("GITHUB_WORKSPACE", ".")
fail = False

def check_exists(path, desc, executable=False):
    global fail
    p = os.path.join(ROOT, path)
    if not os.path.exists(p):
        print(f"❌ Falta {desc}: {path}")
        fail = True
        return
    if executable:
        if not (os.stat(p).st_mode & stat.S_IXUSR):
            print(f"⚠️ {desc} no és executable: {path}")
        else:
            print(f"✅ {desc} executable: {path}")
    print(f"✅ OK: {desc}: {path}")

check_exists("main.py", "llançador principal")
check_exists("run.sh", "script d’execució", executable=True)
check_exists("requirements.txt", "requirements")
check_exists("d4_core", "carpeta d4_core")
check_exists("d4_core/core_d4.py", "mòdul core_d4.py")

sys.path.append(os.path.join(ROOT, "d4_core"))
try:
    import core_d4  # noqa: F401
    print("✅ Importació de core_d4 correcta")
except Exception as e:
    print(f"❌ Error important en importar core_d4: {e}")
    fail = True

for key in ("SMTP_USERNAME", "SMTP_PASSWORD", "ALERT_EMAIL"):
    print(f"{'✅' if os.getenv(key) else '⚠️'} Secret present: {key}" if os.getenv(key) else f"⚠️ Secret absent o buit: {key}")

sys.exit(1 if fail else 0)