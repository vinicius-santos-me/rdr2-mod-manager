# RDR2 Mod Manager

Gerenciador de mods para **Red Dead Redemption 2** (PC). Permite ativar e desativar mods rapidamente sem apagar nada — apenas renomeando as pastas/arquivos que não são originais do jogo.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows-lightblue)

---

## Como funciona

O programa escaneia a pasta do RDR2 e classifica tudo em três categorias:

- **Originais** — arquivos e pastas que pertencem ao jogo (nunca são alterados).
- **Mods Ativos** — qualquer coisa que não seja original e não esteja desativada.
- **Mods Desativados** — arquivos/pastas que tiveram o sufixo `(disable)` adicionado ao nome.

Para **desativar** um mod, o programa simplesmente adiciona `(disable)` ao final do nome. Para **ativar**, remove esse sufixo. Nada é apagado.

---

## Requisitos

- **Windows 10 ou 11**
- **Python 3.10+** (para rodar pelo código fonte)
- Nenhuma dependência externa além das bibliotecas padrão do Python (`tkinter`, `os`, `logging`)

---

## Como usar

### Opção 1 — Executável pré-compilado

Baixe o `.exe` gerado pela build e execute diretamente. Sem necessidade de instalar o Python.

### Opção 2 — Pelo código fonte

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/rdr2-mod-manager.git
cd rdr2-mod-manager

# Rode diretamente
python rdr2_mod_managertk.py
```

### Opção 3 — Fazer sua própria build

```bash
# Instale o PyInstaller
pip install pyinstaller

# Execute o script de build
python build.py
```

O executável será gerado na pasta `dist/`.

---

## Como usar o programa

1. Abra o programa.
2. Clique em **Procurar...** e selecione a pasta de instalação do RDR2.
3. O scan é feito automaticamente — você verá todos os mods ativos e desativados.
4. Use os botões:
   - **Desativar Mods** — adiciona `(disable)` a todos os mods ativos.
   - **Ativar Mods** — remove `(disable)` de todos os mods desativados.

---

## Estrutura do Repositório

```
rdr2-mod-manager/
├── rdr2_mod_managertk.py   # Código fonte principal
├── build.py                # Script para gerar o .exe com PyInstaller
├── requirements.txt        # Dependências (apenas PyInstaller para build)
├── .gitignore              # Arquivos ignorados pelo Git
└── README.md               # Este arquivo
```

---

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).
