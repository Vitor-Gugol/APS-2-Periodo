import math
from time import sleep
from tkinter import *

def code():
    kWh = float(entrada_kWh.get())

    resultado_text.delete(1.0, END)

    resultado_text.insert(INSERT, "Consumo de energia em kWh: " + str(kWh) + "\n")
    resultado_text.insert(INSERT, "Tipo de energia: " + fonte_energia_var.get() + "\n\n")

    FatorEmissao = 0
    fonte_energia = fonte_energia_var.get()

    if fonte_energia == "Carvão":
        FatorEmissao = 2.2 / 1000
    if fonte_energia == "Gás natural":
        FatorEmissao = 0.4 / 1000
    if fonte_energia == "Petróleo":
        FatorEmissao = 2.2 / 1000
    if fonte_energia == "Nuclear":
        resultado_text.insert(INSERT, "A geração de eletricidade a partir de usinas nucleares é considerada de baixa emissão de carbono, com emissões de CO2 muito baixas ou próximas a zero.")
    if fonte_energia == "Hidrelétrica":
        resultado_text.insert(INSERT, "A geração de eletricidade a partir de usinas hidrelétricas é considerada uma fonte de energia de baixa emissão de carbono, com emissões de CO2 muito baixas ou próximas a zero.")
    if fonte_energia == "Eólica" or fonte_energia == "Solar":
        resultado_text.insert(INSERT, "A geração de eletricidade a partir de fontes de energia eólica e solar é considerada praticamente livre de emissões de carbono. As emissões associadas à fabricação e instalação de painéis solares e turbinas eólicas são muito menores em comparação com a eletricidade gerada.")

    EmissaoCarbono = kWh * FatorEmissao
    resultado_text.insert(INSERT, "Emissões de CO2: %.2f toneladas ou %.2f kg\n" % (EmissaoCarbono, EmissaoCarbono * 1000))

    CreditoDeCarbono = math.ceil(EmissaoCarbono)  # Arredonde CreditoDeCarbono para cima
    resultado_text.insert(INSERT, "Crédito de carbono necessário: %.0f\n" % CreditoDeCarbono)
    
    # Defina o ValorCredito de acordo com a moeda que você deseja usar (por exemplo, 25 reais por crédito de carbono)
    ValorCredito = 25
    
    CreditoExcedente = max(0, CreditoDeCarbono - EmissaoCarbono)  # Certifique-se de que o CreditoExcedente seja não negativo
    resultado_text.insert(INSERT, "Crédito Excedente: %.2f\n" % CreditoExcedente," toneladas")  # Exibe o CreditoExcedente
    
    LucroEstimado = CreditoExcedente * ValorCredito
    resultado_text.insert(INSERT, "Lucro Estimado: R$ %.2f\n" % LucroEstimado)

janela = Tk()
janela.title("Calculadora de Emissões de Carbono")
janela.geometry("600x400")
janela.configure(bg="dim gray")  # Define o fundo da janela como cinza chumbo

titulo_label = Label(janela, text="Calculadora de Emissões de Carbono", font=("Arial", 16), bg="dim gray", fg="white")
titulo_label.grid(column=0, row=0, padx=20, pady=10, columnspan=2)

entrada_kWh_label = Label(janela, text="Consumo de energia em kWh:", bg="dim gray", fg="white")
entrada_kWh_label.grid(column=0, row=1, sticky="w", padx=20, pady=5)

entrada_kWh = Entry(janela, bg="dim gray", fg="white")
entrada_kWh.grid(column=1, row=1, padx=20, pady=5)

fonte_energia_label = Label(janela, text="Escolha a fonte de energia:", bg="dim gray", fg="white")
fonte_energia_label.grid(column=0, row=2, sticky="w", padx=20, pady=5)

fonte_energia_opcoes = ["Carvão", "Gás natural", "Petróleo", "Nuclear", "Hidrelétrica", "Eólica", "Solar"]
fonte_energia_var = StringVar(janela)
fonte_energia_var.set(fonte_energia_opcoes[0])
fonte_energia_menu = OptionMenu(janela, fonte_energia_var, *fonte_energia_opcoes)
fonte_energia_menu.configure(bg="dim gray", fg="white")
fonte_energia_menu.grid(column=1, row=2, sticky="w", padx=20, pady=5)

botao = Button(janela, text="Calcular", command=code, bg="dim gray", fg="white")
botao.grid(column=0, row=3, columnspan=2, pady=10)

resultado_text = Text(janela, height=10, width=50, bg="dim gray", fg="white")
resultado_text.grid(column=0, row=4, padx=20, pady=10, columnspan=2)

janela.mainloop()
