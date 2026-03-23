import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Trailer do Alan - Cardápio", page_icon="🍔", layout="centered")

# --- ESTILO VISUAL (AZUL E BRANCO) ---
st.markdown("""
    <style>
    .stApp { background-color: #F0F8FF; }
    .main-title { color: #0077b6; font-size: 38px; font-weight: bold; text-align: center; margin-bottom: 5px; }
    .stButton>button { 
        background-color: #00b4d8; color: white; width: 100%; border-radius: 12px; 
        min-height: 80px; font-weight: bold; border: none; transition: 0.3s;
        font-size: 14px; margin-bottom: 10px;
    }
    .stButton>button:hover { background-color: #0077b6; transform: scale(1.02); }
    .footer-total { 
        position: fixed; bottom: 0; left: 0; width: 100%; background-color: white; 
        padding: 15px; text-align: center; border-top: 3px solid #00b4d8; z-index: 100;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="main-title">🍔 Trailer do Alan</p>', unsafe_allow_html=True)

# --- SISTEMA DE CARRINHO ---
if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []

def adicionar(nome, preco, desc):
    st.session_state.carrinho.append({"item": nome, "preco": preco, "desc": desc})
    st.toast(f"✅ {nome} adicionado!")

# --- ABAS ---
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🍔 Lanches", "➕ Adicionais", "🥤 Bebidas", "🍰 Doces", "🏁 Finalizar"])

# --- ABA 1: LANCHES (AJUSTADA) ---
with tab1:
    tipos = ["Hambúrguer", "Frango", "Lombo", "Picanha"]
    precos_base = {"Hambúrguer": 10, "Frango": 12, "Lombo": 14, "Picanha": 18}

    for t in tipos:
        with st.expander(f"✨ Opções de {t}"):
            p = precos_base[t]
            col1, col2 = st.columns(2)
            
            # Padronizando: Pão, Carne, Alface, Tomate + Ingrediente da Versão
            base_ing = f"Pão, {t}, Alface e Tomate"

            with col1:
                # X-Burger (Queijo)
                if st.button(f"X-{t}\n(Queijo)\nR$ {p+5:.2f}", key=f"x{t}"):
                    adicionar(f"X-{t}", p+5, f"{base_ing} e Queijo")
                
                # X-Egg
                if st.button(f"X-Egg {t}\n(Ovo)\nR$ {p+8:.2f}", key=f"egg{t}"):
                    adicionar(f"X-Egg {t}", p+8, f"{base_ing}, Queijo e Ovo")
                
                # X-Presunto (NOVO)
                if st.button(f"X-Presunto {t}\n(Presunto)\nR$ {p+7:.2f}", key=f"pre{t}"):
                    adicionar(f"X-Presunto {t}", p+7, f"{base_ing}, Queijo e Presunto")

            with col2:
                # X-Bacon
                if st.button(f"X-Bacon {t}\n(Bacon)\nR$ {p+10:.2f}", key=f"bac{t}"):
                    adicionar(f"X-Bacon {t}", p+10, f"{base_ing}, Queijo e Bacon")
                
                # X-Egg Bacon
                if st.button(f"X-Egg Bacon {t}\n(Ovo e Bacon)\nR$ {p+15:.2f}", key=f"eggbac{t}"):
                    adicionar(f"X-Egg Bacon {t}", p+15, f"{base_ing}, Queijo, Ovo e Bacon")
                
                # X-Bacon Presunto (NOVO)
                if st.button(f"X-Bacon Presunto {t}\n(Bacon e Presunto)\nR$ {p+13:.2f}", key=f"bacpre{t}"):
                    adicionar(f"X-Bacon Presunto {t}", p+13, f"{base_ing}, Queijo, Bacon e Presunto")

    st.markdown("---")
    if st.button("👑 X-TUDO DO ALAN (Todos os Bifes + Todos Ingredientes) - R$ 45,00"):
        adicionar("X-Tudo Especial", 45.00, "Todos os tipos de carne, Queijo, Ovo, Bacon, Presunto, Alface e Tomate")

# --- ABA 2: ADICIONAIS ---
with tab2:
    adics = {"Queijo": 3, "Presunto": 3, "Ovo": 3, "Bacon": 5, "Milho": 2, "Batata": 4, "Catupiry": 5}
    cols = st.columns(2)
    for i, (item, preco) in enumerate(adics.items()):
        if cols[i % 2].button(f"{item}\n+ R$ {preco:.2f}"):
            adicionar(f"Adicional {item}", preco, "Adicional extra")

# --- ABA 3: BEBIDAS ---
with tab3:
    refris = {"Lata": 5, "600ml": 8, "1 Litro": 10, "2 Litros": 15}
    for tam, preco in refris.items():
        if st.button(f"🥤 Refri {tam} - R$ {preco:.2f}"):
            adicionar(f"Refri {tam}", preco, "")

# --- ABA 4: SOBREMESAS ---
with tab4:
    doces = {"Brigadeiro": 4, "Beijinho": 4, "Doce Amendoim": 3, "Doce Morango": 5}
    for doce, preco in doces.items():
        if st.button(f"{doce} - R$ {preco:.2f}"):
            adicionar(doce, preco, "")

# --- ABA 5: FINALIZAR ---
with tab5:
    nome = st.text_input("Seu Nome:")
    tel = st.text_input("Telefone:")
    end = st.text_input("Endereço Completo:")
    obs = st.text_area("Observações (Ex: Sem cebola, tirar tomate):")

    total_final = sum(item['preco'] for item in st.session_state.carrinho)
    
    if st.button("🟢 ENVIAR PEDIDO PELO WHATSAPP"):
        if nome and end and st.session_state.carrinho:
            itens_lista = "\n".join([f"- {i['item']} ({i['desc']})" for i in st.session_state.carrinho])
            mensagem = f"*PEDIDO - TRAILER DO ALAN*\n\n*Cliente:* {nome}\n*Endereço:* {end}\n\n*ITENS:*\n{itens_lista}\n\n*OBS:* {obs}\n\n*TOTAL: R$ {total_final:.2f}*"
            
            # Número do Alan aqui
            link_wa = f"https://wa.me/5511999999999?text={mensagem.replace(' ', '%20').replace('\n', '%0A')}"
            st.link_button("Ir para o WhatsApp ✅", link_wa)
        else:
            st.error("Preencha os dados e escolha um lanche!")

# --- TOTAL FIXO ---
if st.session_state.carrinho:
    st.markdown(f'<div class="footer-total"><b>🛒 Total: R$ {sum(item["preco"] for item in st.session_state.carrinho):.2f}</b></div>', unsafe_allow_html=True)
