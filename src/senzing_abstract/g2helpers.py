"""
TODO: g2helpers.py
"""

import inspect

# -----------------------------------------------------------------------------
# Help
# -----------------------------------------------------------------------------


def construct_help(self, method_name: str = "") -> str:
    result: str = ""
    if method_name == "":
        class_name = self.__class__.__name__
        methods = inspect.getmembers(self, predicate=inspect.ismethod)
        for method in methods:
            method_name = method[0]
            if not method_name.startswith(("_")):
                method_comment = inspect.getdoc(getattr(self, method_name))
                if method_comment is not None:
                    lines = method_comment.split("\n")
                    method_overview = lines[0].strip()
                    result = f"{result}\n{method_name} - {method_overview}"
        result = f"{result}\n\nFor method details, use {class_name}.help('method_name')"
    else:
        method_comment = inspect.getdoc(getattr(self, method_name))
        if method_comment is not None:
            lines = method_comment.split("\n")
            for line in lines:
                line_stripped = line.strip()
                if not line_stripped.startswith(("..", ":", "**")):
                    result = f"{result}\n{line}"
    return result
