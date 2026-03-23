import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Trailer do Alan - Cardápio", page_icon="🍔", layout="centered")

# --- ESTILO VISUAL (AZUL CLARO E BRANCO NEVE) ---
st.markdown("""
    <style>
    .stApp { background-color: #F0F8FF; } /* Azul Claro / Alice Blue */
    .main-title { color: #0077b6; font-size: 38px; font-weight: bold; text-align: center; margin-bottom: 5px; }
    .sub-title { color: #0077b6; font-size: 18px; text-align: center; margin-bottom: 30px; }
    .stButton>button { 
        background-color: #00b4d8; color: white; width: 100%; border-radius: 12px; 
        height: 50px; font-weight: bold; border: none; transition: 0.3s;
    }
    .stButton>button:hover { background-color: #0077b6; border: 1px solid white; }
    .footer-total { 
        position: fixed; bottom: 0; left: 0; width: 100%; background-color: white; 
        padding: 15px; text-align: center; border-top: 3px solid #00b4d8; z-index: 100;
    }
    .card-lanche { background-color: white; padding: 15px; border-radius: 15px; margin-bottom: 10px; border-left: 5px solid #00b4d8; }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown('<p class="main-title">🍔 Trailer do Alan</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">O melhor hambúrguer da região!</p>', unsafe_allow_html=True)

# Banner Principal (Imagem Apetitosa)
st.image("https://images.unsplash.com/photo-1594212699903-ec8a3eca50f5?q=80&w=1000&auto=format&fit=crop", use_container_width=True)

# --- SISTEMA DE CARRINHO (SESSION STATE) ---
if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []

def adicionar_ao_carrinho(nome, preco):
    st.session_state.carrinho.append({"item": nome, "preco": preco})
    st.toast(f"✅ {nome} adicionado!")

# --- ABAS DE NAVEGAÇÃO ---
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🍔 Lanches", "➕ Adicionais", "🥤 Bebidas", "🍰 Doces", "🏁 Finalizar"])

# --- ABA 1: LANCHES ---
with tab1:
    st.info("🍅 Todos os lanches acompanham Alface e Tomate por padrão.")
    
    tipos = ["Simples", "Frango", "Lombo", "Picanha"]
    precos_base = {"Simples": 10, "Frango": 12, "Lombo": 14, "Picanha": 18}

    for t in tipos:
        with st.expander(f"✨ Opções de Hambúrguer de {t}"):
            # Variações solicitadas
            p = precos_base[t]
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"X-{t} (Queijo)\nR$ {p+5:.2f}", key=f"x{t}"):
                    adicionar_ao_carrinho(f"X-{t} (Queijo)", p+5)
                
                if st.button(f"X-Egg {t}\nR$ {p+8:.2f}", key=f"egg{t}"):
                    adicionar_ao_carrinho(f"X-Egg {t}", p+8)
            
            with col2:
                if st.button(f"X-Bacon {t}\nR$ {p+10:.2f}", key=f"bac{t}"):
                    adicionar_ao_carrinho(f"X-Bacon {t}", p+10)
                
                if st.button(f"X-Egg Bacon {t}\nR$ {p+15:.2f}", key=f"eggbac{t}"):
                    adicionar_ao_carrinho(f"X-Egg Bacon {t}", p+15)

    st.markdown("---")
    if st.button("👑 X-TUDO DO ALAN (Todos os Bifes + Todos Ingredientes) - R$ 45,00"):
        adicionar_ao_carrinho("X-Tudo Especial", 45.00)

# --- ABA 2: ADICIONAIS ---
with tab2:
    st.subheader("➕ Adicione um toque extra")
    adics = {
        "Queijo": 3, "Presunto": 3, "Ovo": 3, "Bacon": 5, "Milho": 2, 
        "Batata": 4, "Catupiry": 5, "Hamb. Simples": 7, "Hamb. Picanha": 12
    }
    cols = st.columns(2)
    for i, (item, preco) in enumerate(adics.items()):
        if cols[i % 2].button(f"{item} (+ R$ {preco:.2f})", key=f"add{item}"):
            adicionar_ao_carrinho(f"Adicional {item}", preco)

# --- ABA 3: BEBIDAS ---
with tab3:
    st.subheader("🥤 Refrigerantes")
    refris = {"Lata": 5, "600ml": 8, "1 Litro": 10, "2 Litros": 15}
    for tam, preco in refris.items():
        if st.button(f"Refri {tam} - R$ {preco:.2f}"):
            adicionar_ao_carrinho(f"Refri {tam}", preco)

# --- ABA 4: SOBREMESAS ---
with tab4:
    st.subheader("🍰 Sobremesas")
    doces = {"Brigadeiro": 4, "Beijinho": 4, "Doce Amendoim": 3, "Doce Morango": 5}
    for doce, preco in doces.items():
        if st.button(f"{doce} - R$ {preco:.2f}"):
            adicionar_ao_carrinho(doce, preco)

# --- ABA 5: FINALIZAR ---
with tab5:
    st.subheader("👤 Identificação e Entrega")
    nome = st.text_input("Seu Nome:")
    tel = st.text_input("Telefone:")
    end = st.text_input("Endereço Completo:")
    comp = st.text_input("Complemento (Apto, bloco, casa):")
    
    st.write("---")
    st.warning("📝 Caso não queira algum item do lanche, coloque aqui. Ex: Não colocar alface e tomate")
    obs = st.text_area("Suas Observações:")

    total_final = sum(item['preco'] for item in st.session_state.carrinho)
    
    if st.button("🟢 ENVIAR PEDIDO PELO WHATSAPP"):
        if nome and end and st.session_state.carrinho:
            # Montagem da Mensagem
            itens_lista = "\n".join([f"- {i['item']}: R$ {i['preco']:.2f}" for i in st.session_state.carrinho])
            mensagem = f"*PEDIDO - TRAILER DO ALAN*\n\n" \
                       f"*Cliente:* {nome}\n" \
                       f"*Endereço:* {end}\n" \
                       f"*Complemento:* {comp}\n\n" \
                       f"*ITENS:*\n{itens_lista}\n\n" \
                       f"*OBS:* {obs}\n" \
                       f"---" \
                       f"\n*TOTAL: R$ {total_final:.2f}*"
            
            # Link do WhatsApp (Troque pelo número do Alan)
            numero_alan = "5511999999999" 
            link_wa = f"https://wa.me/{numero_alan}?text={mensagem.replace(' ', '%20').replace('\n', '%0A')}"
            
            st.success("Tudo pronto! Clique no botão abaixo para abrir seu WhatsApp.")
            st.link_button("Ir para o WhatsApp ✅", link_wa)
        else:
            st.error("Por favor, preencha os dados e escolha pelo menos um item!")

# --- RODAPÉ FIXO DO TOTAL ---
if st.session_state.carrinho:
    total_float = sum(item['preco'] for item in st.session_state.carrinho)
    st.markdown(f"""
        <div class="footer-total">
            <span style="color:#0077b6; font-size:20px; font-weight:bold;">
                🛒 Total do Pedido: R$ {total_float:.2f}
            </span>
        </div>
    """, unsafe_allow_html=True)
