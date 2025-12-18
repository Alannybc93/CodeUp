# 🚀 CodeUP - Plataforma de Aprendizado em Programação

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

## 📋 Sobre o Projeto

CodeUP é uma plataforma web para aprendizado de programação construída com Django. Oferece trilhas de aprendizado, exercícios práticos e uma comunidade ativa para estudantes de tecnologia.

### ✨ Funcionalidades

- ✅ **Sistema de usuários** com autenticação personalizada
- 📚 **Trilhas de aprendizado** em diferentes tecnologias
- 💻 **Exercícios práticos** com correção automática
- 🎯 **Progresso monitorado** com dashboards
- 👥 **Comunidade ativa** de estudantes
- 🎨 **Design moderno** com tema escuro e dourado

## 🛠️ Tecnologias

- **Backend:** Django 5.2, Python 3.13
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** SQLite3 (desenvolvimento)
- **Deploy:** Pronto para produção

## 🚀 Como Executar

```bash
# 1. Clone o repositório
git clone https://github.com/Alannybc93/CodeUp.git
cd CodeUp

# 2. Crie um ambiente virtual
python -m venv venv

# 3. Ative o ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 4. Instale as dependências
pip install -r requirements.txt

# 5. Execute as migrações
python manage.py migrate

# 6. Crie um superusuário (opcional)
python manage.py createsuperuser

# 7. Execute o servidor
python manage.py runserver

# 8. Acesse: http://127.0.0.1:8000/