import requests
from config.settings import LLM_CONFIG

class ConversationGenerator:
    def __init__(self):
        self.api_key = LLM_CONFIG['API_KEY']
        self.model_name = LLM_CONFIG['MODEL_NAME']

    def generate_scenarios(self, num_scenarios=LLM_CONFIG['NUM_SCENARIOS']):
        # 调用 LLM API 生成对话场景
        url = f"https://api.llm.example.com/generate"
        payload = {
            'model': self.model_name,
            'prompt': 'Generate English learning scenarios.',
            'num_scenarios': num_scenarios
        }
        headers = {'Authorization': f'Bearer {self.api_key}'}

        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()['scenarios']
        else:
            raise Exception('Error generating scenarios')
