import os

from google import genai
from config.config import MODEL_NAME, OPENAI_API_KEY, OPENAI_API_BASE, EMBEDDING_DEPLOYMENT_NAME, LIMIT_TOKENS, MAX_RESPONSE_TOKENS
from logs.usege_log import use_register, register_error

client = genai.Client(
    api_key= OPENAI_API_KEY,
    base_url= OPENAI_API_BASE
)

def search_configuration():
    return {
        "model": MODEL_NAME,
        "embedding_model": EMBEDDING_DEPLOYMENT_NAME,
        "limit_tokens": LIMIT_TOKENS,
        "max_response_tokens": MAX_RESPONSE_TOKENS
    }

def receive_input(user_input):
    return user_input.strip()

def get_response_api(conversation_history):
    try:
        response = client.chat.completions.create(
            model = MODEL_NAME,
            messages = conversation_history,
            max_tokens = MAX_RESPONSE_TOKENS
        )
        response_text = response.choices[0].message.content.strip()
        return response_text
    except Exception as e:
        register_error(str(e))
        return "Error to generate response, please try again later."

def get_embedding_api(text):
    try:
        embedding_response = client.embeddings.create(
            model= EMBEDDING_DEPLOYMENT_NAME,
            input= text
        )
        return embedding_response.data[0].embedding
    except Exception as e:
        register_error(str(e))
        return "error to getting embedding, please try again later."
    
def verify_limit_tokens(conversation_history, TOKEN_LIMIT):
    total_tokens_used = sum(len(message['content'].split()) for message in conversation_history)
    return total_tokens_used >= TOKEN_LIMIT

def update_conversation_history(conversation_history, role, content):
    conversation_history.append({"role": role, "content": content})
    return conversation_history