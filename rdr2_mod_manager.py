# -*- coding: utf-8 -*-

# Versão com Interface Gráfica Melhorada (ttk, Tema Escuro)

import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext

# --- LISTA DE ARQUIVOS E LÓGICA DO PROGRAMA (NÃO MUDA) ---
ORIGINAL_FILES = {
    "12on7", "Redistributables", "x64", "amd_ags_x64.dll", "anirm_0.rpf", "appdata0_update.rpf",
    "bink2w64.dll", "common_0.rpf", "data_0.rpf", "dxilconv7.dll", "ffx_fsr2_api_dx12_x64.dll",
    "ffx_fsr2_api_vk_x64.dll", "ffx_fsr2_api_x64.dll", "hd_0.rpf", "index.bin", "levels_0.rpf",
    "levels_1.rpf", "levels_2.rpf", "levels_3.rpf", "levels_4.rpf", "levels_5.rpf", "levels_6.rpf",
    "levels_7.rpf", "movies_0.rpf", "NvLowLatencyVk.dll", "nvngx_dlss.dll", "oo2core_5_win64.dll",
    "packs_0.rpf", "packs_1.rpf", "RDR2.exe", "rowpack_0.rpf", "shaders_x64.rpf", "textures_0.rpf",
    "textures_1.rpf", "uninstall.exe", "update_1.rpf", "update_2.rpf", "update_3.rpf", "update_4.rpf",
}
DISABLE_SUFFIX = "(disable)"


def scan_game_folder(folder_path: str):
    # (Esta função permanece inalterada)
    if not folder_path or not os.path.isdir(folder_path): return None, None, None
    originals, active_mods, disabled_mods = [], [], []
    try:
        for item_name in os.listdir(folder_path):
            if item_name in ORIGINAL_FILES:
                originals.append(item_name)
            elif item_name.endswith(DISABLE_SUFFIX):
                disabled_mods.append(item_name)
            else:
                active_mods.append(item_name)
    except Exception as e:
        messagebox.showerror("Erro de Leitura", f"Erro ao ler a pasta do jogo: {e}")
        return None, None, None
    return originals, active_mods, disabled_mods


def format_scan_results(originals: list, active_mods: list, disabled_mods: list) -> str:
    # (Esta função permanece inalterada)
    if originals is None: return "Selecione uma pasta válida e clique em 'Scan'."
    total_originais, total_ativos, total_desativados = len(originals), len(active_mods), len(disabled_mods)
    active_mods.sort()
    disabled_mods.sort()
    result_text = (
        f"--- RESULTADO DO SCAN ---\n"
        f"Arquivos Originais Encontrados: {total_originais}\n\n"
        f"--- MODS ATIVOS ({total_ativos}) ---\n"
    )
    result_text += "\n".join(active_mods) + "\n" if active_mods else "Nenhum mod ativo encontrado.\n"
    result_text += f"\n--- MODS DESATIVADOS ({total_desativados}) ---\n"
    result_text += "\n".join(disabled_mods) + "\n" if disabled_mods else "Nenhum mod desativado encontrado.\n"
    return result_text


def manage_mods(folder_path: str, mods_list: list, action: str):
    # (Esta função permanece inalterada)
    if not mods_list:
        messagebox.showinfo("Aviso", "Nenhum mod para processar.")
        return 0
    count = 0
    for mod_name in mods_list:
        try:
            if action == 'disable' and not mod_name.endswith(DISABLE_SUFFIX):
                old_path, new_path = os.path.join(folder_path, mod_name), os.path.join(folder_path,
                                                                                       f"{mod_name}{DISABLE_SUFFIX}")
                os.rename(old_path, new_path)
                count += 1
            elif action == 'enable' and mod_name.endswith(DISABLE_SUFFIX):
                old_path, new_path = os.path.join(folder_path, mod_name), os.path.join(folder_path,
                                                                                       mod_name.replace(DISABLE_SUFFIX,
                                                                                                        ''))
                os.rename(old_path, new_path)
                count += 1
        except Exception as e:
            messagebox.showerror("Erro de Renomeação", f"Falha ao renomear '{mod_name}':\n{e}")
    action_text = "ativados" if action == 'enable' else 'desativados'
    messagebox.showinfo("Operação Concluída", f"{count} mod(s) foram {action_text} com sucesso!")
    return count


# --- Classe da Aplicação com a NOVA Interface ---
class ModManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RDR2 Mod Manager v1.1")
        self.root.geometry("650x550")
        self.root.minsize(550, 450)  # Tamanho mínimo da janela

        # --- Configuração do Estilo e Tema Escuro ---
        self.style = ttk.Style(root)
        self.root.configure(bg="#2E2E2E")  # Cor de fundo da janela

        # Define um tema base
        self.style.theme_use("clam")

        # Configurações do tema escuro para os widgets
        self.style.configure("TFrame", background="#2E2E2E")
        self.style.configure("TLabel", background="#2E2E2E", foreground="#FFFFFF", font=("Segoe UI", 10))
        self.style.configure("TEntry", fieldbackground="#4A4A4A", foreground="#FFFFFF", insertcolor="#FFFFFF",
                             borderwidth=0)
        self.style.configure("TButton", background="#4A4A4A", foreground="#FFFFFF", font=("Segoe UI", 10, "bold"),
                             borderwidth=1, focusthickness=3, focuscolor='none')
        self.style.map("TButton", background=[("active", "#6A6A6A")])  # Cor ao passar o mouse

        # Estilo customizado para botões de ação
        self.style.configure("Accent.TButton", background="#0078D7", foreground="#FFFFFF")
        self.style.map("Accent.TButton", background=[("active", "#005A9E")])
        self.style.configure("Disable.TButton", background="#C42B1C", foreground="#FFFFFF")
        self.style.map("Disable.TButton", background=[("active", "#A32418")])
        self.style.configure("Enable.TButton", background="#188344", foreground="#FFFFFF")
        self.style.map("Enable.TButton", background=[("active", "#126333")])

        # --- Variáveis ---
        self.folder_path = tk.StringVar()
        self.last_active_mods = []
        self.last_disabled_mods = []

        # --- Layout com Grid ---
        main_frame = ttk.Frame(root, padding="10 10 10 10")
        main_frame.pack(expand=True, fill=tk.BOTH)

        # Configura o redimensionamento das linhas e colunas
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)

        # Seletor de pasta (Linha 0)
        ttk.Label(main_frame, text="Pasta do RDR2:").grid(row=0, column=0, sticky="w", pady=(0, 5))
        entry = ttk.Entry(main_frame, textvariable=self.folder_path, state='readonly', width=60)
        entry.grid(row=0, column=1, sticky="ew", padx=(5, 5), pady=(0, 5))
        browse_button = ttk.Button(main_frame, text="Procurar...", command=self.browse_folder, style="Accent.TButton",
                                   cursor="hand2")
        browse_button.grid(row=0, column=2, sticky="e", pady=(0, 5))

        # Botões de ação (Linha 1)
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=1, column=0, columnspan=3, sticky="ew", pady=5)
        button_frame.columnconfigure((0, 1, 2), weight=1)  # Faz os 3 botões ocuparem espaço igual

        scan_button = ttk.Button(button_frame, text="Scan", command=self.perform_scan, cursor="hand2")
        scan_button.grid(row=0, column=0, sticky="ew", padx=(0, 3))
        disable_button = ttk.Button(button_frame, text="Desativar Mods", command=self.disable_mods_action,
                                    style="Disable.TButton", cursor="hand2")
        disable_button.grid(row=0, column=1, sticky="ew", padx=3)
        enable_button = ttk.Button(button_frame, text="Ativar Mods", command=self.enable_mods_action,
                                   style="Enable.TButton", cursor="hand2")
        enable_button.grid(row=0, column=2, sticky="ew", padx=(3, 0))

        # Área de texto (Linha 2)
        self.output_text = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, state='disabled', height=15,
                                                     bg="#1E1E1E", fg="#D4D4D4", font=("Consolas", 10),
                                                     relief="solid", borderwidth=1, insertbackground="#FFFFFF")
        self.output_text.grid(row=2, column=0, columnspan=3, sticky="nsew", pady=(5, 0))
        self.update_output(
            "Bem-vindo ao RDR2 Mod Manager!\n\n1. Clique em 'Procurar...' para selecionar a pasta do seu jogo.\n2. O scan será feito automaticamente.")

    # --- Funções de Callback (a lógica dentro delas não muda) ---
    def update_output(self, text):
        self.output_text.config(state='normal')
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, text)
        self.output_text.config(state='disabled')

    def browse_folder(self):
        path = filedialog.askdirectory(title="Selecione a pasta do Red Dead Redemption 2")
        if path:
            self.folder_path.set(path)
            self.perform_scan()

    def perform_scan(self):
        path = self.folder_path.get()
        if not path:
            messagebox.showerror("Erro", "Por favor, selecione uma pasta válida do RDR2.")
            return
        originals, active, disabled = scan_game_folder(path)
        self.last_active_mods, self.last_disabled_mods = active, disabled
        results_text = format_scan_results(originals, active, disabled)
        self.update_output(results_text)

    def disable_mods_action(self):
        path = self.folder_path.get()
        if not path or not self.last_active_mods:
            messagebox.showwarning("Aviso", "Nenhum mod ativo para desativar (baseado no último scan).")
            return
        manage_mods(path, self.last_active_mods, 'disable')
        self.perform_scan()

    def enable_mods_action(self):
        path = self.folder_path.get()
        if not path or not self.last_disabled_mods:
            messagebox.showwarning("Aviso", "Nenhum mod desativado para ativar (baseado no último scan).")
            return
        manage_mods(path, self.last_disabled_mods, 'enable')
        self.perform_scan()


if __name__ == "__main__":
    root = tk.Tk()
    app = ModManagerApp(root)
    root.mainloop()