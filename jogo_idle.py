import time

ouro = 0
ouro_por_segundo = 1
custo_upgrade = 10
ultima_coleta = time.time()
nivel_upgrade = 1

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

