from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from utils.Config import Config
import streamlit as st


def analyze_card(card_url):
    credential = AzureKeyCredential(Config.KEY)
    document_client = DocumentIntelligenceClient(Config.ENDPOINT, credential= credential)
    card_info = document_client.begin_analyze_document(
        "prebuilt-creditCard", analyze_request=AnalyzeDocumentRequest(url_source=card_url)
    )
    result = card_info.result()
    st.write(f"card result: {result}")

    for doc in result.documents:
        fields= doc.get('fields', {})

        return {
            "card_name": fields.get('CardHolderName', {}).get('content'),
            "card_number": fields.get('CardNumber', {}).get('content'),
            "expiry_date": fields.get('ExpirationDate', {}).get('content'),
            "payment_network": fields.get('PaymentNetwork', {}).get('content'),
            "card_number": fields.get('CardNumber', {}).get('content'),
        }
    

    
