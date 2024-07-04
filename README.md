weather_api/
│
├── data/                    # Armazenamento de dados locais, se necessário
├── notebooks/               # Notebooks Jupyter para exploração e análise
├── src/
│   ├── __init__.py
│   ├── api/                 # Endpoints da API
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── stations.py
│   │   └── history.py
│   ├── models/              # Modelos de banco de dados e IA
│   │   ├── __init__.py
│   │   ├── db_models.py     # Modelos de banco de dados
│   │   └── time_series_model.py  # Modelos de IA
│   ├── services/            # Lógica de negócio
│   │   ├── __init__.py
│   │   └── data_scraping.py
│   ├── utils/               # Funções utilitárias
│   │   ├── __init__.py
│   │   ├── helpers.py
│   │   └── selenium_automation_tools.py
│   └── automations/         # Scripts de automação
│       ├── __init__.py
│       └── data_scraping_stations.py
├── tests/                   # Testes unitários e de integração
│   ├── __init__.py
│   └── test_api.py
│
├── .env                     # Variáveis de ambiente
├── .gitignore
├── requirements.txt         # Dependências do projeto
├── README.md
└── main.py                  # Arquivo principal que inicia a aplicação
