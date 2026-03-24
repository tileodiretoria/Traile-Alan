import streamlit as st

# =========================================================
# 🛠️ PAINEL DE CONTROLE (ESTRUTURA SAGRADA DO LEO)
# =========================================================

TITULO_ABA_1, TITULO_ABA_2, TITULO_ABA_3 = "Hambúrguer Simples", "Hambúrguer de Frango", "Hambúrguer de Lombo"
TITULO_ABA_4, TITULO_ABA_5, TITULO_ABA_6 = "Hambúrguer de Picanha", "Filé de Frango", "🔥 X-TUDO"

ITENS_CARDAPIO = {
    TITULO_ABA_1: [{"n": "Hambúrguer", "p": 10.00, "ing": "Pão, Carne, Alface e Tomate"}, {"n": "X-Burger", "p": 15.00, "ing": "Pão, Carne, Queijo, Alface e Tomate"}, {"n": "X-Egg", "p": 18.00, "ing": "Pão, Carne, Queijo, Ovo, Alface e Tomate"}, {"n": "X-Bacon", "p": 20.00, "ing": "Pão, Carne, Queijo, Bacon, Alface e Tomate"}, {"n": "X-Presunto", "p": 17.00, "ing": "Pão, Carne, Queijo, Presunto, Alface e Tomate"}, {"n": "X-Bacon Presunto", "p": 23.00, "ing": "Pão, Carne, Queijo, Bacon, Presunto, Alface e Tomate"}, {"n": "X-Egg Bacon Presunto", "p": 26.00, "ing": "Pão, Carne, Queijo, Ovo, Bacon, Presunto, Alface e Tomate"}],
    TITULO_ABA_2: [{"n": "Hambúrguer Frango", "p": 12.00, "ing": "Pão, Frango, Alface e Tomate"}, {"n": "X-Burger Frango", "p": 17.00, "ing": "Pão, Frango, Queijo, Alface e Tomate"}, {"n": "X-Egg Frango", "p": 20.00, "ing": "Pão, Frango, Queijo, Ovo, Alface e Tomate"}, {"n": "X-Bacon Frango", "p": 22.00, "ing": "Pão, Frango, Queijo, Bacon, Alface e Tomate"}, {"n": "X-Presunto Frango", "p": 19.00, "ing": "Pão, Frango, Queijo, Presunto, Alface e Tomate"}, {"n": "X-Bacon Presunto Frango", "p": 25.00, "ing": "Pão, Frango, Queijo, Bacon, Presunto, Alface e Tomate"}, {"n": "X-Egg Bacon Presunto Frango", "p": 28.00, "ing": "Pão, Frango, Queijo, Ovo, Bacon, Presunto, Alface e Tomate"}],
    TITULO_ABA_3: [{"n": "Hambúrguer Lombo", "p": 14.00, "ing": "Pão, Lombo, Alface e Tomate"}, {"n": "X-Burger Lombo", "p": 19.00, "ing": "Pão, Lombo, Queijo, Alface e Tomate"}, {"n": "X-Egg Lombo", "p": 22.00, "ing": "Pão, Lombo, Queijo, Ovo, Alface e Tomate"}, {"n": "X-Bacon Lombo", "p": 24.00, "ing": "Pão, Lombo, Queijo, Bacon, Alface e Tomate"}, {"n": "X-Presunto Lombo", "p": 21.00, "ing": "Pão, Lombo, Queijo, Presunto, Alface e Tomate"}, {"n": "X-Bacon Presunto Lombo", "p": 27.00, "ing": "Pão, Lombo, Queijo, Bacon, Presunto, Alface e Tomate"}, {"n": "X-Egg Bacon Presunto Lombo", "p": 30.00, "ing": "Pão, Lombo, Queijo, Ovo, Bacon, Presunto, Alface e Tomate"}],
    TITULO_ABA_4: [{"n": "Hambúrguer Picanha", "p": 18.00, "ing": "Pão, Picanha, Alface e Tomate"}, {"n": "X-Burger Picanha", "p": 23.00, "ing": "Pão, Picanha, Queijo, Alface e Tomate"}, {"n": "X-Egg Picanha", "p": 26.00, "ing": "Pão, Picanha, Queijo, Ovo, Alface e Tomate"}, {"n": "X-Bacon Picanha", "p": 28.00, "ing": "Pão, Picanha, Queijo, Bacon, Alface e Tomate"}, {"n": "X-Presunto Picanha", "p": 25.00, "ing": "Pão, Picanha, Queijo, Presunto, Alface e Tomate"}, {"n": "X-Bacon Presunto Picanha", "p": 31.00, "ing": "Pão, Picanha, Queijo, Bacon, Presunto, Alface e Tomate"}, {"n": "X-Egg Bacon Presunto Picanha", "p": 34.00, "ing": "Pão, Picanha, Queijo, Ovo, Bacon, Presunto, Alface e Tomate"}],
    TITULO_ABA_5: [{"n": "Filé de Frango", "p": 15.00, "ing": "Pão, Filé, Alface e Tomate"}, {"n": "X-Burger Filé", "p": 20.00, "ing": "Pão, Filé, Queijo, Alface e Tomate"}, {"n": "X-Egg Filé", "p": 23.00, "ing": "Pão, Filé, Queijo, Ovo, Alface e Tomate"}, {"n": "X-Bacon Filé", "p": 25.00, "ing": "Pão, Filé, Queijo, Bacon, Alface e Tomate"}, {"n": "X-Presunto Filé", "p": 22.00, "ing": "Pão, Filé, Queijo, Presunto, Alface e Tomate"}, {"n": "X-Bacon Presunto Filé", "p": 28.00, "ing": "Pão, Filé, Queijo, Bacon, Presunto, Alface e Tomate"}, {"n": "X-Egg Bacon Presunto Filé", "p": 31.00, "ing": "Pão, Filé, Queijo, Ovo, Bacon, Presunto, Alface e Tomate"}],
    TITULO_ABA_6: [{"n": "X-TUDO DO ALAN", "p": 45.00, "ing": "Picanha, Lombo, Filé Frango, Hambúrguer, Queijo, Presunto, Ovo, Bacon, Alface, Tomate, Milho e Batata"}]
}

ADICIONAIS_PAGOS = {"Bife Hambúrguer": 5.0, "Bife Frango": 5.0, "Bife Picanha": 8.0, "Bife Lombo": 6.0, "Filé Frango": 6.0, "Queijo": 3.0, "Presunto": 3.0, "Ovo": 3.0, "Bacon": 5.0, "Catupiry": 5.0}
CORTESIAS = {"Milho": 0.0, "Batata Palha": 0.0}
BEBIDAS = {"Lata": 5.0, "600ml": 8.0, "1 Litro": 10.0, "2 Litros": 15.0}
DOCES = {"Brigadeiro": 4.0, "Beijinho": 4.0, "Doce Amendoim": 3.0}
WHATSAPP_ALAN = "5511999999999"

# =========================================================
# ⚙️ MOTOR DO SITE (LÓGICA DE ETAPAS)
# =========================================================

st.set_page_config(page_title="Trailer do Alan", layout="centered")

# Estilo visual mantido exatamente como o original
st.markdown("""<style>
    .stApp { background-color: #F0F8FF; }
    .stButton>button { background-color: #0077b6; color: white; width: 100%; border-radius: 12px; min-height: 80px; font-weight: bold; font-size: 14px; margin-bottom: 5px; }
    .footer-soma { position: fixed; bottom: 0; left: 0; width: 100%; background: white; padding: 15px; text-align: center; border-top: 3px solid #00b4d8; z-index: 100; font-size: 20px; color: #0077b6; }
    .lanche-box { background: #e1f5fe; padding: 10px; border-radius: 10px; border-left: 5px solid #0077b6; margin-bottom: 10px; }
    </style>""", unsafe_allow_html=True)

st.markdown('<h1 style="text-align:center; color:#0077b6;">🍔 Trailer do Alan</h1>', unsafe_allow_html=True)

# Inicialização de variáveis de controle
if 'pedidos_concluidos' not in st.session_state: st.session_state.pedidos_concluidos = []
if 'lanche_atual_id' not in st.session_state: st.session_state.lanche_atual_id = 1
if 'temp_lanche' not in st.session_state: st.session_state.temp_lanche = {"hamburguer": None, "extras": []}

# Função para travar o lanche atual e pular para o próximo
def finalizar_lanche_atual():
    if st.session_state.temp_lanche["hamburguer"]:
        st.session_state.pedidos_concluidos.append(st.session_state.temp_lanche)
        st.session_state.temp_lanche = {"hamburguer": None, "extras": []}
        st.session_state.lanche_atual_id += 1
        st.success(f"Lanche {st.session_state.lanche_atual_id-1} finalizado! Agora monte o próximo.")
    else:
        st.error("Escolha pelo menos um hambúrguer antes de finalizar!")

tabs = st.tabs(["🍔 Lanches", "➕ Adicionais", "🥤 Bebidas", "🍰 Doces", "🏁 Finalizar"])

# Controle de fluxo: Se chegou ao 7, acabou a vez
if st.session_state.lanche_atual_id <= 6:
    atual = f"Lanche {st.session_state.lanche_atual_id}"
    
    # ABA LANCHES
    with tabs[0]:
        st.info(f"📍 Você está montando agora o: **{atual}**")
        for titulo, lanches in ITENS_CARDAPIO.items():
            with st.expander(f"✨ {titulo}"):
                c1, c2 = st.columns(2)
                for i, l in enumerate(lanches):
                    col = c1 if i % 2 == 0 else c2
                    if col.button(f"{l['n']}\nR$ {l['p']:.2f}", key=f"btn_{titulo}_{i}"):
                        st.session_state.temp_lanche["hamburguer"] = {"n": l['n'], "p": l['p']}
                        st.toast(f"✅ {l['n']} selecionado para o {atual}")

    # ABA ADICIONAIS
    with tabs[1]:
        st.write(f"### ➕ Extras para o **{atual}**")
        c1, c2 = st.columns(2)
        for i, (n, p) in enumerate(ADICIONAIS_PAGOS.items()):
            col = c1 if i % 2 == 0 else c2
            if col.button(f"{n}\n+ R$ {p:.2f}", key=f"add_{i}"):
                st.session_state.temp_lanche["extras"].append({"n": n, "p": p})
                st.toast(f"➕ {n} adicionado")
        
        st.write("---")
        if st.button(f"✅ FINALIZAR {atual} E IR PARA O PRÓXIMO", use_container_width=True):
            finalizar_lanche_atual()

    # ABA BEBIDAS E DOCES (Adicionam ao lanche atual)
    with tabs[2]:
        for n, p in BEBIDAS.items():
            if st.button(f"🥤 {n} - R$ {p:.2f}", key=f"beb_{n}"):
                st.session_state.temp_lanche["extras"].append({"n": f"Bebida {n}", "p": p})
                st.toast(f"🥤 {n} adicionada ao {atual}")

    with tabs[3]:
        for n, p in DOCES.items():
            if st.button(f"🍰 {n} - R$ {p:.2f}", key=f"doce_{n}"):
                st.session_state.temp_lanche["extras"].append({"n": n, "p": p})
                st.toast(f"🍰 {n} adicionado ao {atual}")
else:
    st.warning("⚠️ Limite de 6 lanches atingido. Vá para a aba Finalizar!")

# ABA FINALIZAR
with tabs[4]:
    st.write("### 🧾 Resumo Detalhado por Lanche")
    total_geral = 0.0
    resumo_whats = ""
    
    # Mostra os que já foram fechados
    for idx, p in enumerate(st.session_state.pedidos_concluidos):
        subtotal = p['hamburguer']['p'] + sum(e['p'] for e in p['extras'])
        total_geral += subtotal
        with st.container():
            st.markdown(f"""<div class="lanche-box"><b>🍔 LANCHE {idx+1}: {p['hamburguer']['n']}</b><br>
            {f"".join([f"• {e['n']} (R$ {e['p']:.2f})<br>" for e in p['extras']])}
            <b>Subtotal: R$ {subtotal:.2f}</b></div>""", unsafe_allow_html=True)
            resumo_whats += f"\n*LANCHE {idx+1}: {p['hamburguer']['n']}*\n" + "".join([f"- {e['n']}\n" for e in p['extras']]) + f"*Subtotal: R$ {subtotal:.2f}*\n"

    # Mostra o que está sendo montado agora (se houver)
    if st.session_state.temp_lanche["hamburguer"]:
        st.write("🕒 *Lanche em montagem (ainda não finalizado):*")
        st.write(f"- {st.session_state.temp_lanche['hamburguer']['n']}")

    nome_u = st.text_input("Seu Nome:")
    end_u = st.text_input("Endereço:")
    
    if st.button("🟢 ENVIAR PEDIDO COMPLETO"):
        if nome_u and end_u and total_geral > 0:
            msg = f"*PEDIDO TRAILER DO ALAN*\n*Cliente:* {nome_u}\n*Endereço:* {end_u}\n{resumo_whats}\n*TOTAL GERAL: R$ {total_geral:.2f}*"
            link = f"https://wa.me/{WHATSAPP_ALAN}?text={msg.replace(' ', '%20').replace('\n', '%0A')}"
            st.link_button("Confirmar no WhatsApp ✅", link)

if total_geral > 0:
    st.markdown(f'<div class="footer-soma"><b>🛒 VALOR TOTAL: R$ {total_geral:.2f}</b></div>', unsafe_allow_html=True)
