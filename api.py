from flask import Flask
import time

app = Flask(__name__)

jogo = {
    "ouro": 0,
    "ouro_por_segundo": 1,
    "nivel_upgrade": 1,
    "custo_upgrade": 10,
    "ultima_coleta": time.time()
}

def atualizar_ouro():
    agora = time.time()
    segundos = agora - jogo["ultima_coleta"]
    jogo["ouro"] = jogo["ouro"] + segundos * jogo["ouro_por_segundo"]
    jogo["ultima_coleta"] = agora

@app.route("/status")
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

app.run(port=5001)

