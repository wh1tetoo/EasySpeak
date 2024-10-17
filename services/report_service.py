import os
from datetime import datetime
from config.settings import REPORT_DIR

class ReportService:
    def __init__(self):
        self.report_dir = REPORT_DIR

    def generate_report(self, scenarios):
        report_path = os.path.join(self.report_dir, f"report_{datetime.now().strftime('%Y%m%d')}.txt")
        with open(report_path, 'w') as report_file:
            report_file.write("\n\n".join(scenarios))
        print(f"Report saved to {report_path}")
