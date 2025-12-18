# Documentação do Sistema CodeUp

## Estrutura do Projeto

### Apps Django:
1. **usuarios** - Sistema de autenticação e perfis
2. **core** - Funcionalidades centrais
3. **exercicios** - Sistema de exercícios
4. **trilhas** - Caminhos de aprendizado
5. **gamificacao** - XP, níveis, conquistas
6. **comunidades** - Fóruns e discussões
7. **estatisticas** - Análise de progresso

## Configuração de Desenvolvimento

1. Clone o repositório
2. Crie virtual environment: python -m venv venv
3. Ative: .\venv\Scripts\Activate (Windows)
4. Instale dependências: pip install -r requirements.txt
5. Migrações: python manage.py migrate
6. Servidor: python manage.py runserver

## Padrões de Commit

- feat: Nova funcionalidade
- fix: Correção de bug
- docs: Documentação
- style: Formatação
- refactor: Refatoração
- test: Testes

