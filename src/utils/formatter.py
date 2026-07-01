import re

def format_smart_list(text: str) -> str:
    """
    SMART LIST AUTO-FORMATTER:
    - Single Item Strip: If only 1 line exists, strip leading bullet/number.
    - Multi-line: Always convert to sequential numeric numbering (`1. `, `2. `), stripping any existing `-`, `*`, or numbers.
    """
    if not text:
        return ""
        
    lines = [line.strip() for line in text.strip().split('\n')]
    lines = [line for line in lines if line]
    
    if not lines:
        return ""
        
    # Single Item Strip
    if len(lines) == 1:
        return re.sub(r'^(\d+\.|-|•|\*)\s*', '', lines[0])
        
    # Multi-line: Strip any existing bullet/number and apply sequential numbering
    result = []
    for i, line in enumerate(lines):
        clean_line = re.sub(r'^(\d+\.|-|•|\*)\s*', '', line)
        result.append(f"{i+1}. {clean_line}")
        
    return '\n'.join(result)
