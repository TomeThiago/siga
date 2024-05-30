# Nome do Projeto

Descrição breve do projeto. 

## Requisitos

- Python 3.8+
- Django 3.2+
- Virtualenv

## Instalação

### 1. Clonar o repositório

```bash
  git clone https://github.com/tomethiago/siga.git

  cd siga
```

### 2. Criar e ativar um ambiente virtual

```bash	
  python -m venv venv

  source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instalar as dependências

```bash	
  pip install -r requirements.txt
```

### 4. Configurar o arquivo .env

```bash	
  DEBUG=True
  SECRET_KEY=your_secret_key
  DB_NAME=your_db_name
  DB_USER=your_db_user
  DB_PASSWORD=your_db_password
  DB_HOST=your_db_host
  DB_PORT=your_db_port
```

### 5. Aplicar as migrações
```bash	
  python manage.py migrate
```

### 6. Criar um superusuário
```bash	
  python manage.py createsuperuser
```

### 7. Iniciar o servidor de desenvolvimento
```bash	
  python manage.py runserver
```

Acesse o projeto em http://localhost:8000.

## Estrutura do Projeto

```plaintext
seu-projeto/
├── manage.py
├── seu_projeto/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── app1/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── static/
│   └── css/
│       └── styles.css
└── templates/
    └── base.html
```

## Licença
Distribuído sob a licença MIT. Veja LICENSE para mais informações.