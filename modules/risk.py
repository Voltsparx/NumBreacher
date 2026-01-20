def calculate_risk(is_voip, carrier):
    score = 0

    if is_voip:
        score += 50
    if carrier == "Unknown":
        score += 30

    if score >= 70:
        return "High"
    elif score >= 40:
        return "Medium"
    else:
        return "Low"
