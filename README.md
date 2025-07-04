# 📋 Agendify - Task Manager

Um sistema de gerenciamento de tarefas moderno e intuitivo desenvolvido com **Pyweber**, oferecendo uma interface web elegante para organizar e acompanhar suas atividades.

## 🚀 Funcionalidades

- ✅ **Criação de Tarefas**: Adicione novas tarefas com título, descrição, email e status
- 🔍 **Filtragem Inteligente**: Filtre tarefas por status (Pendente/Enviado/Todas)
- ✏️ **Edição em Tempo Real**: Edite tarefas existentes através de modal interativo
- 🗑️ **Exclusão Rápida**: Remova tarefas desnecessárias com um clique
- 📧 **Integração de Email**: Links diretos para contato via email
- 🎨 **Interface Responsiva**: Design moderno e adaptável a diferentes dispositivos
- 💾 **Persistência de Dados**: Armazenamento local com SQLite

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python com Pyweber Framework
- **Frontend**: HTML5, CSS3, JavaScript (via Pyweber)
- **Banco de Dados**: SQLite com manage_sql
- **Estilização**: CSS customizado com Bootstrap Icons
- **Arquitetura**: MVC (Model-View-Controller)

## 📁 Estrutura do Projeto

```
Agendify/
├── 📄 main.py              # Aplicação principal e rotas
├── 📁 database/
│   ├── 📄 database.py      # Classe de gerenciamento do banco
│   └── 📄 tasks.db         # Banco de dados SQLite
├── 📁 templates/
│   └── 📄 index.html       # Template principal da aplicação
└── 📁 style/
    └── 📄 styles.css       # Estilos customizados
```

## 🔧 Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

- Python 3.10+
- Pyweber Framework
- manage_sql (para gerenciamento SQLite)

## 📦 Instalação

1. **Clone o repositório**:
```bash
git clone <url-do-repositorio>
cd Agendify
```

2. **Instale as dependências**:
```bash
pip install pyweber manage_sql
```

3. **Execute a aplicação**:
```bash
python main.py
```

4. **Acesse no navegador**:
```
http://localhost:5000
```

## 🎯 Como Usar

### Criando uma Nova Tarefa
1. Preencha o formulário "Nova Tarefa"
2. Adicione título, descrição, email e status
3. Clique em "Criar Tarefa"

### Filtrando Tarefas
- Use o dropdown "Status" para filtrar por:
  - **Todas**: Exibe todas as tarefas
  - **Pendente**: Apenas tarefas pendentes
  - **Enviado**: Apenas tarefas enviadas

### Editando Tarefas
1. Clique no botão "Editar" na tarefa desejada
2. Modifique os campos no modal
3. Clique em "Salvar" para confirmar

### Excluindo Tarefas
- Clique no botão "Apagar" na tarefa que deseja remover

## 🏗️ Arquitetura

### Backend (main.py)
- **TaskCard**: Componente reutilizável para exibição de tarefas
- **Home**: Template principal com lógica de interação
- **API Routes**: Endpoints RESTful para CRUD de tarefas

### Database (database.py)
- **Database Class**: Abstração para operações SQLite
- **CRUD Operations**: Create, Read, Update, Delete
- **Filtros**: Busca por status e ID

### Frontend
- **Responsive Design**: Interface adaptável
- **Modal System**: Edição inline de tarefas
- **Real-time Updates**: Atualizações dinâmicas sem reload

## 🔌 API Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/` | Página principal |
| `POST` | `/api/task` | Criar nova tarefa |
| `GET` | `/api/tasks` | Listar todas as tarefas |
| `GET` | `/api/tasks/{id}` | Buscar tarefa por ID |
| `PUT` | `/api/tasks/{id}` | Atualizar tarefa |

## 📊 Modelo de Dados

```python
Task {
    id: int (auto-increment)
    title: str
    description: str
    datetime: datetime
    email: str
    status: str ('pending' | 'sent')
}
```

## 🎨 Características do Design

- **Gradientes Modernos**: Header com gradiente atrativo
- **Cards Interativos**: Tarefas organizadas em cards responsivos
- **Badges de Status**: Indicadores visuais coloridos
- **Animações Suaves**: Transições CSS para melhor UX
- **Ícones Bootstrap**: Iconografia profissional

## 🚀 Melhorias Futuras

- [ ] Autenticação de usuários
- [ ] Notificações por email
- [ ] Categorização de tarefas
- [ ] Dashboard com estatísticas
- [ ] Exportação de dados
- [ ] API REST completa
- [ ] Testes automatizados
- [ ] Deploy em nuvem

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

Desenvolvido com ❤️ usando Pyweber Framework

---

⭐ **Se este projeto foi útil para você, considere dar uma estrela!**
