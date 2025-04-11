def compute_fuzzy_modifier(description: str) -> float:
    if not description:
        return 1.0
    description = description.lower()
    modifier = 1.0
    high_keywords = ["catastrophic", "extensive", "severe", "devastating", "critical", "massive", "uncontrolled", "explosive", "dire", "unprecedented", "destructive"]
    low_keywords = ["minor", "small", "limited", "contained", "mild", "insignificant", "minimal", "localized"]
    for word in high_keywords:
        if word in description:
            modifier += 0.2
    for word in low_keywords:
        if word in description:
            modifier -= 0.1
    return max(0.8, modifier)
