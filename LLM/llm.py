from meta_ai_api import MetaAI
gen = MetaAI()

def generate_commands(knowledge, prompt):
  instruction = "Generate a clear, concise sequence of commands that completes the task in the prompt, following the format precisely."

  format = "Provide only the command sequence, with no extra text, comments, or explanations. Encapsulate all commands within $$[ command block ]$$."

  formatted_message = f'Knowledge: {knowledge} \n\n Format: {format} \n\n Prompt: {prompt} \n\n Instructions: {instruction}'

  try:
    response = gen.prompt(message=formatted_message)
    print(response.get("message", "Error: No message found in response"))
    return response.get("message", "No message")
  except Exception as e:
    print(f"API call failed: {e}")
    return None

