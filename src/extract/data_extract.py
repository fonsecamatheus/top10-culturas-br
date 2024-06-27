from typing import Any, Dict, List


class DataExtract:
    def __init__(self, response:List[Dict[str, Any]]) -> None:
        self.response = response

    def extract_values(self) -> List[Dict[str, Any]]:
        return self.response[1:]