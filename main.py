import pandas as pd
from scrapers.Mercado_Livre import Mercado_Livre


def main():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }


    url = ""

    mercado_livre = Mercado_Livre(category="", url=url, headers=headers, extraction_date="")

    produtos = mercado_livre.extract_data()

    df_produtos = pd.DataFrame(produtos)

    print(df_produtos)

if __name__ == "__main__":
    main()

