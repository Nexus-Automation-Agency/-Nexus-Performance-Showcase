# core/auditor.py

class NexusPerformanceAuditor:
    def __init__(self, module_name):
        self.module_name = module_name

    def evaluate(self, speed, stability, error_rate):
        score = (speed * 0.4) + (stability * 0.4) - (error_rate * 0.2)

        if score < 50:
            return {
                "module": self.module_name,
                "status": "ALERT",
                "score": score
            }

        return {
            "module": self.module_name,
            "status": "OPTIMAL",
            "score": score
  }
