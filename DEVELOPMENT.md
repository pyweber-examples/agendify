# 🛠️ Configuração de Desenvolvimento - Agendify

Este guia ajuda desenvolvedores a configurar o ambiente de desenvolvimento local.

## 📋 Pré-requisitos

- Python 3.10 ou superior
- pip (gerenciador de pacotes Python)
- Git

## 🚀 Configuração Rápida

### 1. Clone o Repositório
```bash
git clone <url-do-repositorio>
cd Agendify
```

### 2. Ambiente Virtual
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. Executar a Aplicação
```bash
python main.py
```

### 5. Acessar a Aplicação
Abra seu navegador e acesse: `http://localhost:5000`

## 🔧 Configurações de Desenvolvimento

### Estrutura de Pastas Recomendada
```
Agendify/
├── venv/                   # Ambiente virtual (não commitado)
├── database/
│   ├── database.py
│   └── tasks.db           # Banco local (não commitado)
├── templates/
├── style/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

### Variáveis de Ambiente (Futuro)
Crie um arquivo `.env` para configurações locais:
```env
DEBUG=True
DATABASE_URL=sqlite:///tasks.db
PORT=5000
```

## 🧪 Testes (Planejado)

```bash
# Executar testes unitários
python -m pytest tests/

# Executar com coverage
python -m pytest --cov=. tests/
```

## 📝 Convenções de Código

### Python
- Seguir PEP 8
- Usar type hints
- Docstrings para funções públicas
- Máximo 88 caracteres por linha

### Commits
- Usar Conventional Commits
- Mensagens em inglês
- Commits pequenos e focados

## 🐛 Debug

### Logs
O Pyweber fornece logs automáticos. Para debug adicional:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Database
Para inspecionar o banco SQLite:
```bash
sqlite3 database/tasks.db
.tables
.schema tasks
SELECT * FROM tasks;
```

## 🚀 Deploy Local

### Modo Desenvolvimento
```bash
python main.py
```

### Modo Produção (Futuro)
```bash
# Com gunicorn (quando disponível)
gunicorn -w 4 -b 0.0.0.0:5000 main:app
```

## 📚 Recursos Úteis

- [Documentação Pyweber](https://pyweber.readthedocs.io/)
- [Manage SQL Docs](https://manage-sql.readthedocs.io/)
- [SQLite Documentation](https://sqlite.org/docs.html)

## ❓ Problemas Comuns

### Erro: Module not found
```bash
pip install -r requirements.txt
```

### Erro: Database locked
```bash
# Feche todas as conexões com o banco
# Reinicie a aplicação
```

### Porta já em uso
```bash
# Mude a porta no main.py ou mate o processo
lsof -ti:5000 | xargs kill -9  # Linux/macOS
```

## 🤝 Contribuindo

Veja [CONTRIBUTING](CONTRIBUTING.md) para diretrizes detalhadas.

---
💡 **Dica**: Use um IDE como VSCode com extensões Python para melhor experiência de desenvolvimento!
