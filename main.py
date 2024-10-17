from scheduler.task_scheduler import TaskScheduler
from utils.logger import setup_logger

if __name__ == "__main__":
    logger = setup_logger()
    logger.info("Starting EasySpeak...")

    scheduler = TaskScheduler()
    scheduler.start()
