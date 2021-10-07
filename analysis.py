from typing import Any, Dict, List

import oseti


class Analyzer:
    def __init__(self) -> None:
        self.analyzer = oseti.Analyzer()

    def _format_sentence(self, sentence: Dict[str, Any]) -> Dict[str, Any]:
        return dict(
            positive=sentence["positive"],
            negative=[token.replace("-NEGATION", "") for token in sentence["negative"]],
            score=sentence["score"],
        )

    def analyze(self, blob: str) -> List[Dict[str, Any]]:
        sentences = self.analyzer.analyze_detail(blob)
        analyzed_list = [self._format_sentence(sentence) for sentence in sentences]
        return analyzed_list
