def generate_nudge_context(
    risk_label: str,
    behavior_label: str,
    strategy: str
):
    nudges = []

    # Risk-based nudges
    if risk_label == "High Risk":
        nudges.append("Focus on stabilizing cash flow before increasing repayments.")
    elif risk_label == "Medium Risk":
        nudges.append("Small improvements in spending control can reduce your risk.")
    else:
        nudges.append("Maintain your current habits to keep risk low.")

    # Behavior-based nudges
    if behavior_label == "Impulsive Spender":
        nudges.append("Try a 24-hour pause before non-essential purchases.")
    else:
        nudges.append("Your saving discipline is a strong financial asset.")

    # Strategy-based nudges
    if "Avalanche" in strategy:
        nudges.append("Prioritize high-interest debts to reduce long-term cost.")
    elif "Snowball" in strategy:
        nudges.append("Clearing smaller debts can build repayment momentum.")
    else:
        nudges.append("Reducing expenses will unlock future repayment options.")

    return nudges
