def optimize_debt(
    income: float,
    expenses: float,
    total_debt: float,
    risk_label: str
):
    surplus = income - expenses

    if surplus <= 0:
        return {
            "strategy": "Stabilization",
            "monthly_target": 0,
            "reason": "Expenses exceed or equal income. Focus on reducing expenses first."
        }

    # High risk users → conservative approach
    if risk_label == "High Risk":
        target = 0.2 * surplus
        return {
            "strategy": "Snowball (Conservative)",
            "monthly_target": round(target, 2),
            "reason": "High risk detected. Conservative repayment to avoid cash flow stress."
        }

    # Very high debt burden
    if total_debt > income * 36:  # ~3x annual income
        target = 0.3 * surplus
        return {
            "strategy": "Avalanche",
            "monthly_target": round(target, 2),
            "reason": "High debt burden. Prioritize high-interest debts to minimize long-term cost."
        }

    # Default case
    target = 0.3 * surplus
    return {
        "strategy": "Snowball",
        "monthly_target": round(target, 2),
        "reason": "Moderate debt and healthy surplus. Snowball improves motivation and consistency."
    }
