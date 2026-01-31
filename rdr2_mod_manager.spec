# -*- mode: python ; coding: utf-8 -*-
#
# Spec do PyInstaller para o RDR2 Mod Manager
# Uso: pyinstaller rdr2_mod_manager.spec
#

import os

# Caminho base do projeto (onde esse .spec está)
BASE_DIR = os.path.abspath(os.getcwd())

a = Analysis(
    ['rdr2_mod_manager.py'],
    pathex=[BASE_DIR],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    excludes=[],
)

pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    a.zipfiles,
    a.datas,
    name='RDR2_Mod_Manager',                          # Nome do .exe final
    debug=False,
    bootloader_argv=[],
    strip=False,
    upx=True,                                         # Comprime o exe (menor tamanho)
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,                                    # GUI — sem janela de console
    disable_windowed_traceback=True,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=os.path.join(BASE_DIR, 'icon.ico'),          # Ícone do exe
    version=None,
)
