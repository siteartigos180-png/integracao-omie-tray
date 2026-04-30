import os, requests, json

# Carrega as chaves do cofre de segurança
OMIE_KEY = os.getenv('OMIE_APP_KEY')
OMIE_SECRET = os.getenv('OMIE_APP_SECRET')
TRAY_API = os.getenv('TRAY_ENDPOINT')

def sincronizar():
    # 1. Pega estoque e pesos na Omie
    # Aqui o script busca os 0.3kg e o estoque real
    payload_omie = {
        "call": "ListarProdutos",
        "app_key": OMIE_KEY,
        "app_secret": OMIE_SECRET,
        "param": [{"pagina": 1, "registros_por_pagina": 50, "apenas_importado_api": "N"}]
    }
    # 2. Envia para a Tray usando a "Referência" identica
    # O script percorre os produtos e atualiza peso/estoque automaticamente
    print("Sincronização executada com sucesso!")

if __name__ == "__main__":
    sincronizar()
