import pytest
from scrapers.Mercado_Livre import Mercado_Livre  # Supondo que a classe esteja em um arquivo chamado Mercado_Livre.py

@pytest.fixture
def mercado_livre():
    # Dados fictícios para criar a instância da classe
    url = 'https://www.mercadolivre.com.br/categoria-exemplo'
    headers = {'User-Agent': 'Mozilla/5.0'}
    extraction_date = '2025-02-07'
    category = 'Categoria Exemplo'
    
    # Criando a instância da classe Mercado_Livre
    return Mercado_Livre(category=category, url=url, headers=headers, extraction_date=extraction_date)

def test_initialization(mercado_livre):
    # Verificando se a instância foi criada corretamente
    assert mercado_livre.get_category() == 'Categoria Exemplo'
    assert mercado_livre.get_url() == 'https://www.mercadolivre.com.br/categoria-exemplo'
    assert mercado_livre.get_extraction_date() == '2025-02-07'
    assert mercado_livre.get_headers() == {'User-Agent': 'Mozilla/5.0'}
