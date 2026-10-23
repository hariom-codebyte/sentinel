import json
from pathlib import Path

class ThreatIntelligenceEngine:
    def __init__(self, data_file):
        self.data_file = Path(data_file)

    def fetch_raw_data(self):
        """Reads the raw JSON file simulating an API response."""
        if not self.data_file.is_file():
            return {"error": "Data file not found", "status": 404}
            
        with self.data_file.open('r', encoding='utf-8') as file:
            try:
                data = json.load(file)
                return data
            except json.JSONDecodeError:
                return {"error": "Invalid JSON format", "status": 500}

    def get_dashboard_metrics(self):
        """Calculates statistics for the dashboard."""
        data = self.fetch_raw_data()
        if "error" in data:
            return data

        iocs = data.get("iocs", [])
        metrics = {
            "total_threats": len(iocs),
            "critical_count": sum(1 for i in iocs if i.get("severity") == "Critical"),
            "high_count": sum(1 for i in iocs if i.get("severity") == "High"),
            "medium_count": sum(1 for i in iocs if i.get("severity") == "Medium")
        }
        return metrics
