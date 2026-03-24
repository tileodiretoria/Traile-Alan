import streamlit as st

# =========================================================
# 🛠️ PAINEL DE CONTROLE (BASE ORIGINAL DO LEO - INTEGRAL)
# =========================================================

TITULO_ABA_1 = "Hambúrguer Simples"
TITULO_ABA_2 = "Hambúrguer de Frango"
TITULO_ABA_3 = "Hambúrguer de Lombo"
TITULO_ABA_4 = "Hambúrguer de Picanha"
TITULO_ABA_5 = "Filé de Frango"
TITULO_ABA_6 = "🔥 X-TUDO"

ITENS_CARDAPIO = {
    TITULO_ABA_1: [{"n": "Hambúrguer", "p": 10.00, "ing": "Pão, Carne, Alface e Tomate"}, {"n": "X-Burger", "p": 15.00, "ing": "Pão, Carne, Queijo, Alface e Tomate"}, {"n": "X-Egg", "p": 18.00, "ing": "Pão, Carne, Queijo, Ovo, Alface e Tomate"}, {"n": "X-Bacon", "p": 20.00, "ing": "Pão, Carne, Queijo, Bacon, Alface e Tomate"}, {"n": "X-Presunto", "p": 17.00, "ing": "Pão, Carne, Queijo, Presunto, Alface e Tomate"}, {"n": "X-Bacon Presunto", "p": 23.00, "ing": "Pão, Carne, Queijo, Bacon, Presunto, Alface e Tomate"}, {"n": "X-Egg Bacon Presunto", "p": 26.00, "ing": "Pão, Carne, Queijo, Ovo, Bacon, Presunto, Alface e Tomate"}],
    TITULO_ABA_2: [{"n": "Hambúrguer Frango", "p": 12.00, "ing": "Pão, Frango, Alface e Tomate"}, {"n": "X-Burger Frango", "p": 17.00, "ing": "Pão, Frango, Queijo, Alface e Tomate"}, {"n": "X-Egg Frango", "p": 20.00, "ing": "Pão, Frango, Queijo, Ovo, Alface e Tomate"}, {"n": "X-Bacon Frango", "p": 22.00, "ing": "Pão, Frango, Queijo, Bacon, Alface e Tomate"}, {"n": "X-Presunto Frango", "p": 19.00, "ing": "Pão, Frango, Queijo, Presunto, Alface e Tomate"}, {"n": "X-Bacon Presunto Frango", "p": 25.00, "ing": "Pão, Frango, Queijo, Bacon, Presunto, Alface e Tomate"}, {"n": "X-Egg Bacon Presunto Frango", "p": 28.00, "ing": "Pão, Frango, Queijo, Ovo, Bacon, Presunto, Alface e Tomate"}],
    TITULO_ABA_3: [{"n": "Hambúrguer Lombo", "p": 14.00, "ing": "Pão, Lombo, Alface e Tomate"}, {"n": "X-Burger Lombo", "p": 19.00, "ing": "Pão, Lombo, Queijo, Alface e Tomate"}, {"n": "X-Egg Lombo", "p": 22.00, "ing": "Pão, Lombo, Queijo, Ovo, Alface e Tomate"}, {"n": "X-Bacon Lombo", "p": 24.00, "ing": "Pão, Lombo, Queijo, Bacon, Alface e Tomate"}, {"n": "X-Presunto Lombo", "p": 21.00, "ing": "Pão, Lombo, Queijo, Presunto, Alface e Tomate"}, {"n": "X-Bacon Presunto Lombo", "p": 27.00, "ing": "Pão, Lombo, Queijo, Bacon, Presunto, Alface e Tomate"}, {"n": "X-Egg Bacon Presunto Lombo", "p": 30.00, "ing": "Pão, Lombo, Queijo, Ovo, Bacon, Presunto, Alface e Tomate"}],
    TITULO_ABA_4: [{"n": "Hambúrguer Picanha", "p": 18.00, "ing": "Pão, Picanha, Alface e Tomate"}, {"n": "X-Burger Picanha", "p": 23.00, "ing": "Pão, Picanha, Queijo, Alface e Tomate"}, {"n": "X-Egg Picanha", "p": 26.00, "ing": "Pão, Picanha, Queijo, Ovo, Alface e Tomate"}, {"n": "X-Bacon Picanha", "p": 28.00, "ing": "Pão, Picanha, Queijo, Bacon, Alface e Tomate"}, {"n": "X-Presunto Picanha", "p": 25.00, "ing": "Pão, Picanha, Queijo, Presunto, Alface e Tomate"}, {"n": "X-Bacon Presunto Picanha", "p": 31.00, "ing": "Pão, Picanha, Queijo, Bacon, Presunto, Alface e Tomate"}, {"n": "X-Egg Bacon Presunto Picanha", "p": 34.00, "ing": "Pão, Picanha, Queijo, Ovo, Bacon, Presunto, Alface e Tomate"}],
    TITULO_ABA_5: [{"n": "Filé de Frango", "p": 15.00, "ing": "Pão, Filé, Alface e Tomate"}, {"n": "X-Burger Filé", "p": 20.00, "ing": "Pão, Filé, Queijo, Alface e Tomate"}, {"n": "X-Egg Filé", "p": 23.00, "ing": "Pão, Filé, Queijo, Ovo, Alface e Tomate"}, {"n": "X-Bacon Filé", "p": 25.00, "ing": "Pão, Filé, Queijo, Bacon, Alface e Tomate"}, {"n": "X-Presunto Filé", "p": 22.00, "ing": "Pão, Filé, Queijo, Presunto, Alface e Tomate"}, {"n": "X-Bacon Presunto Filé", "p": 28.00, "ing": "Pão, Filé, Queijo, Bacon, Presunto, Alface e Tomate"}, {"n": "X-Egg Bacon Presunto Filé", "p": 31.00, "ing": "Pão, Filé, Queijo, Ovo, Bacon, Presunto, Alface e Tomate"}],
    TITULO_ABA_6: [{"n": "X-TUDO DO ALAN", "p": 45.00, "ing": "Picanha, Lombo, Filé Frango, Hambúrguer, Queijo, Presunto, Ovo, Bacon, Alface, Tomate, Milho e Batata"}]
}

ADICIONAIS_PAGOS = {"Bife de Hambúrguer": 5.00, "Bife de Frango": 5.00, "Bife de Picanha": 8.00, "Bife de Lombo": 6.00, "Filé de Frango": 6.00, "Queijo": 3.00, "Presunto": 3.00, "Ovo": 3.00, "Bacon": 5.00, "Catupiry": 5.00}
CORTESIAS = {"Milho": 0.00, "Batata Palha": 0.00}
BEBIDAS = {"Lata": 5.00, "600ml": 8.00, "1 Litro": 10.00, "2 Litros": 15.00}
DOCES = {"Brigadeiro": 4.00, "Beijinho": 4.00, "Doce Amendoim": 3.00}
WHATSAPP_ALAN = "5511999999999"

# =========================================================
# ⚙️ MOTOR DO SITE
# =========================================================

st.set_page_config(page_title="Trailer do Alan", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #F0F8FF; }
    .stButton>button { 
        background-color: #0077b6; color: white; width: 100%; border-radius: 12px; 
        min-height: 120px; font-weight: bold; font-size: 14px; margin-bottom: 10px;
        display: flex; align-items: center; justify-content: center;
    }
    .footer-soma { 
        position: fixed; bottom: 0; left: 0; width: 100%; background: white; 
        padding: 15px; text-align: center; border-top: 3px solid #00b4d8; z-index: 100;
        font-size: 20px; color: #0077b6;
    }
    .resumo-box { background: #e3f2fd; padding: 15px; border-radius: 10px; border-left: 5px solid #0077b6; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 style="text-align:center; color:#0077b6;">🍔 Trailer do Alan</h1>', unsafe_allow_html=True)

if 'lanches_fechados' not in st.session_state: st.session_state.lanches_fechados = []
if 'lanche_atual' not in st.session_state: st.session_state.lanche_atual = {"n": None, "p": 0.0, "extras": []}
if 'id_atual' not in st.session_state: st.session_state.id_atual = 1

tabs = st.tabs(["🍔 Lanches", "➕ Adicionais", "🥤 Bebidas", "🍰 Doces", "🏁 Finalizar"])

# BLOCO DE MONTAGEM (SÓ ATÉ 6)
if st.session_state.id_atual <= 6:
    with tabs[0]:
        st.info(f"📍 Montando agora: **Lanche {st.session_state.id_atual}**")
        for titulo, lanches in ITENS_CARDAPIO.items():
            with st.expander(f"✨ Opções de {titulo}"):
                c1, c2 = st.columns(2)
                for i, l in enumerate(lanches):
                    coluna = c1 if i % 2 == 0 else c2
                    if coluna.button(f"{l['n']}\nR$ {l['p']:.2f}\n({l['ing']})", key=f"btn_{titulo}_{i}"):
                        st.session_state.lanche_atual["n"] = l['n']
                        st.session_state.lanche_atual["p"] = l['p']
                        st.toast(f"Lanche {st.session_state.id_atual} selecionado!")

    with tabs[1]:
        st.write("### ➕ Extras")
        c1, c2 = st.columns(2)
        for i, (nome, preco) in enumerate(ADICIONAIS_PAGOS.items()):
            coluna = c1 if i % 2 == 0 else c2
            if coluna.button(f"{nome}\n+ R$ {preco:.2f}", key=f"extra_pago_{i}"):
                st.session_state.lanche_atual["extras"].append({"n": nome, "p": preco})
                st.toast(f"Adicionado {nome}")

    with tabs[2]:
        for nome, preco in BEBIDAS.items():
            if st.button(f"🥤 {nome} - R$ {preco:.2f}", key=f"beb_{nome}"):
                st.session_state.lanche_atual["extras"].append({"n": f"Bebida {nome}", "p": preco})
                st.toast(f"Bebida {nome} adicionada!")

    with tabs[3]:
        for nome, preco in DOCES.items():
            if st.button(f"🍰 {nome} - R$ {preco:.2f}", key=f"doce_{nome}"):
                st.session_state.lanche_atual["extras"].append({"n": nome, "p": preco})
                st.toast(f"Doce {nome} adicionado!")

# ABA FINALIZAR (O CORAÇÃO DO PEDIDO)
with tabs[4]:
    nome_u = st.text_input("Seu Nome:")
    end_u = st.text_input("Endereço Completo:")
    tel_u = st.text_input("Telefone:")
    
    st.markdown("### 📋 Resumo do seu Pedido")
    total_acumulado = 0.0
    resumo_texto_whatsapp = ""

    # 1. MOSTRA OS LANCHES QUE JÁ FORAM TRAVADOS
    for idx, l in enumerate(st.session_state.lanches_fechados):
        sub = l['p'] + sum(e['p'] for e in l['extras'])
        total_acumulado += sub
        st.markdown(f"""<div class="resumo-box"><b>✅ LANCHE {idx+1}: {l['n']}</b><br>
        {f"".join([f"• {e['n']} (R$ {e['p']:.2f})<br>" for e in l['extras']])}
        <b>Subtotal: R$ {sub:.2f}</b></div>""", unsafe_allow_html=True)
        resumo_texto_whatsapp += f"\n*LANCHE {idx+1}: {l['n']}*\n" + "".join([f"- {e['n']}\n" for e in l['extras']]) + f"*Subtotal: R$ {sub:.2f}*\n"

    # 2. MOSTRA O LANCHE QUE ESTÁ SENDO MONTADO AGORA
    if st.session_state.lanche_atual["n"]:
        l_agora = st.session_state.lanche_atual
        sub_agora = l_agora['p'] + sum(e['p'] for e in l_agora['extras'])
        st.markdown(f"""<div class="resumo-box" style="border-left-color: orange;"><b>⏳ MONTANDO AGORA (Lanche {st.session_state.id_atual}): {l_agora['n']}</b><br>
        {f"".join([f"• {e['n']} (R$ {e['p']:.2f})<br>" for e in l_agora['extras']])}
        <b>Subtotal Parcial: R$ {sub_agora:.2f}</b></div>""", unsafe_allow_html=True)
        
        # BOTÃO PARA FECHAR ESTE LANCHE E PASSAR PRO PRÓXIMO
        if st.button(f"🔒 FINALIZAR LANCHE {st.session_state.id_atual} E MONTAR OUTRO"):
            st.session_state.lanches_fechados.append(st.session_state.lanche_atual.copy())
            st.session_state.lanche_atual = {"n": None, "p": 0.0, "extras": []}
            st.session_state.id_atual += 1
            st.rerun()

    # 3. ENVIO FINAL
    if st.button("🟢 CONCLUIR PEDIDO E ENVIAR WHATSAPP", type="primary"):
        # Se clicar em enviar e ainda tiver um lanche "em aberto" na tela, a gente inclui ele automaticamente
        temp_total = total_acumulado
        temp_resumo = resumo_texto_whatsapp
        if st.session_state.lanche_atual["n"]:
            l_final = st.session_state.lanche_atual
            sub_f = l_final['p'] + sum(e['p'] for e in l_final['extras'])
            temp_total += sub_f
            temp_resumo += f"\n*LANCHE {st.session_state.id_atual}: {l_final['n']}*\n" + "".join([f"- {e['n']}\n" for e in l_final['extras']]) + f"*Subtotal: R$ {sub_f:.2f}*\n"

        if nome_u and end_u and temp_total > 0:
            msg = (f"*PEDIDO TRAILER DO ALAN*\n*Cliente:* {nome_u}\n*Endereço:* {end_u}\n*Tel:* {tel_u}\n\n*ITENS:*{temp_resumo}\n*TOTAL GERAL: R$ {temp_total:.2f}*")
            st.link_button("Confirmar no WhatsApp ✅", f"https://wa.me/{WHATSAPP_ALAN}?text={msg.replace(' ', '%20').replace('\n', '%0A')}")
        else:
            st.warning("Preencha nome, endereço e escolha ao menos um lanche!")

# RODAPÉ COM SOMA TOTAL REAL
valor_no_rodape = total_acumulado + (st.session_state.lanche_atual['p'] + sum(e['p'] for e in st.session_state.lanche_atual['extras']))
if valor_no_rodape > 0:
    st.markdown(f'<div class="footer-soma"><b>🛒 TOTAL DO PEDIDO: R$ {valor_no_rodape:.2f}</b></div>', unsafe_allow_html=True)
