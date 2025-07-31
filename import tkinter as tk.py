import tkinter as tk
import hashlib


def gerar_hash(mensagem):
    mensagem_bytes = mensagem.encode()
    hash_obj = hashlib.sha256(mensagem_bytes)
    hash_hex = hash_obj.hexdigest()
    return hash_hex


def enviar_mensagem():
    nome = entrada_nome.get()
    mensagem = entrada_msg.get()
    if nome and mensagem:
        hash_msg = gerar_hash(mensagem)
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, f"{nome}: {mensagem}\nHash: {hash_msg}\n\n")
        # Resposta automática do "bot"
        resposta_bot = f"Bot: Recebi sua mensagem, {nome}! O hash dela é:\n{hash_msg}\n\n"
        chat_box.insert(tk.END, resposta_bot)
        chat_box.config(state=tk.DISABLED)
        entrada_msg.delete(0, tk.END)


# Janela principal
root = tk.Tk()
root.title("Mini Chat")
root.geometry("450x350")
root.configure(bg="#222831")

# Frame principal
frame = tk.Frame(root, bg="#393e46", padx=10, pady=10)
frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Campo de nome
tk.Label(frame, text="Nome:", bg="#393e46", fg="#eeeeee", font=(
    "Arial", 10, "bold")).grid(row=0, column=0, sticky="w")
entrada_nome = tk.Entry(frame, font=("Arial", 10))
entrada_nome.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

# Campo de mensagem
tk.Label(frame, text="Mensagem:", bg="#393e46", fg="#eeeeee",
         font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w")
entrada_msg = tk.Entry(frame, font=("Arial", 10))
entrada_msg.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

# Botão de enviar
tk.Button(frame, text="Enviar", command=enviar_mensagem, bg="#00adb5",
          fg="#eeeeee", font=("Arial", 10, "bold")).grid(row=1, column=2, padx=5, pady=5)

# Caixa de exibição
chat_box = tk.Text(frame, height=12, width=50, bg="#222831",
                   fg="#eeeeee", font=("Consolas", 10))
chat_box.grid(row=2, column=0, columnspan=3, pady=10)
chat_box.config(state=tk.DISABLED)

# Ajustar colunas
frame.columnconfigure(1, weight=1)

root.mainloop()
