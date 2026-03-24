# DEFINIÇÃO DAS CATEGORIAS
    # Ajustado para que a primeira categoria (Carne) siga a nomenclatura limpa
    categorias = [
        {"nome": "Hambúrguer Simples", "tipo": "Carne", "pb": 10}, 
        {"nome": "Hambúrguer de Frango", "tipo": "Hambúrguer de Frango", "pb": 12},
        {"nome": "Hambúrguer de Lombo", "tipo": "Lombo", "pb": 14},
        {"nome": "Hambúrguer de Picanha", "tipo": "Picanha", "pb": 18},
        {"nome": "Filé de Frango", "tipo": "Filé de Frango", "pb": 15},
    ]

    for cat in categorias:
        with st.expander(f"✨ Opções de {cat['nome']}"):
            tipo = cat['tipo']
            pb = cat['pb']
            col1, col2 = st.columns(2)
            
            # Lógica para Carne (Hambúrguer Simples) ter nomes limpos nos botões
            if tipo == "Carne":
                lanches = [
                    {"n": "Hambúrguer", "p": pb, "ing": "Pão, Carne, Alface e Tomate"},
                    {"n": "X-Burger", "p": pb+5, "ing": "Pão, Carne, Queijo, Alface e Tomate"},
                    {"n": "X-Egg", "p": pb+8, "ing": "Pão, Carne, Queijo, Ovo, Alface e Tomate"},
                    {"n": "X-Bacon", "p": pb+10, "ing": "Pão, Carne, Queijo, Bacon, Alface e Tomate"},
                    {"n": "X-Presunto", "p": pb+7, "ing": "Pão, Carne, Queijo, Presunto, Alface e Tomate"},
                    {"n": "X-Bacon Presunto", "p": pb+13, "ing": "Pão, Carne, Queijo, Bacon, Presunto, Alface e Tomate"},
                    {"n": "X-Egg Bacon Presunto", "p": pb+16, "ing": "Pão, Carne, Queijo, Ovo, Bacon, Presunto, Alface e Tomate"}
                ]
            else:
                # Mantém o padrão anterior para as outras carnes (Frango, Lombo, etc)
                lanches = [
                    {"n": f"{tipo}", "p": pb, "ing": f"Pão, {tipo}, Alface e Tomate"},
                    {"n": f"X-Burger {tipo}", "p": pb+5, "ing": f"Pão, {tipo}, Queijo, Alface e Tomate"},
                    {"n": f"X-Egg {tipo}", "p": pb+8, "ing": f"Pão, {tipo}, Queijo, Ovo, Alface e Tomate"},
                    {"n": f"X-Bacon {tipo}", "p": pb+10, "ing": f"Pão, {tipo}, Queijo, Bacon, Alface e Tomate"},
                    {"n": f"X-Presunto {tipo}", "p": pb+7, "ing": f"Pão, {tipo}, Queijo, Presunto, Alface e Tomate"},
                    {"n": f"X-Bacon Presunto {tipo}", "p": pb+13, "ing": f"Pão, {tipo}, Queijo, Bacon, Presunto, Alface e Tomate"},
                    {"n": f"X-Egg Bacon Presunto {tipo}", "p": pb+16, "ing": f"Pão, {tipo}, Queijo, Ovo, Bacon, Presunto, Alface e Tomate"}
                ]

            for i, l in enumerate(lanches):
                col_target = col1 if i % 2 == 0 else col2
                btn_label = f"{l['n']}\nR$ {l['p']:.2f}\n({l['ing']})"
                if col_target.button(btn_label, key=f"btn_{l['n']}_{cat['nome']}"):
                    adicionar(l['n'], l['p'], l['ing'])
