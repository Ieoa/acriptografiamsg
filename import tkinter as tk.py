import tkinter as tk
import hashlib


def gerar_hash(mensagem):  # Corrigido o nome do parâmetro
    mensagem_bytes = mensagem.encode()
    hash_obj = hashlib.sha256(mensagem_bytes)
    hash_hex = hash_obj.hexdigest()  # Corrigido o método
    return hash_hex


def enviar_mensagem():
    nome = entrada_nome.get()
    mensagem = entrada_msg.get()
    if nome and mensagem:
        hash_msg = gerar_hash(mensagem)
        chat_box.insert(tk.END, f"{nome}: {mensagem}\nHash: {hash_msg}\n\n")
        entrada_msg.delete(0, tk.END)


# Janela principal
root = tk.Tk()
root.title("Mini Chat")
root.geometry("400x300")

# Campo de nome
tk.Label(root, text="Nome:").pack()
entrada_nome = tk.Entry(root)
entrada_nome.pack()

# Campo de mensagem
tk.Label(root, text="Mensagem:").pack()
entrada_msg = tk.Entry(root)
entrada_msg.pack()

# Botão de enviar
tk.Button(root, text="Enviar", command=enviar_mensagem).pack(pady=5)

# Caixa de exibição
chat_box = tk.Text(root, height=10, width=50)
chat_box.pack()

# Loop principal
root.mainloop()
