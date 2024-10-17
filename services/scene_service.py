from models.conversation_generator import ConversationGenerator
from services.email_service import EmailService

class SceneService:
    def __init__(self):
        self.generator = ConversationGenerator()
        self.email_service = EmailService()

    def generate_and_send_scenarios(self):
        scenarios = self.generator.generate_scenarios()
        body = "\n\n".join(scenarios)
        self.email_service.send_email(
            recipient_email='student@example.com',
            subject='Your Daily English Learning Scenarios',
            body=body
        )
