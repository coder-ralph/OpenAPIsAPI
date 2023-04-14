import openai 

openai.api_key = 'your api key here'

def get_response(prompt): 
  model_engine = "text-davinci-002" 
  prompt = (f"{prompt}") 
   
  completions = openai.Completion.create( 
      engine=model_engine, 
      prompt=prompt, 
      max_tokens=2048, 
      n=1, 
      stop=None, 
      temperature=0.5, 
  ) 
  message = completions.choices[0].text 
  return message.strip() 

response = get_response("Write a Hello World program in Python.") 
print(response) 