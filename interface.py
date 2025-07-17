import tkinter as tk
from tkinter import ttk

from Pablo.enigma.main import criptografar


def pressionar_tecla(letra):
    r1 = int(rotor1.get())
    r2 = int(rotor2.get())
    r3 = int(rotor3.get())

    letra_resultado = criptografar(letra,r1,r2,r3)
    letra_saida.set(letra_resultado)


janela = tk.Tk()
janela.title("Máquina Enigma")
janela.configure(bg="#c18c4d")


rotor_frame = tk.Frame(janela, bg="#c18c4d")
rotor_frame.pack(pady=10)

rotor1 = ttk.Combobox(rotor_frame, values=[1,2,3],  width=3)
rotor1.set(1)
rotor1.pack(side="left", padx=10)

rotor2 = ttk.Combobox(rotor_frame, values=[1,2,3], width=3)
rotor2.set(2)
rotor2.pack(side="left", padx=10)

rotor3 = ttk.Combobox(rotor_frame, values=[1,2,3], width=3)
rotor3.set(3)
rotor3.pack(side="left", padx=10)


plugboard_frame = tk.Frame(janela, bg="#c18c4d")
plugboard_frame.pack(pady=10)

pares_plug = ["M-U", "L-B", "Q-C", "Z-K"]
for par in pares_plug:
    lbl = tk.Label(plugboard_frame, text=par, font=("Courier", 12), bg="#c18c4d", fg="black")
    lbl.pack(side="left", padx=6)


letra_saida = tk.StringVar(value="")
saida_frame = tk.Frame(janela, bg="#c18c4d")
saida_frame.pack(pady=10)

lampada = tk.Label(saida_frame, textvariable=letra_saida, font=("Helvetica", 30, "bold"),
                   bg="green", fg="black", width=2)
lampada.pack()


teclado_frame = tk.Frame(janela, bg="#c18c4d")
teclado_frame.pack()

alfabeto = [chr(i) for i in range(65, 91)]  # A-Z

for idx, letra in enumerate(alfabeto):
    btn = tk.Button(teclado_frame, text=letra, width=3, height=2,
                    command=lambda l=letra: pressionar_tecla(l))
    btn.grid(row=idx // 13, column=idx % 13, padx=2, pady=2)


janela.mainloop()
