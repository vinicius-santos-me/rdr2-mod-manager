# Como Criar Releases no GitHub

Este guia explica como gerar o `.exe` com ícone e publicar como uma release no seu repositório GitHub.

---

## Pré-requisitos

Ter o repositório clonado e o ambiente configurado:

```bash
git clone https://github.com/seu-usuario/rdr2-mod-manager.git
cd rdr2-mod-manager
pip install pyinstaller
```

---

## 1. Estrutura esperada antes de dar build

Garanta que esses arquivos estão na raiz do projeto:

```
rdr2-mod-manager/
├── rdr2_mod_managertk.py        ← código fonte
├── rdr2_mod_manager.spec        ← configuração do PyInstaller (já inclui o ícone)
├── icon.ico                     ← ícone do exe (deve estar com esse nome exato)
├── build.py                     ← script de build
└── ...
```

> **Importante:** o `.spec` espera o ícone com o nome `icon.ico` na mesma pasta. Não mude esse nome.

---

## 2. Gerar o `.exe`

```bash
python build.py
```

Após a build, o executável aparece em:

```
dist/rdr2_mod_manager.exe
```

Ele já vai estar com o ícone do RDR2.

---

## 3. Criar uma Release no GitHub

### Pela interface do GitHub (recomendado)

1. Acesse o seu repositório no GitHub.
2. Clique em **Releases** (na direita da página, abaixo de *Code*).
3. Clique em **New Release**.
4. Preenche os campos:
   - **Tag version:** use o formato `v1.0.0` (ex: `v1.1.0`, `v1.2.0`).
   - **Release title:** mesmo da tag, ex: `v1.1.0`.
   - **Description:** descreva o que mudou nessa versão (changelog).
5. Clique em **Attach binaries by dragging them here** e arraste o arquivo `dist/rdr2_mod_manager.exe`.
6. Clique **Publish release**.

### Pela linha de comando (usando GitHub CLI)

Se você tiver o [GitHub CLI](https://cli.github.com/) instalado:

```bash
# Cria a tag e a release, e anexa o .exe
gh release create v1.0.0 dist/rdr2_mod_manager.exe \
  --title "v1.0.0" \
  --notes "Primeira release do RDR2 Mod Manager."
```

Para versões seguintes, só muda a tag e o texto:

```bash
gh release create v1.1.0 dist/rdr2_mod_manager.exe \
  --title "v1.1.0" \
  --notes "- Correção de bug X\n- Melhoria Y"
```

---

## 4. Como os usuários baixam

Qualquer pessoa acessa **Releases** no repositório e baixa o `.exe` diretamente — sem precisar instalar Python ou fazer build.

---

## Resumo do fluxo completo

```
Edita o código → python build.py → dist/rdr2_mod_manager.exe
                                          ↓
                              gh release create v1.x.0 dist/rdr2_mod_manager.exe
                                          ↓
                              Usuários baixam pela página de Releases
```
