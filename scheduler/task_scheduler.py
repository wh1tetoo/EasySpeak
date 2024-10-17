import schedule
import time
from services.scene_service import SceneService
from config.settings import SCHEDULER_CONFIG

class TaskScheduler:
    def __init__(self):
        self.scene_service = SceneService()

    def generate_daily_scenarios(self):
        print("Generating daily scenarios...")
        self.scene_service.generate_and_send_scenarios()

    def start(self):
        schedule.every(SCHEDULER_CONFIG['INTERVAL_HOURS']).hours.do(self.generate_daily_scenarios)

        while True:
            schedule.run_pending()
            time.sleep(1)
