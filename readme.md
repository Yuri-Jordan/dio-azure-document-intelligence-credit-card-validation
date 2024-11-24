# Credit Card Information Analysis with Azure AI Document Intelligence

## Overview
This project utilizes Azure AI Document Intelligence to analyze credit card information from scanned documents or images. The goal is to extract relevant data such as card number, expiration date, and cardholder name.

## Prerequisites
Before running the project, ensure you have the following:

- Python
- Azure subscription (for Azure AI Document Intelligence and Blob Storage)
- Required Python packages (listed in requirements.py)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Yuri-Jordan/dio-azure-document-intelligence-credit-card-validation.git
    cd analise-documento-fraude-azureai
2. **Install required packages:**
    ```bash
    pip install -r requirements.txt
## Configuration

1. **Set up Azure AI Document Intelligence:**
    - Create an Azure account and set up a Document Intelligence resource.
    - Obtain your endpoint and API key from the Azure portal.
2. **Set up Azure Blob Storage:**
    - Create an Azure account and set up a Azure Blob Storage resource.
    - Create asd Set up a container in Azure Blob Storage resource.
    - Obtain your storage account name, container name, and the storage connection string.
3. **Rename the .env-example file to .env and add the following:**
    ```python
    container-name = "your-container-name"
    storage-connect-string = "your-storage-account-string"
    storage-acc-name = "your-storage-account-name"
    doc-url = "your-document-intelligence-project-url"
    key = "your-document-intelligence-key"
## Usage

1. **Run the analysis script using streamlit:**
    ```bash
    streamlit run src/app.py
2. **Your app will open in: http://localhost:8501**

## Acknowledgments
- https://www.dio.me
    