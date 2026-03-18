import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA (ESTILO PROFISSIONAL) ---
st.set_page_config(page_title="Trailer do Alan", page_icon="🍔", layout="centered")

# CSS para mudar as cores do site (Tirando a branquidão)
st.markdown("""
    <style>
    .stApp {
        background-color: #1E1E1E; /* Fundo Grafite Escuro */
        color: white;
    }
    .stButton>button {
        background-color: #FFD700; /* Botão Dourado */
        color: black;
        font-weight: bold;
        border-radius: 10px;
    }
    h1, h2, h3 {
        color: #FFA500; /* Títulos Laranja */
    }
    div[data-baseweb="select"] > div {
        background-color: #333;
        color: white;
    }
    </style>
    """, unsafe_allow_config=True)

st.title("🍔 Trailer do Alan - Cardápio Online")
st.write("Monte seu lanche e receba quentinho em casa!")

# --- BARRA LATERAL (CADASTRO) ---
st.sidebar.header("👤 Seus Dados")
nome = st.sidebar.text_input("Nome completo")
endereco = st.sidebar.text_input("Endereço de entrega")
telefone = st.sidebar.text_input("Seu WhatsApp (com DDD)")

# --- CARDÁPIO E PREÇOS ---
st.header("🛒 Escolha seu Lanche")

# Dicionário de preços
precos_lanches = {
    "X-Burger": 20.00,
    "X-Salada": 22.00,
    "X-Tudo": 28.00,
    "Combo Alan (Lanche + Batata + Refri)": 35.00
}

escolha = st.selectbox("Selecione o lanche principal:", list(precos_lanches.keys()))
valor_base = precos_lanches[escolha]

st.subheader("➕ Adicionais (Turbine seu lanche)")
col1, col2 = st.columns(2)

with col1:
    bacon = st.checkbox("Bacon Extra (R$ 4,00)")
    queijo = st.checkbox("Queijo Extra (R$ 3,00)")

with col2:
    ovo = st.checkbox("Ovo (R$ 2,00)")
    maionese = st.checkbox("Maionese Caseira (R$ 1,50)")

# --- LÓGICA DE CÁLCULO ---
total = valor_base
adicionais_lista = []

if bacon: 
    total += 4.00
    adicionais_lista.append("Bacon")
if queijo: 
    total += 3.00
    adicionais_lista.append("Queijo")
if ovo: 
    total += 2.00
    adicionais_lista.append("Ovo")
if maionese: 
    total += 1.50
    adicionais_lista.append("Maionese")

# Mostra o valor em tempo real
st.markdown(f"## 💰 Total do Pedido: **R$ {total:.2f}**")

# --- FINALIZAÇÃO ---
if st.button("🛒 FINALIZAR MEU PEDIDO"):
    if nome and endereco and telefone:
        # Montagem da mensagem profissional para o WhatsApp
        str_adicionais = ", ".join(adicionais_lista) if adicionais_lista else "Nenhum"
        
        mensagem = (
            f"🍔 *NOVO PEDIDO DO TRAILER* 🍔\n\n"
            f"👤 *Cliente:* {nome}\n"
            f"📍 *Endereço:* {endereco}\n"
            f"📱 *Tel:* {telefone}\n"
            f"--------------------------\n"
            f"🥪 *Lanche:* {escolha}\n"
            f"🥓 *Adicionais:* {str_adicionais}\n"
            f"💵 *VALOR TOTAL:* R$ {total:.2f}\n"
            f"--------------------------\n"
            f"⏰ Aguardando confirmação..."
        )
        
        # Link do WhatsApp (Troque pelo número real do Alan)
        numero_alan = "5511999999999" 
        link_wa = f"https://wa.me/{numero_alan}?text={mensagem.replace(' ', '%20').replace('\n', '%0A')}"
        
        st.success("✅ Pedido calculado! Agora clique no botão abaixo para enviar para a cozinha:")
        st.link_button("🔥 ENVIAR PARA O WHATSAPP DO ALAN", link_wa)
    else:
        st.warning("⚠️ Por favor, preencha seus dados na barra lateral antes de finalizar!")
