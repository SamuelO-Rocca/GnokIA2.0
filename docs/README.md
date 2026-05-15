# GnokIA - Assistente Técnico TEAMBOTS

GnokIA é um assistente especializado em tecnologia e na cultura da equipe TEAMBOTS. Ele utiliza uma arquitetura de Provedores (MCP) para gerenciar memória técnica e de sistema, integrando-se a APIs de LLM para geração de respostas naturais e sarcásticas.

## 🚀 Tecnologias Utilizadas
- **Python 3.12+**
- **NumPy**: Para cálculos de similaridade vetorial (Memória do Sistema).
- **Integrado com OpenAI/Gemini API**: Através do módulo `brain_api`.

## 🛠️ Configuração do Ambiente

1. **Crie um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # venv\Scripts\activate  # Windows
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configuração de Variáveis:**
   - Renomeie o arquivo `.env.example` para `.env` e adicione sua chave de API.
   - Verifique as constantes em `src/config/config.py`.

## 📂 Estrutura de Pastas
- `src/mcp/Provider_Tecnology`: Base de conhecimento técnica estática e dinâmica.
- `src/mcp/Provider_System`: Gerenciamento de preferências e contexto de usuário.
- `src/mcp/central`: O "Cérebro" que orquestra a lógica entre entrada do usuário, memória e API.

## 📈 Métricas de Performance
- **Latência de Busca**: O sistema prioriza buscas locais em $O(1)$ ou $O(N)$ antes de realizar chamadas de rede (API), economizando tokens.
- **Token Management**: Controle rigoroso de histórico para evitar estouro de contexto da LLM.

## 🛡️ Segurança
Nunca suba seu arquivo `.env` ou `config.py` (se contiver segredos) para o repositório. O projeto já conta com um `.gitignore` configurado.