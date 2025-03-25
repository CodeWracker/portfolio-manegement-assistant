# categories.py
from enum import Enum

class Tipo(Enum):
    """
    Tipo é o nível mais geral da classificação.
    Exemplo: Caixa, FII, Renda Fixa, Variável (BR), Internacional, Cripto etc.
    """
    CAIXA = "Caixa"
    FII = "FII"
    RENDA_FIXA = "Renda Fixa"
    VARIAVEL_BR = "Variavel BR"
    INTERNACIONAL = "Internacional"
    CRIPTO = "Cripto"
    # Acrescente outros tipos se necessário


class Categoria(Enum):
    """
    Categoria representa um agrupamento dentro de cada tipo.
    Exemplo (para FII): FOF, Papel, Tijolo, Corporativo...
    Exemplo (para Renda Fixa): CDI, Tesouro Direto, CDB, etc.
    Exemplo (para Ações BR): Ações, ETF BR
    Exemplo (para Internacional): BDR, ETF INT
    Exemplo (para Cripto): pode ser algo mais genérico (CriptoCategory) 
    ou dividido conforme estratégia.
    """
    # Dinheiro em Caixa
    CORRETORA = "Corretora"
    
    # FII
    FOF = "FOF"
    PAPEL = "Papel"
    TIJOLO = "Tijolo"
    CORPORATIVO = "Corporativo"

    # Renda Fixa
    CDI = "CDI"
    TESOURO_DIRETO = "Tesouro Direto"

    # Variável BR
    ACOES = "Ações"
    ETF_BR = "ETF BR"

    # Internacional
    BDR = "BDR"
    ETF_INT = "ETF INT"

    # Cripto
    CRIPTO_CATEGORY = "CriptoCategory"  # Se quiser agrupar todas as subcategorias cripto
    # ou crie categorias mais específicas (por ex.: "Cripto DeFi", "Cripto Layer1" etc.)

    # Adicione outras categorias conforme precisar


class Subcategoria(Enum):
    """
    Subcategoria é o nível mais específico.
    Exemplo (para FII): subdivisões de FOF, Papel etc.
    Exemplo (para Renda Fixa): Prefixado, IPCA+, Selic etc.
    Exemplo (para Ações BR): Setores (Bancos, Energia, Saneamento etc.)
    Exemplo (para Cripto): subdividir em 'Store of Value', 'Smart Contract', 'DeFi', etc.,
    permitindo uma diversificação mais detalhada dentro de Cripto.
    """
    
    # --------------------
    # Exemplo Corretora
    # --------------------
    RICO = "Rico"

    # --------------------
    # Exemplo FII
    # --------------------
    FOF_BTG = "FOF_BTG"                # FII FOF gerido pelo BTG, etc.
    PAPEL_TVM = "Papel_TitulosImob"    # Papel lastreado em Títulos Imobiliários
    TIJOLO_HIBRIDO = "Tijolo_Hibrido"
    TIJOLO_LOGISTICO = "Tijolo_Logistico"
    TIJOLO_SHOPPINGS = "Tijolo_Shoppings"
    CORPORATIVO_SHOPPINGS = "Corporativo_Shoppings"
    # ... e assim por diante

    # --------------------
    # Exemplo Renda Fixa
    # --------------------
    CDI_NUBANK = "CDI_Nubank"
    TD_PREFIXADO = "Prefixado"
    TD_IPCA = "IPCA+"
    TD_SELIC = "SELIC"
    # ... e assim por diante

    # --------------------
    # Exemplo Ações BR
    # --------------------
    ACOES_BANCO = "Banco"
    ACOES_AERONAUTICA = "Aeronautica"
    ACOES_ENERGIA = "Energia"
    ACOES_SANEAMENTO = "Saneamento"
    # ... e assim por diante

    # --------------------
    # Exemplo ETFs BR
    # --------------------
    ETF_BR_BR = "ETF_Brasil"

    # --------------------
    # Exemplo Internacional
    # --------------------
    BDR_SAUDE = "Saude"
    BDR_TECH_INT = "Tech INT"
    ETF_INT_CHINA = "China"
    ETF_INT_EUA = "EUA"
    ETF_INT_EUROPA = "Europa"
    ETF_INT_MUNDO = "Mundo"
    # ... e assim por diante

    # --------------------
    # Exemplo Cripto
    # (Subdividindo de forma a separar comportamentos distintos)
    # --------------------
    STORE_OF_VALUE = "StoreOfValue"            # ex: Bitcoin, Litecoin
    SMART_CONTRACT = "SmartContractPlatform"   # ex: Ethereum, Cardano
    DEFI = "DeFi"                              # ex: Uniswap, Aave
    EXCHANGE_TOKEN = "ExchangeToken"           # ex: BNB, OKB
    MEME = "Meme"                              # ex: Dogecoin, Shiba
    PRIVACY = "Privacy"                        # ex: Monero, Zcash
    STABLECOIN = "Stablecoin"                  # ex: USDT, USDC, DAI
    PAYMENT = "Payment"                        # ex: XRP, XLM
    ORACLE = "Oracle"                          # ex: Chainlink
    INTEROPERABILITY = "Interoperability"      # ex: Polkadot, Cosmos
    # ... e assim por diante
