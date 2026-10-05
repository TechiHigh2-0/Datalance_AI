import os
from google import genai
from google.genai import types

def get_gemma_response(system_prompt: str, user_prompt: str) -> str:
    """
    Calls the Google AI Studio API using the provided API key.
    Uses gemma-4-26b-a4b-it if available, else standard gemini model.
    """
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable is missing. Please add it to your .env file.")
        
    client = genai.Client(api_key=api_key)
    
    # Try the preferred model first
    preferred_model = "gemma-4-26b-a4b-it"
    fallback_model = "gemma-2-27b-it" # Standard gemma 2
    
    model_to_use = preferred_model
    
    try:
        response = client.models.generate_content(
            model=model_to_use,
            contents=user_prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.2,
            )
        )
    except Exception as e:
        # If model is not found, fallback to the available one
        if "not found" in str(e).lower() or "unsupported" in str(e).lower():
            try:
                response = client.models.generate_content(
                    model=fallback_model,
                    contents=user_prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=system_prompt,
                        temperature=0.2,
                    )
                )
            except Exception as inner_e:
                raise Exception(f"AI Service Error (Fallback Failed): {str(inner_e)}")
        else:
            raise Exception(f"AI Service Error: {str(e)}")
            
    if not response or not response.text:
        raise ValueError("Received empty response from the model.")
        
    return response.text
