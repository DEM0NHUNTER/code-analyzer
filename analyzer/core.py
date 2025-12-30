import ast
from radon.complexity import cc_visit
from src.api.models import FunctionMetric


class CodeAnalyzer:
    @staticmethod
    def analyze_snippet(code: str) -> list[FunctionMetric]:
        """
        Parses the code string, extracts functions, and calculates Cyclomatic Complexity.
        """
        metrics = []

        try:
            # 1. Parse the code using Radon (Calculates complexity "CC")
            # Radon returns a list of blocks. We only want functions/methods.
            blocks = cc_visit(code)

            for block in blocks:
                # We only care about functions (type 'F') or methods (type 'M')
                if hasattr(block, 'name') and hasattr(block, 'complexity'):
                    is_complex = block.complexity > 10

                    metric = FunctionMetric(
                        name=block.name,
                        complexity=block.complexity,
                        line_number=block.lineno,
                        is_complex=is_complex
                    )
                    metrics.append(metric)

        except SyntaxError as e:
            # Senior Move: Don't crash the server if the user sends bad code.
            # We catch the syntax error and return an empty list (or could raise a custom error).
            print(f"Syntax Error parsing snippet: {e}")
            return []

        except Exception as e:
            print(f"Analysis failed: {e}")
            return []

        return metrics