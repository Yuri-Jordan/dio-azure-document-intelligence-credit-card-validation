import streamlit as st
from services.blob_service import upload_blob
from services.card_service import analyze_card


def configure_interface():
    st.title("Upload arquivo - DIO - fake docs")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        fileName = uploaded_file.name

        try:
            blob_url = upload_blob(uploaded_file, fileName)
            card_info = analyze_card(blob_url)
            st.write(f"Arquivo {fileName} enviado com sucesso para o Azure blob storage!")
            show_image_validation(blob_url=blob_url, card_info=card_info)
        except:
            st.write(f"Erro ao enviar arquivo {fileName} para o Azure blob storage!")

def show_image_validation(blob_url, card_info):
    st.image(blob_url, caption="Arquivo enviado", use_container_width=True)
    st.write(f"Resultado da validação:")
    if card_info and card_info["card_name"]:
        st.html(f"<h1 style='color: green;'>Cartão Válido</h1>")
        st.write(f"Titular: {card_info['card_name']}")
        st.write(f"Número: {card_info['card_number']}")
        st.write(f"Emissor: {card_info['payment_network']}")
        st.write(f"Validade: {card_info['expiry_date']}")
    else:
        st.html(f"<h1 style='color: red;'>Cartão Inválido</h1>")

if __name__ == "__main__":
    configure_interface()