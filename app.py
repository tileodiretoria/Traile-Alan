import streamlit as st

# Configuração da página
st.set_page_config(page_title="Trailer do Alan", page_icon="🍔")

st.title("🍔 Sistema de Pedidos - Trailer do Alan")
st.write("Preencha os dados abaixo para enviar seu pedido direto para o nosso WhatsApp!")

# --- 1. COLETA DE DADOS ---
# Criamos caixas de texto para o cliente digitar
nome = st.text_input("Seu Nome:")
endereco = st.text_input("Endereço de Entrega:")
lanche = st.selectbox("Escolha seu Lanche:", ["X-Burger", "X-Salada", "X-Tudo", "Combo Família"])
observacao = st.text_area("Alguma observação? (Ex: Sem cebola)")

# --- 2. CONFIGURAÇÃO DO ALAN ---
# Substitua pelo número real do Alan. 
# Formato: 55 + DDD + Número (sem espaços ou traços)
numero_whatsapp_alan = "5571992363322" 

# --- 3. A LÓGICA DO ENVIO ---
if st.button("Finalizar Pedido"):
    if nome and endereco: # Verifica se o cliente preencheu o básico
        
        # Aqui montamos o "corpo" da mensagem
        # O \n serve para pular linha na mensagem do WhatsApp
        texto = (
            f"✅ *NOVO PEDIDO* ✅\n\n"
            f"*Cliente:* {nome}\n"
            f"*Lanche:* {lanche}\n"
            f"*Endereço:* {endereco}\n"
            f"*Obs:* {observacao}"
        )
        
        # O link do WhatsApp não aceita espaços vazios, então usamos .replace(" ", "%20")
        # Isso transforma "Oi Alan" em "Oi%20Alan", que a internet entende.
        link_final = f"https://wa.me/{numero_whatsapp_alan}?text={texto.replace(' ', '%20')}"
        
        # Mostramos o botão de confirmação
        st.success("Pedido organizado com sucesso!")
        st.link_button("🚀 ENVIAR PARA O WHATSAPP DO ALAN", link_final)
    else:
        st.error("Ops! Por favor, preencha seu nome e endereço.")
