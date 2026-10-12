import os
import sys
import time
import shutil
import tempfile
import platform
import subprocess
import tkinter as tk
from tkinter import messagebox

BG = "#101014"
PANEL = "#1b1b22"
RED = "#f02d3a"
RED_DARK = "#a81724"
WHITE = "#f4f4f6"
MUTED = "#a5a5b2"
GREEN = "#55d98b"

class OptimizerApp:
    def __init__(self, root):
        self.root = root
        root.title("EL FLACO TJS OPTIMIZED")
        root.geometry("980x680")
        root.minsize(820, 600)
        root.configure(bg=BG)

        header = tk.Frame(root, bg=BG)
        header.pack(fill="x", padx=28, pady=(24, 14))
        tk.Label(header, text="EL FLACO", bg=BG, fg=WHITE,
                 font=("Segoe UI", 25, "bold")).pack(anchor="w")
        tk.Label(header, text="TJS OPTIMIZED  //  WINDOWS GAMING TOOLKIT",
                 bg=BG, fg=RED, font=("Segoe UI", 11, "bold")).pack(anchor="w", pady=(1, 0))
        tk.Label(header, text="Ferramentas seguras para preparar seu PC antes de jogar.",
                 bg=BG, fg=MUTED, font=("Segoe UI", 10)).pack(anchor="w", pady=(8, 0))

        status = tk.Frame(root, bg=PANEL, highlightbackground="#30303a", highlightthickness=1)
        status.pack(fill="x", padx=28, pady=(0, 16))
        self.status_label = tk.Label(status, text="●  SISTEMA PRONTO",
                                     bg=PANEL, fg=GREEN, font=("Segoe UI", 10, "bold"))
        self.status_label.pack(side="left", padx=16, pady=13)
        self.os_label = tk.Label(status, text=f"{platform.system()} {platform.release()}",
                                 bg=PANEL, fg=MUTED, font=("Segoe UI", 10))
        self.os_label.pack(side="right", padx=16)

        body = tk.Frame(root, bg=BG)
        body.pack(fill="both", expand=True, padx=28, pady=(0, 18))
        left = tk.Frame(body, bg=BG)
        left.pack(side="left", fill="both", expand=True, padx=(0, 10))
        right = tk.Frame(body, bg=BG)
        right.pack(side="left", fill="both", expand=True, padx=(10, 0))

        self.card(left, "01  /  DIAGNÓSTICO", "Veja informações básicas do sistema.",
                  "VER MEU PC", self.system_info)
        self.card(left, "02  /  LIMPEZA TEMPORÁRIA", "Remove arquivos temporários do seu usuário.\nArquivos em uso serão ignorados.",
                  "LIMPAR TEMPORÁRIOS", self.clean_temp)
        self.card(right, "03  /  MODO JOGO", "Abra as configurações de jogos do Windows para revisar o Modo de Jogo.",
                  "ABRIR CONFIGURAÇÕES", self.open_game_settings)
        self.card(right, "04  /  CHECKLIST FORTNITE", "Dicas rápidas antes de entrar no jogo.",
                  "VER CHECKLIST", self.checklist)

        footer = tk.Frame(root, bg=BG)
        footer.pack(fill="x", padx=28, pady=(0, 18))
        tk.Label(footer, text="VERSÃO 0.1  •  SEM PROMESSAS FALSAS DE FPS  •  ALTERAÇÕES REVERSÍVEIS",
                 bg=BG, fg="#777783", font=("Segoe UI", 8)).pack(anchor="w")

    def card(self, parent, title, desc, button_text, command):
        frame = tk.Frame(parent, bg=PANEL, highlightbackground="#30303a", highlightthickness=1)
        frame.pack(fill="both", expand=True, pady=8)
        tk.Label(frame, text=title, bg=PANEL, fg=RED, font=("Segoe UI", 11, "bold")).pack(anchor="w", padx=18, pady=(17, 8))
        tk.Label(frame, text=desc, bg=PANEL, fg=MUTED, justify="left",
                 font=("Segoe UI", 10), wraplength=350).pack(anchor="w", padx=18, pady=(0, 16))
        btn = tk.Button(frame, text=button_text, command=command, bg=RED_DARK, fg=WHITE,
                        activebackground=RED, activeforeground=WHITE, relief="flat",
                        font=("Segoe UI", 10, "bold"), cursor="hand2", padx=14, pady=10)
        btn.pack(anchor="w", padx=18, pady=(0, 18))

    def set_status(self, text, color=GREEN):
        self.status_label.config(text="●  " + text, fg=color)

    def system_info(self):
        try:
            import ctypes
            class MEMORYSTATUSEX(ctypes.Structure):
                _fields_ = [
                    ("dwLength", ctypes.c_ulong), ("dwMemoryLoad", ctypes.c_ulong),
                    ("ullTotalPhys", ctypes.c_ulonglong), ("ullAvailPhys", ctypes.c_ulonglong),
                    ("ullTotalPageFile", ctypes.c_ulonglong), ("ullAvailPageFile", ctypes.c_ulonglong),
                    ("ullTotalVirtual", ctypes.c_ulonglong), ("ullAvailVirtual", ctypes.c_ulonglong),
                    ("ullAvailExtendedVirtual", ctypes.c_ulonglong)
                ]
            mem = MEMORYSTATUSEX()
            mem.dwLength = ctypes.sizeof(mem)
            ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(mem))
            total = mem.ullTotalPhys / (1024**3)
            free = mem.ullAvailPhys / (1024**3)
            msg = (f"Sistema: {platform.system()} {platform.release()}\n"
                   f"Processador: {platform.processor() or 'Não identificado'}\n"
                   f"RAM total: {total:.1f} GB\nRAM disponível: {free:.1f} GB\n\n"
                   "Este diagnóstico é informativo; não mede FPS nem temperatura.")
        except Exception:
            msg = (f"Sistema: {platform.system()} {platform.release()}\n"
                   f"Processador: {platform.processor() or 'Não identificado'}\n"
                   "Não foi possível ler todos os detalhes de memória.")
        self.set_status("DIAGNÓSTICO CONCLUÍDO")
        messagebox.showinfo("EL FLACO TJS — Diagnóstico", msg)

    def clean_temp(self):
        temp_dir = tempfile.gettempdir()
        if not messagebox.askyesno(
            "Confirmar limpeza",
            "O app tentará remover arquivos da pasta temporária do seu usuário:\n\n"
            f"{temp_dir}\n\n"
            "Arquivos em uso ou sem permissão serão ignorados. Continuar?"
        ):
            return
        removed_files = 0
        removed_dirs = 0
        errors = 0
        cutoff = time.time()
        try:
            for name in os.listdir(temp_dir):
                path = os.path.join(temp_dir, name)
                try:
                    if os.path.isfile(path) or os.path.islink(path):
                        os.remove(path)
                        removed_files += 1
                    elif os.path.isdir(path):
                        shutil.rmtree(path)
                        removed_dirs += 1
                except (PermissionError, OSError):
                    errors += 1
        except OSError as exc:
            messagebox.showerror("Limpeza", f"Não foi possível acessar a pasta temporária:\n{exc}")
            return
        self.set_status("LIMPEZA FINALIZADA")
        messagebox.showinfo(
            "Limpeza concluída",
            f"Arquivos removidos: {removed_files}\nPastas removidas: {removed_dirs}\n"
            f"Itens ignorados (em uso/sem permissão): {errors}\n\n"
            "A limpeza não garante aumento de FPS."
        )

    def open_game_settings(self):
        if sys.platform != "win32":
            messagebox.showwarning("Windows", "Esta função foi feita para Windows.")
            return
        try:
            os.startfile("ms-settings:gaming-gamemode")
            self.set_status("CONFIGURAÇÕES ABERTAS")
        except Exception:
            try:
                subprocess.Popen(["cmd", "/c", "start", "", "ms-settings:gaming-gamemode"], shell=False)
            except Exception as exc:
                messagebox.showerror("Erro", f"Não foi possível abrir as configurações:\n{exc}")

    def checklist(self):
        msg = (
            "CHECKLIST ANTES DO FORTNITE\n\n"
            "1. Feche programas que você não está usando.\n"
            "2. Confira se o Windows e o driver da GPU estão atualizados.\n"
            "3. No Fortnite, teste o modo de renderização adequado ao seu PC.\n"
            "4. Use resolução e qualidade gráfica compatíveis com seu hardware.\n"
            "5. Evite ferramentas que prometem FPS milagroso ou desativam proteções.\n\n"
            "O resultado varia conforme CPU, GPU, RAM, temperatura e configurações."
        )
        messagebox.showinfo("EL FLACO TJS — Checklist", msg)

if __name__ == "__main__":
    root = tk.Tk()
    app = OptimizerApp(root)
    root.mainloop()
