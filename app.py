import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Trailer do Alan", page_icon="🍔", layout="centered")

# CSS Corrigido (Trocando config por html)
st.markdown("""
    <style>
    .stApp {
        background-color: #1E1E1E;
        color: white;
    }
    .stButton>button {
        background-color: #FFD700;
        color: red;
        font-weight: bold;
        border-radius: 10px;
        width: 100%;
    }
    h1, h2, h3 {
        color: #FFA500;
    }
    /* Estilo para as caixas de texto e seleção */
    input, div[data-baseweb="select"] {
        background-color: #333 !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🍔 Trailer do Alan - Cardápio Online")

# --- BARRA LATERAL (CADASTRO) ---
st.sidebar.header("👤 Seus Dados")
nome = st.sidebar.text_input("Nome completo")
endereco = st.sidebar.text_input("Endereço de entrega")
telefone = st.sidebar.text_input("Seu WhatsApp (com DDD)")

# --- CARDÁPIO E PREÇOS ---
st.header("🛒 Escolha seu Lanche")

precos_lanches = {
    "X-Burger": 20.00,
    "X-Salada": 22.00,
    "X-Tudo": 28.00,
    "Combo Alan (Lanche + Batata + Refri)": 35.00
}

escolha = st.selectbox("Selecione o lanche principal:", list(precos_lanches.keys()))
valor_base = precos_lanches[escolha]

st.subheader("➕ Adicionais")
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

st.markdown(f"## 💰 Total do Pedido: **R$ {total:.2f}**")

# --- FINALIZAÇÃO ---
if st.button("🛒 FINALIZAR MEU PEDIDO"):
    if nome and endereco and telefone:
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
        
        # COLOQUE O NÚMERO DO ALAN AQUI:
        numero_alan = "5511999999999" 
        link_wa = f"https://wa.me/{numero_alan}?text={mensagem.replace(' ', '%20').replace('\n', '%0A')}"
        
        st.success("✅ Pedido organizado!")
        st.link_button("🔥 ENVIAR PARA O WHATSAPP DO ALAN", link_wa)
    else:
        st.warning("⚠️ Preencha Nome, Endereço e Telefone na barra lateral!")
