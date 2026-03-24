import streamlit as st

# =========================================================
# 🛠️ CARDÁPIO COMPLETO (BASE ORIGINAL + NOVAS OPÇÕES)
# =========================================================

ITENS_CARDAPIO = {
    "Hambúrguer Simples": [
        {"n": "Hambúrguer", "p": 10.00, "ing": "Pão, Carne, Alface e Tomate"},
        {"n": "X-Burger", "p": 15.00, "ing": "Pão, Carne, Queijo, Alface e Tomate"},
        {"n": "X-Egg", "p": 18.00, "ing": "Pão, Carne, Queijo, Ovo, Alface e Tomate"},
        {"n": "X-Bacon", "p": 20.00, "ing": "Pão, Carne, Queijo, Bacon, Alface e Tomate"},
        {"n": "X-Presunto", "p": 17.00, "ing": "Pão, Carne, Queijo, Presunto, Alface e Tomate"},
        {"n": "X-Bacon Presunto", "p": 23.00, "ing": "Pão, Carne, Queijo, Bacon, Presunto, Alface e Tomate"},
        {"n": "X-Egg Bacon Presunto", "p": 26.00, "ing": "Pão, Carne, Queijo, Ovo, Bacon, Presunto, Alface e Tomate"}
    ],
    "Hambúrguer de Frango": [
        {"n": "Hambúrguer Frango", "p": 12.00, "ing": "Pão, Frango, Alface e Tomate"},
        {"n": "X-Burger Frango", "p": 17.00, "ing": "Pão, Frango, Queijo, Alface e Tomate"},
        {"n": "X-Egg Frango", "p": 20.00, "ing": "Pão, Frango, Queijo, Ovo, Alface e Tomate"},
        {"n": "X-Bacon Frango", "p": 22.00, "ing": "Pão, Frango, Queijo, Bacon, Alface e Tomate"},
        {"n": "X-Presunto Frango", "p": 19.00, "ing": "Pão, Frango, Queijo, Presunto, Alface e Tomate"},
        {"n": "X-Bacon Presunto Frango", "p": 25.00, "ing": "Pão, Frango, Queijo, Bacon, Presunto, Alface e Tomate"},
        {"n": "X-Egg Bacon Presunto Frango", "p": 28.00, "ing": "Pão, Frango, Queijo, Ovo, Bacon, Presunto, Alface e Tomate"}
    ],
    "Hambúrguer de Lombo": [
        {"n": "Hambúrguer Lombo", "p": 14.00, "ing": "Pão, Lombo, Alface e Tomate"},
        {"n": "X-Burger Lombo", "p": 19.00, "ing": "Pão, Lombo, Queijo, Alface e Tomate"},
        {"n": "X-Egg Lombo", "p": 22.00, "ing": "Pão, Lombo, Queijo, Ovo, Alface e Tomate"},
        {"n": "X-Bacon Lombo", "p": 24.00, "ing": "Pão, Lombo, Queijo, Bacon, Alface e Tomate"},
        {"n": "X-Presunto Lombo", "p": 21.00, "ing": "Pão, Lombo, Queijo, Presunto, Alface e Tomate"},
        {"n": "X-Bacon Presunto Lombo", "p": 27.00, "ing": "Pão, Lombo, Queijo, Bacon, Presunto, Alface e Tomate"},
        {"n": "X-Egg Bacon Presunto Lombo", "p": 30.00, "ing": "Pão, Lombo, Queijo, Ovo, Bacon, Presunto, Alface e Tomate"}
    ],
    "Hambúrguer de Picanha": [
        {"n": "Hambúrguer Picanha", "p": 18.00, "ing": "Pão, Picanha, Alface e Tomate"},
        {"n": "X-Burger Picanha", "p": 23.00, "ing": "Pão, Picanha, Queijo, Alface e Tomate"},
        {"n": "X-Egg Picanha", "p": 26.00, "ing": "Pão, Picanha, Queijo, Ovo, Alface e Tomate"},
        {"n": "X-Bacon Picanha", "p": 28.00, "ing": "Pão, Picanha, Queijo, Bacon, Alface e Tomate"},
        {"n": "X-Presunto Picanha", "p": 25.00, "ing": "Pão, Picanha, Queijo, Presunto, Alface e Tomate"},
        {"n": "X-Bacon Presunto Picanha", "p": 31.00, "ing": "Pão, Picanha, Queijo, Bacon, Presunto, Alface e Tomate"},
        {"n": "X-Egg Bacon Presunto Picanha", "p": 34.00, "ing": "Pão, Picanha, Queijo, Ovo, Bacon, Presunto, Alface e Tomate"}
    ],
    "Filé de Frango": [
        {"n": "Filé de Frango", "p": 15.00, "ing": "Pão, Filé, Alface e Tomate"},
        {"n": "X-Burger Filé", "p": 20.00, "ing": "Pão, Filé, Queijo, Alface e Tomate"},
        {"n": "X-Egg Filé", "p": 23.00, "ing": "Pão, Filé, Queijo, Ovo, Alface e Tomate"},
        {"n": "X-Bacon Filé", "p": 25.00, "ing": "Pão, Filé, Queijo, Bacon, Alface e Tomate"},
        {"n": "X-Presunto Filé", "p": 22.00, "ing": "Pão, Filé, Queijo, Presunto, Alface e Tomate"},
        {"n": "X-Bacon Presunto Filé", "p": 28.00, "ing": "Pão, Filé, Queijo, Bacon, Presunto, Alface e Tomate"},
        {"n": "X-Egg Bacon Presunto Filé", "p": 31.00, "ing": "Pão, Filé, Queijo, Ovo, Bacon, Presunto, Alface e Tomate"}
    ],
    "🔥 X-TUDO": [
        {"n": "X-TUDO DO ALAN", "p": 45.00, "ing": "Picanha, Lombo, Filé Frango, Hambúrguer, Queijo, Presunto, Ovo, Bacon, Alface, Tomate, Milho e Batata"}
    ],
    "🥪 Outras Opções": [
        {"n": "Misto Quente", "p": 10.00, "ing": "Pão, Queijo e Presunto"},
        {"n": "Queijo Quente", "p": 8.00, "ing": "Pão e Queijo"}
    ]
}

ADICIONAIS_PAGOS = {"Bife de Hambúrguer": 5.00, "Bife de Frango": 5.00, "Bife de Picanha": 8.00, "Bife de Lombo": 6.00, "Filé de Frango": 6.00, "Queijo": 3.00, "Presunto": 3.00, "Ovo": 3.00, "Bacon": 5.00, "Catupiry": 5.00}
CORTESIAS = {"Milho": 0.00, "Batata Palha": 0.00}

# BEBIDAS COM TEXTO "REFRIGERANTE" NO LUGAR DO EMOJI
BEBIDAS = {"Lata": 5.00, "600ml": 8.00, "1 Litro": 10.00, "2 Litros": 15.00}

DOCES = {"Brigadeiro": 4.00, "Beijinho": 4.00, "Doce Amendoim": 3.00}
WHATSAPP_ALAN = "5571992363322"

# =========================================================
# ⚙️ LÓGICA DO SISTEMA
# =========================================================

st.set_page_config(page_title="Trailer do Alan", layout="wide")

if 'lanches_fechados' not in st.session_state: st.session_state.lanches_fechados = []
if 'lanche_atual' not in st.session_state: st.session_state.lanche_atual = {"n": None, "p": 0.0, "ing": "", "extras": []}
if 'id_atual' not in st.session_state: st.session_state.id_atual = 1

def resetar_tudo():
    st.session_state.lanches_fechados = []
    st.session_state.lanche_atual = {"n": None, "p": 0.0, "ing": "", "extras": []}
    st.session_state.id_atual = 1
    st.rerun()

st.markdown('<h1 style="text-align:center; color:#0077b6;">🍔 Trailer do Alan</h1>', unsafe_allow_html=True)

col_menu, col_visual = st.columns([0.60, 0.40])

with col_menu:
    tabs = st.tabs(["🍔 Lanches", "➕ Adicionais", "🥤 Bebidas", "🍰 Doces", "🏁 Finalizar"])

    if st.session_state.id_atual <= 6:
        with tabs[0]:
            st.info(f"📍 Selecione o Lanche {st.session_state.id_atual}")
            for cat, lanches in ITENS_CARDAPIO.items():
                with st.expander(f"✨ {cat}"):
                    for i, l in enumerate(lanches):
                        if st.button(f"{l['n']} - R$ {l['p']:.2f}\n({l['ing']})", key=f"l_{cat}_{i}"):
                            st.session_state.lanche_atual.update({"n": l['n'], "p": l['p'], "ing": l['ing']})
                            st.rerun()

        with tabs[1]:
            st.write("### ➕ Adicionais (Cobrados)")
            c1, c2 = st.columns(2)
            for i, (n, p) in enumerate(ADICIONAIS_PAGOS.items()):
                col = c1 if i % 2 == 0 else c2
                if col.button(f"{n} (+R$ {p:.2f})", key=f"pago_{i}"):
                    st.session_state.lanche_atual["extras"].append({"n": n, "p": p})
                    st.rerun()
            
            st.markdown("---")
            st.write("### 🍟 Cortesias (Grátis)")
            c3, c4 = st.columns(2)
            for i, (n, p) in enumerate(CORTESIAS.items()):
                col = c3 if i % 2 == 0 else c4
                if col.button(f"{n} (R$ {p:.2f})", key=f"free_{i}"):
                    st.session_state.lanche_atual["extras"].append({"n": n, "p": p})
                    st.rerun()

        with tabs[2]:
            for n, p in BEBIDAS.items():
                # AQUI FOI ALTERADO: REMOVIDO EMOJI E ADICIONADO "REFRIGERANTE"
                if st.button(f"Refrigerante {n} - R$ {p:.2f}", key=f"beb_{n}"):
                    st.session_state.lanche_atual["extras"].append({"n": f"Refrigerante {n}", "p": p})
                    st.rerun()

        with tabs[3]:
            for n, p in DOCES.items():
                if st.button(f"🍰 {n} - R$ {p:.2f}", key=f"doc_{n}"):
                    st.session_state.lanche_atual["extras"].append({"n": n, "p": p})
                    st.rerun()

    with tabs[4]:
        st.subheader("🏁 Finalizar Pedido")
        nome = st.text_input("Seu Nome:")
        tel = st.text_input("Telefone:")
        end = st.text_input("Endereço Completo:")
        obs = st.text_area("Observações:")
        
        pedidos = st.session_state.lanches_fechados + ([st.session_state.lanche_atual] if st.session_state.lanche_atual["n"] else [])
        
        if len(pedidos) > 0 and nome and tel and end:
            msg = f"*PEDIDO TRAILER DO ALAN*\n*Cliente:* {nome}\n*Telefone:* {tel}\n*Endereço:* {end}\n"
            total = 0
            for i, l in enumerate(pedidos):
                sub = l['p'] + sum(e['p'] for e in l['extras'])
                total += sub
                msg += f"\n*Lanche {i+1}: {l['n']}* (R$ {l['p']:.2f})\n" + "".join([f"- {e['n']} (R$ {e['p']:.2f})\n" for e in l['extras']]) + f"*Subtotal: R$ {sub:.2f}*\n"
            msg += f"\n*TOTAL GERAL: R$ {total:.2f}*"
            if obs: msg += f"\n*Observações:* {obs}"
            
            st.link_button("🟢 ENVIAR PARA O WHATSAPP DO ALAN", f"https://wa.me/{WHATSAPP_ALAN}?text={msg.replace(' ', '%20').replace('\n', '%0A')}")
            if st.button("🔄 INICIAR NOVO PEDIDO (LIMPAR SITE)"): resetar_tudo()
        else:
            st.warning("Preencha todos os dados e finalize pelo menos um lanche!")

# =========================================================
# 📋 PAINEL VISUAL (LATERAL)
# =========================================================
with col_visual:
    st.markdown('<div style="background:white; padding:20px; border-radius:15px; border:2px solid #0077b6;">', unsafe_allow_html=True)
    st.subheader("📝 Seu Pedido Atual")
    
    for idx, l in enumerate(st.session_state.lanches_fechados):
        sub = l['p'] + sum(e['p'] for e in l['extras'])
        st.success(f"**✅ LANCHE {idx+1}: {l['n']}** (R$ {l['p']:.2f})\n\n" + "".join([f"• {e['n']} (R$ {e['p']:.2f})  \n" for e in l['extras']]) + f"**Total Lanche: R$ {sub:.2f}**")

    if st.session_state.id_atual <= 6:
        st.markdown(f"### 🍔 Lanche {st.session_state.id_atual}")
        if st.session_state.lanche_atual["n"]:
            l_at = st.session_state.lanche_atual
            st.info(f"**Item Base:** {l_at['n']} (R$ {l_at['p']:.2f})")
            sub_p = l_at['p']
            for i, e in enumerate(l_at["extras"]):
                c1, c2 = st.columns([0.8, 0.2])
                c1.write(f"• {e['n']} (R$ {e['p']:.2f})")
                sub_p += e['p']
                if c2.button("🗑️", key=f"del_{i}"):
                    st.session_state.lanche_atual["extras"].pop(i)
                    st.rerun()
            st.write(f"**Total Parcial: R$ {sub_p:.2f}**")
            if st.button(f"🔒 FINALIZAR LANCHE {st.session_state.id_atual} E MONTAR OUTRO", use_container_width=True):
                st.session_state.lanches_fechados.append(st.session_state.lanche_atual.copy())
                st.session_state.lanche_atual = {"n": None, "p": 0.0, "ing": "", "extras": []}
                st.session_state.id_atual += 1
                st.rerun()
        else:
            st.warning("Escolha um lanche na aba ao lado.")
    st.markdown('</div>', unsafe_allow_html=True)

# RODAPÉ COM TOTAL GERAL
total_geral = sum([l['p'] + sum(e['p'] for e in l['extras']) for l in st.session_state.lanches_fechados])
if st.session_state.lanche_atual['n']:
    total_geral += st.session_state.lanche_atual['p'] + sum(e['p'] for e in st.session_state.lanche_atual['extras'])
st.markdown(f'<div style="position:fixed; bottom:0; left:0; width:100%; background:white; padding:10px; text-align:center; border-top:2px solid #0077b6; z-index:100;"><b>VALOR TOTAL DO PEDIDO: R$ {total_geral:.2f}</b></div>', unsafe_allow_html=True)
