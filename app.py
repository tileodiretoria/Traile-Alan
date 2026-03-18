import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Trailer do Alan", page_icon="🍔")

# CSS PERSONALIZADO (Verde Menta)
st.markdown("""
    <style>
    .stApp { background-color: #E8F5E9; color: #1B5E20; }
    .stButton>button { 
        background-color: #2E7D32; color: white; 
        border-radius: 8px; width: 100%; font-weight: bold; 
    }
    .stCheckbox, .stTextInput, .stSelectbox {
        background-color: #FFFFFF; padding: 10px; 
        border-radius: 10px; border: 1px solid #C8E6C9;
    }
    h1, h2, h3 { color: #1B5E20; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("🍔 Trailer do Alan")

# --- 1. CONFIGURAÇÃO DO CARDÁPIO ---
cardapio = {
    "Selecione seu lanche...": {"preco": 0.00, "itens": "Escolha uma opção abaixo"},
    "X-Burger": {"preco": 20.00, "itens": "Pão, Carne, Queijo"},
    "X-Salada": {"preco": 22.00, "itens": "Pão, Carne, Queijo, Alface, Tomate"},
    "X-Egg-Bacon: {"preço": 30.00, "itens: "Pão, Carne, Queijo, Ovo e Bacon"}
    "X-Tudo": {"preco": 28.00, "itens": "Pão, Carne, Queijo, Ovo, Bacon, Salada, Milho"},
    "Combo Alan": {"preco": 35.00, "itens": "X-Burguer + Batata M + Refri Lata"}
}

# --- BARRA LATERAL (CLIENTE) ---
st.sidebar.header("📋 Dados de Entrega")
nome = st.sidebar.text_input("Seu Nome")
endereco = st.sidebar.text_input("Endereço Completo")
telefone = st.sidebar.text_input("WhatsApp (com DDD)")

# --- SELEÇÃO DO LANCHE ---
st.header("🛒 Monte seu Pedido")

opcoes_lanche = []
for n, info in cardapio.items():
    if n == "Selecione seu lanche...":
        opcoes_lanche.append(n)
    else:
        opcoes_lanche.append(f"{n} - R$ {info['preco']:.2f} ({info['itens']})")

escolha_lanche_formatada = st.selectbox("Escolha seu lanche principal:", opcoes_lanche)
nome_lanche = escolha_lanche_formatada.split(" - ")[0]
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

# --- SEÇÃO DE BEBIDAS (COM PREÇOS VISÍVEIS!) ---
st.subheader("🥤 Bebidas")
bebidas = {
    "Nenhuma": 0.0,
    "Refri em Lata": 5.0,
    "Refri 1 Litro": 10.0,
    "Refri 2 Litros": 15.0
}

# Criamos a lista de texto para o cliente ver o preço
opcoes_bebida = []
for b, p in bebidas.items():
    if b == "Nenhuma":
        opcoes_bebida.append(b)
    else:
        opcoes_bebida.append(f"{b} - R$ {p:.2f}")

escolha_bebida_formatada = st.selectbox("Deseja adicionar refrigerante?", opcoes_bebida)
# Pegamos apenas o nome da bebida para buscar o preço no dicionário
nome_bebida = escolha_bebida_formatada.split(" - ")[0]
valor_bebida = bebidas[nome_bebida]

# --- OBSERVAÇÕES ---
st.subheader("📝 Observações")
obs = st.text_area("Ex: Ponto da carne, retirar ingrediente, etc.")

# --- LÓGICA DE CÁLCULO TOTAL ---
total = valor_base + valor_bebida
extras = []
if add_bacon: total += 4.0; extras.append("Bacon")
if add_queijo: total += 3.0; extras.append("Queijo")
if add_ovo: total += 2.0; extras.append("Ovo")
if add_maio: total += 1.5; extras.append("Maionese")

st.write("---")
st.markdown(f"### 💰 Total a Pagar: **R$ {total:.2f}**")

# --- FINALIZAÇÃO ---
if st.button("🚀 FINALIZAR E ENVIAR PEDIDO"):
    if nome_lanche == "Selecione seu lanche...":
        st.error("⚠️ Por favor, escolha um lanche do cardápio!")
    elif nome and endereco and telefone:
        lista_extras = ", ".join(extras) if extras else "Nenhum"
        
        mensagem = (
            f"🍔 *PEDIDO DO TRAILER* 🍔\n\n"
            f"*Cliente:* {nome}\n"
            f"*Endereço:* {endereco}\n"
            f"--------------------------\n"
            f"*Lanche:* {nome_lanche}\n"
            f"*Adicionais:* {lista_extras}\n"
            f"*Bebida:* {nome_bebida}\n"
            f"*Observações:* {obs if obs else 'Nenhuma'}\n"
            f"--------------------------\n"
            f"💵 *VALOR TOTAL:* R$ {total:.2f}"
        )
        
        # Coloque o número do Alan aqui (ex: 5511999999999)
        numero_alan = "5511999999999" 
        link_wa = f"https://wa.me/{numero_alan}?text={mensagem.replace(' ', '%20').replace('\n', '%0A')}"
        
        st.success("Tudo pronto! Clique no botão abaixo:")
        st.link_button("✅ ENVIAR PARA O WHATSAPP DO ALAN", link_wa)
    else:
        st.error("⚠️ Preencha Nome, Endereço e Telefone na barra lateral!")
