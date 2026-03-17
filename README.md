💵 Automação de Cotação Dólar PTAX (Banco Central) Este projeto automatiza a extração da cotação do Dólar PTAX para fechamentos mensais, consumindo dados diretamente da API de Séries Temporais do Banco Central do Brasil (SGS).

🚀 Motivação Como Analista de Investimentos, a precisão nos dados de fechamento de mês é fundamental. Este script elimina a necessidade de busca manual, garantindo que o valor oficial do último dia útil de cada mês seja extraído e consolidado automaticamente.

🛠️ Tecnologias Python 3.x

Pandas: Manipulação e estruturação dos dados.

Requests: Consumo da API do Banco Central.

Datetime: Lógica para cálculo automático do último dia útil de cada mês.

📊 Como Funciona O script calcula o último dia útil de cada mês para o intervalo de anos definido.

Faz uma requisição à API do BCB para a série 10813 (Dólar PTAX).

Trata exceções (feriados ou indisponibilidade da API).

Exporta um arquivo .xlsx pronto para ser utilizado em relatórios ou no Power BI.

🔒 Segurança e Boas Práticas O script utiliza variáveis para caminhos de diretórios, facilitando a portabilidade. Para uso em produção, recomenda-se o uso de arquivos .env para gerenciar caminhos de rede ou pastas locais.

⚙️ Como Executar Clone o repositório.

Instale as dependências: pip install -r requirements.txt.

Execute o script principal: python extractor_ptax_bcb.py.

---

💵 PTAX Dollar Rate Automation (Central Bank of Brazil) This project automates the extraction of the PTAX Dollar rate for monthly closings, consuming data directly from the Central Bank of Brazil (BCB) Time Series API (SGS).

🚀 Motivation As an Investment Analyst, precision in month-end closing data is essential. This script eliminates the need for manual searches, ensuring that the official value of the last business day of each month is automatically extracted and consolidated.

🛠️ Technologies Python 3.x

Pandas: Data manipulation and structuring.

Requests: Central Bank API consumption.

Datetime: Logic for automatic calculation of the last business day of each month.

📊 How It Works The script calculates the last business day of each month for the defined year range.

It requests the BCB API for series 10813 (PTAX Dollar).

It handles exceptions (holidays or API unavailability).

It exports an .xlsx file ready for use in reports or Power BI.

🔒 Security and Best Practices The script uses variables for directory paths to facilitate portability. For production use, using .env files is recommended to manage network paths or local folders.

⚙️ How to Run Clone the repository.

Install the dependencies: pip install -r requirements.txt.

Run the main script: python extractor_ptax_bcb.py.