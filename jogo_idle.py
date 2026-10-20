import time
import json
import os

ouro = 0
ouro_por_segundo = 1
nivel_upgrade = 1
custo_upgrade = 10
ultima_coleta = time.time()


if os.path.exists("save.json"):
    with open("save.json") as arquivo:
        dados = json.load(arquivo)
    ouro = dados["ouro"]
    ouro_por_segundo = dados["ouro_por_segundo"]
    nivel_upgrade = dados["nivel_upgrade"]
    custo_upgrade = dados["custo_upgrade"]
    ultima_coleta = dados["ultima_coleta"]



print("==Jogo Idle====")

while True:
    comando = input("\n[u] comprar upgrade | [s] sair | [Enter] ver ouro | [i] status")


    #calcula quanto tempo passou desde a ultima coleta
    agora = time.time()
    segundos = agora - ultima_coleta
    ouro = ouro + segundos * ouro_por_segundo
    ultima_coleta = agora

    if comando == "u":
        if ouro >= custo_upgrade:
            ouro = ouro - custo_upgrade
            ouro_por_segundo = ouro_por_segundo +1
            custo_upgrade = custo_upgrade * 1.5
            print(f"Upgrade comprado lvl {nivel_upgrade} -> {nivel_upgrade + 1}")
            nivel_upgrade = nivel_upgrade + 1
        else:
            print("Ouro insuficiente")
    elif comando == "i":
        print(f"Produção de ouro / s {ouro_por_segundo}")
        
    elif comando == "s":
        break
    else:
        print(f"Ouro: {ouro:.0f} | Proximo upgrade: {custo_upgrade:.0f}")
dados = {
    "ouro": ouro,
    "ouro_por_segundo": ouro_por_segundo,
    "nivel_upgrade": nivel_upgrade,
    "custo_upgrade": custo_upgrade,
    "ultima_coleta": ultima_coleta,
}

with open("save.json", "w") as arquivo:
    json.dump(dados, arquivo)
print("Jogo salvo")
