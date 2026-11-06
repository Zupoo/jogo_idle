from flask import Flask, send_file
import time

app = Flask(__name__)

jogo = {  # aonde estao guardados as informaçoes do jogador e esta sendo e vai sendo atualizado por outras funçoes.
    "ouro": 10,
    "ouro_por_segundo": 0,
    "nivel_upgrade": 1,
    "custo_upgrade": 10,
    "itens": {"peixe_palhaco": 0, "anemonas": 0, "corais": 0},
    "ultima_coleta": time.time()
}

itens = {           #itens disponiveis no jogo e seus status, por exemplo o custo e a produção de ouro
    "peixe_palhaco": {"custo": 10, "ouro_por_segundo": 1},
    "anemonas": {"custo": 100, "ouro_por_segundo": 10},
    "corais": {"custo": 500, "ouro_por_segundo": 50}
}

def atualizar_ouro():       # funcao q calcula a quantidade de ouro farmado des de a ultima atualização
    jogo["ouro_por_segundo"] = 0
    agora = time.time()
    segundos = agora - jogo["ultima_coleta"]
    for item in jogo["itens"]:                  #multipicar a quantidade de itens q o jogador tem pela produção de ouro deles
        qtd_itens = jogo["itens"][item]
        jogo["ouro_por_segundo"] += qtd_itens * itens[item]["ouro_por_segundo"]
    jogo["ouro"] = jogo["ouro"] + segundos * jogo["ouro_por_segundo"]
    jogo["ultima_coleta"] = agora

@app.route("/status") #rota q retorna alguns status do personagem como ouro, ouro por segundo, nivel e custo de upgrade
def status():
    atualizar_ouro()
    return{
        "ouro": round(jogo["ouro"]),
        "ouro_por_segundo": jogo["ouro_por_segundo"],
        "nivel_upgrade": jogo["nivel_upgrade"],
        "custo_upgrade": round(jogo["custo_upgrade"]),
    }

@app.route("/upgrade", methods=["POST"]) 
def upgrade():
    atualizar_ouro()
    if jogo["ouro"] >= jogo["custo_upgrade"]:
        jogo["ouro"] -= jogo["custo_upgrade"]
        jogo["ouro_por_segundo"] += 1
        jogo["custo_upgrade"] *= 1.5
        jogo["nivel_upgrade"] += 1
        return{"comprou": True, "nivel_upgrade": jogo["nivel_upgrade"]}
    return {"comprou": False, "motivo": "ouro insuficiente"}

@app.route("/loja")  
def loja():
    return itens

@app.route("/comprar/<item_id>", methods=["POST"])
def comprar(item_id):
    atualizar_ouro()
    print("item id", item_id)

    if item_id not in itens:
        return{"comprou": False, "motivo": "item não existe"}, 404

    custo = itens[item_id]["custo"]

    if jogo["ouro"] >= custo:
        jogo["ouro"] -= custo
        jogo["itens"][item_id] += 1
        return {"comprou": True, "item": item_id}

    return {"comprou": False, "motivo": "ouro insuficiente"}






@app.route("/")
def pagina():
    return send_file("index.html")
app.run(port=5001)

