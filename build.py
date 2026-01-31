"""
Script para gerar o executável do RDR2 Mod Manager.

Uso:
    python build.py

Gera o .exe com ícone na pasta dist/
"""

import PyInstaller.__main__ as pyinstaller

pyinstaller.run([
    "rdr2_mod_manager.spec",   # Usa o .spec que já tem ícone e configurações
    "--clean",                  # Limpa cache anterior antes de compilar
])
