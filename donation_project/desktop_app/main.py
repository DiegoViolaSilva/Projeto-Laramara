
```python
# desktop_app/main.py
import tkinter as tk
from tkinter import messagebox
from donation_app.donation import get_donations
from donation_app.community import save_community, get_communities
from donation_app.admin import view_money_donations, view_item_donations

root = tk.Tk()
root.title("Instituto Center Norte - Administração")
root.geometry("400x400")

def admin_dashboard():
    dashboard_window = tk.Toplevel(root)
    dashboard_window.title("Dashboard do Administrador")
    
    tk.Button(dashboard_window, text="Visualizar Doações em Dinheiro", command=show_money_donations).pack()
    tk.Button(dashboard_window, text="Visualizar Doações em Alimentos/Roupas", command=show_item_donations).pack()
    tk.Button(dashboard_window, text="Cadastrar Comunidade/Instituição", command=register_community).pack()

def show_money_donations():
    money_donations_window = tk.Toplevel(root)
    money_donations_window.title("Doações em Dinheiro")
    
    donations = view_money_donations()
    tk.Label(money_donations_window, text="Lista de Doações em Dinheiro").pack()
    for donation in donations:
        tk.Label(money_donations_window, text=str(donation)).pack()

def show_item_donations():
    item_donations_window = tk.Toplevel(root)
    item_donations_window.title("Doações em Alimentos/Roupas")
    
    donations = view_item_donations()
    tk.Label(item_donations_window, text="Lista de Doações em Alimentos/Roupas").pack()
    for donation in donations:
        tk.Label(item_donations_window, text=str(donation)).pack()

def register_community():
    community_window = tk.Toplevel(root)
    community_window.title("Cadastro de Comunidade/Instituição")
    
    tk.Label(community_window, text="Nome da Comunidade/Instituição").pack()
    name_entry = tk.Entry(community_window)
    name_entry.pack()
    
    tk.Label(community_window, text="Endereço").pack()
    address_entry = tk.Entry(community_window)
    address_entry.pack()
    
    tk.Label(community_window, text="Contato").pack()
    contact_entry = tk.Entry(community_window)
    contact_entry.pack()
    
    def save_community_data():
        name = name_entry.get()
        address = address_entry.get()
        contact = contact_entry.get()
        save_community(name, address, contact)
        messagebox.showinfo("Cadastro", "Comunidade/Instituição cadastrada com sucesso!")
        community_window.destroy()
    
    tk.Button(community_window, text="Cadastrar", command=save_community_data).pack()

tk.Button(root, text="Administração", command=admin_dashboard).pack()

root.mainloop()
