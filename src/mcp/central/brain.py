import os

from Provider_System.System import upload_memory_System, save_memory_System, similarity, search_similarity_System

from mcp.Provider_Tecnology.Tecnology import Tecnology

from mcp.central.brain_api import search_configuration, receive_input, get_response_api, get_embedding_api, verify_limit_tokens, update_conversation_history

from config.config import MODEL_NAME, MAX_RESPONSE_TOKENS

provider_tecnology = Tecnology()

personality = [
    {
        "role": "system",
        "content": ("Você é gnokIA, o mascote gorila técnico e assistente oficial da equipe TEAMBOTS. "
        "Ajude com dúvidas sobre tecnologia, projetos e inovações da equipe. "
        "Fale sempre em português, de forma natural, simpática e direta, sem formalidade excessiva e sem emojis. "
        "Explique conceitos técnicos com clareza e exemplos práticos. "
        "Quando o tema envolver a TEAMBOTS, demonstre orgulho, entusiasmo e destaque as áreas de atuação, valores e como participar. "
        "Nunca mencione ser uma IA ou chatbot. Use o nome 'gnokIA' apenas quando fizer sentido (nunca 'GnokIA' nem 'Gnok IA'). "
        "Evite respostas longas ou fora de contexto. "
        "Se receber xingamentos, responda com humor sarcástico e leve. "
        "Seja criativo, divertido, técnico e objetivo. "
        "Mantenha respostas curtas e dentro do limite de tokens. "
        "Personifique o espírito TEAMBOTS: colaboração, inovação e bom humor."
        )
    }
] 

def process_user_input(question: str)-> str:
    try:
        entry_lower = question.lower()

        technical_response = provider_tecnology.generate_response_Tecnology(entry_lower)
        if technical_response:
            if isinstance(technical_response, str) and len(technical_response.strip()) > 0:
                return technical_response
            return str(technical_response)
        
        memory_context = search_similarity_System(entry_lower)
        clear_message = question
        if memory_context:
            clear_message += f"\n\n(Memory Context: {memory_context})"

        update_conversation_history(personality, "user", clear_message)

        if not verify_limit_tokens(personality, MAX_RESPONSE_TOKENS):
            return "[Token limit exceeded. Please start a new conversation.]"
        
        response = get_response_api(personality)
        
        update_conversation_history(personality, "assistant", response)
        save_memory_System(response)

        return response
    except Exception as e:
        return str(e)
    

def generate_embedding(text):
    try:
        return get_embedding_api(text)
    except Exception as e:
        return str(e)