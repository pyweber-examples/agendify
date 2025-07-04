# 🤝 Contribuindo para o Agendify

Obrigado por considerar contribuir para o Agendify! Este documento fornece diretrizes para contribuições.

## 📋 Como Contribuir

### 🐛 Reportando Bugs

1. Verifique se o bug já foi reportado nas [Issues](../../issues)
2. Se não encontrar, crie uma nova issue com:
   - Título claro e descritivo
   - Descrição detalhada do problema
   - Passos para reproduzir
   - Comportamento esperado vs atual
   - Screenshots (se aplicável)
   - Informações do ambiente (OS, Python version, etc.)

### 💡 Sugerindo Melhorias

1. Abra uma issue com a tag "enhancement"
2. Descreva claramente a melhoria proposta
3. Explique por que seria útil para o projeto
4. Forneça exemplos de uso, se possível

### 🔧 Contribuindo com Código

#### Configuração do Ambiente

1. **Fork o repositório**
2. **Clone seu fork**:
   ```bash
   git clone https://github.com/seu-usuario/agendify.git
   cd agendify
   ```
3. **Crie um ambiente virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate  # Windows
   ```
4. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

#### Processo de Desenvolvimento

1. **Crie uma branch para sua feature**:
   ```bash
   git checkout -b feature/nome-da-feature
   ```

2. **Faça suas alterações seguindo as convenções**:
   - Use nomes descritivos para variáveis e funções
   - Adicione comentários quando necessário
   - Mantenha o código limpo e organizado
   - Siga o padrão PEP 8 para Python

3. **Teste suas alterações**:
   ```bash
   python main.py
   ```

4. **Commit suas mudanças**:
   ```bash
   git add .
   git commit -m "feat: adiciona nova funcionalidade X"
   ```

5. **Push para sua branch**:
   ```bash
   git push origin feature/nome-da-feature
   ```

6. **Abra um Pull Request**

#### Convenções de Commit

Use o padrão [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` nova funcionalidade
- `fix:` correção de bug
- `docs:` mudanças na documentação
- `style:` formatação, ponto e vírgula, etc
- `refactor:` refatoração de código
- `test:` adição de testes
- `chore:` tarefas de manutenção

### 📝 Padrões de Código

#### Python
- Siga o PEP 8
- Use type hints quando possível
- Docstrings para funções e classes
- Nomes em inglês para código, português para comentários

#### HTML/CSS
- Indentação de 4 espaços
- Classes CSS em kebab-case
- Comentários descritivos

### 🧪 Testes

Embora o projeto ainda não tenha testes automatizados, ao contribuir:
1. Teste manualmente todas as funcionalidades afetadas
2. Verifique se não quebrou funcionalidades existentes
3. Teste em diferentes navegadores (se aplicável)

### 📚 Documentação

- Atualize o README.md se necessário
- Adicione comentários no código para lógicas complexas
- Documente novas APIs ou endpoints

## 🎯 Áreas que Precisam de Ajuda

- [ ] Testes automatizados
- [ ] Melhorias na UI/UX
- [ ] Otimização de performance
- [ ] Documentação adicional
- [ ] Internacionalização (i18n)
- [ ] Acessibilidade (a11y)

## ❓ Dúvidas?

Se tiver dúvidas sobre como contribuir:
1. Abra uma issue com a tag "question"
2. Entre em contato através das issues
3. Consulte a documentação do Pyweber

## 🙏 Reconhecimento

Todos os contribuidores serão reconhecidos no [README](README.md) do projeto.

Obrigado por ajudar a tornar o Agendify melhor! 🚀
