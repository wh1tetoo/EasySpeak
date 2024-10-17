EMAIL_CONFIG = {
    'SMTP_SERVER': 'smtp.example.com',
    'SMTP_PORT': 587,
    'SENDER_EMAIL': 'your_email@example.com',
    'SENDER_PASSWORD': 'your_password'
}

LLM_CONFIG = {
    'API_KEY': 'your_llm_api_key',
    'MODEL_NAME': 'dark_side_of_moon',
    'NUM_SCENARIOS': 2  # 每次生成的英语学习场景数量
}

SCHEDULER_CONFIG = {
    'INTERVAL_HOURS': 24  # 每天/每小时生成场景的频率
}

REPORT_DIR = 'data/reports/'
