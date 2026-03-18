import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Trailer do Alan", page_icon="🍔")

# CSS PERSONALIZADO (Verde Claro e Moderno)
st.markdown("""
    <style>
    .stApp {
        background-color: #E8F5E9; /* Verde bem clarinho */
        color: #1B5E20; /* Texto Verde Escuro */
    }
    .stButton>button {
        background-color: #2E7D32; /* Botão Verde Forte */
        color: white;
        border-radius: 8px;
        height: 3em;
        width: 100%;
        font-weight: bold;
    }
    /* Estilo para as caixas de seleção e texto */
    .stCheckbox, .stTextInput, .stSelectbox {
        background-color: #FFFFFF;
        padding: 10px;
        border-radius: 10px;
        border: 1px solid #C8E6C9;
        margin-bottom: 10px;
    }
    h1, h2 {
        color: #1B5E20;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🍔 Trailer do Alan")
st.write("---")

# --- 1. CONFIGURAÇÃO DO CARDÁPIO (Fácil de mudar aqui!) ---
# Aqui você muda o nome, o preço e o que vem dentro
cardapio = {
    "X-Burger": {"preco": 20.00, "itens": "Pão, Carne, Queijo"},
    "X-Salada": {"preco": 22.00, "itens": "Pão, Carne, Queijo, Alface, Tomate"},
    "X-Tudo": {"preco": 28.00, "itens": "Pão, Carne, Queijo, Ovo, Bacon, Salada, Milho"},
    "Combo Alan": {"preco": 35.00, "itens": "X-Burger + Batata M + Refri Lata"}
}

# --- BARRA LATERAL (CLIENTE) ---
st.sidebar.header("📋 Dados de Entrega")
nome = st.sidebar.text_input("Seu Nome")
endereco = st.sidebar.text_input("Endereço Completo")
telefone = st.sidebar.text_input("WhatsApp (com DDD)")

# --- SELEÇÃO DO LANCHE ---
st.header("🛒 Monte seu Pedido")

# Criamos a lista de opções com Nome + Preço + Ingredientes
opcoes = [f"{nome} - R$ {info['preco']:.2f} ({info['itens']})" for nome, info in cardapio.items()]
escolha_formatada = st.selectbox("Selecione seu lanche principal:", opcoes)

# Extraímos o nome do lanche e o preço da escolha feita
nome_lanche = escolha_formatada.split(" - ")[0]
valor_base = cardapio[nome_lanche]["preco"]

# --- ADICIONAIS ---
st.subheader("➕ Adicionais Extras")
c1, c2 = st.columns(2)
with c1:
    add_bacon = st.checkbox("Bacon Extra (+ R$ 4,00)")
    add_queijo = st.checkbox("Queijo Extra (+ R$ 3,00)")
with c2:
    add_ovo = st.checkbox("Ovo (+ R$ 2,00)")
    add_maio = st.checkbox("Maionese Caseira (+ R$ 1,50)")
with c3:
    add_refri = st.checkbox("Coca cola (+ R$ 5,00)")
    add_refri = st.checkbox("Fanta (+ R$ 5,00)")

# --- OBSERVAÇÕES ---
st.subheader("📝 Observações")
obs = st.text_area("Ex: Tirar cebola, ponto da carne, trocar refri, etc.")

# --- CÁLCULO TOTAL ---
total = valor_base
extras = []
if add_bacon: total += 4.0; extras.append("Bacon")
if add_queijo: total += 3.0; extras.append("Queijo")
if add_ovo: total += 2.0; extras.append("Ovo")
if add_maio: total += 1.5; extras.append("Maionese")
if add_refri: total += 5.00; extras.append("Refri lata")
if add_refri: total += 5.00; extras.append("Refri lata")      

st.write("---")
st.markdown(f"### 💰 Total a Pagar: **R$ {total:.2f}**")

# --- BOTÃO FINAL ---
if st.button("🚀 FINALIZAR E ENVIAR PEDIDO"):
    if nome and endereco and telefone:
        # Montagem da mensagem
        lista_extras = ", ".join(extras) if extras else "Nenhum"
        mensagem = (
            f"🍔 *PEDIDO DO TRAILER* 🍔\n\n"
            f"*Cliente:* {nome}\n"
            f"*Endereço:* {endereco}\n"
            f"--------------------------\n"
            f"*Lanche:* {nome_lanche}\n"
            f"*Adicionais:* {lista_extras}\n"
            f"*Observações:* {obs if obs else 'Nenhuma'}\n"
            f"--------------------------\n"
            f"💵 *VALOR TOTAL:* R$ {total:.2f}"
        )
        
        # NÚMERO DO ALAN (Ajuste aqui)
        numero_alan = "5511999999999" 
        link_wa = f"https://wa.me/{numero_alan}?text={mensagem.replace(' ', '%20').replace('\n', '%0A')}"
        
        st.success("Pedido pronto! Clique abaixo para abrir seu WhatsApp.")
        st.link_button("✅ ENVIAR PARA O ALAN", link_wa)
    else:
        st.error("⚠️ Preencha Nome, Endereço e Telefone na barra lateral!")
