class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def _calculate_total_and_count(self):
        total = sum(self.data)
        count = len(self.data)
        return total, count

    def calculate_total(self):
        total, _ = self._calculate_total_and_count()
        return total

    def calculate_average(self):
        total, count = self._calculate_total_and_count()
        return total / count if count != 0 else 0

    def calculate_minimum(self):
        if not self.data:
            return None
        return min(self.data)

    def calculate_maximum(self):
        if not self.data:
            return None
        return max(self.data)
