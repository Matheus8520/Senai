import sqlite3
from tkinter import *

# Conectar ao banco de dados
conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

# Criar tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT NOT NULL,
        endereco TEXT NOT NULL
    )
''')

# Funções CRUD

def criar_cliente(nome, email, telefone, endereco):
    cursor.execute('INSERT INTO clientes (nome, email, telefone, endereco) VALUES (?, ?, ?, ?)', (nome, email, telefone, endereco))
    conn.commit()

def ler_clientes():
    cursor.execute('SELECT * FROM clientes')
    return cursor.fetchall()

def atualizar_cliente(id, nome, email, telefone, endereco):
    cursor.execute('UPDATE clientes SET nome = ?, email = ?, telefone = ?, endereco = ? WHERE id = ?', (nome, email, telefone, endereco, id))
    conn.commit()

def deletar_cliente(id):
    cursor.execute('DELETE FROM clientes WHERE id = ?', (id,))
    conn.commit()

# Interface gráfica
root = Tk()
root.title("Cadastro de Clientes")

# Funções da interface gráfica
def criar_cliente_gui():
    nome = nome_entry.get()
    email = email_entry.get()
    telefone = telefone_entry.get()
    endereco = endereco_entry.get()
    criar_cliente(nome, email, telefone, endereco)
    nome_entry.delete(0, END)
    email_entry.delete(0, END)
    telefone_entry.delete(0, END)
    endereco_entry.delete(0, END)

def ler_clientes_gui():
    clientes = ler_clientes()
    clientes_text.delete(1.0, END)
    for cliente in clientes:
        clientes_text.insert(END, str(cliente) + "\n")

def atualizar_cliente_gui():
    id = int(id_entry.get())
    nome = nome_entry.get()
    email = email_entry.get()
    telefone = telefone_entry.get()
    endereco = endereco_entry.get()
    atualizar_cliente(id, nome, email, telefone, endereco)
    nome_entry.delete(0, END)
    email_entry.delete(0, END)
    telefone_entry.delete(0, END)
    endereco_entry.delete(0, END)
    id_entry.delete(0, END)

def deletar_cliente_gui():
    id = int(id_entry.get())
    deletar_cliente(id)
    id_entry.delete(0, END)

# Componentes da interface gráfica
nome_label = Label(root, text="Nome:")
nome_label.grid(row=0, column=0)
nome_entry = Entry(root)
nome_entry.grid(row=0, column=1)

email_label = Label(root, text="E-mail:")
email_label.grid(row=1, column=0)
email_entry = Entry(root)
email_entry.grid(row=1, column=1)

telefone_label = Label(root, text="Telefone:")
telefone_label.grid(row=2, column=0)
telefone_entry = Entry(root)
telefone_entry.grid(row=2, column=1)

endereco_label = Label(root, text="Endereço:")
endereco_label.grid(row=3, column=0)
endereco_entry = Entry(root)
endereco_entry.grid(row=3, column=1)

id_label = Label(root, text="ID:")
id_label.grid(row=4, column=0)
id_entry = Entry(root)
id_entry.grid(row=4, column=1)

criar_button = Button(root, text="Criar", command=criar_cliente_gui)
criar_button.grid(row=5, column=0)

ler_button = Button(root, text="Ler", command=ler_clientes_gui)
ler_button.grid(row=5, column=1)

atualizar_button = Button(root, text="Atualizar", command=atualizar_cliente_gui)
atualizar_button.grid(row=6, column=0)

deletar_button = Button(root, text="Deletar", command=deletar_cliente_gui)
deletar_button.grid(row=6, column=1)

clientes_text = Text(root)
clientes_text.grid(row=7, column=0, columnspan=2)

root.mainloop()
conn.close()