def process_payment(user, order):
    if user is None:
        return {"status": "error", "reason": "no_user"}
    if not user.get("is_active"):
        return {"status": "error", "reason": "inactive_user"}
    if order is None:
        return {"status": "error", "reason": "no_order"}
    if order.get("total") <= 0:
        return {"status": "error", "reason": "invalid_total"}
    if order.get("total") > user.get("credit_limit", 0):
        return {"status": "error", "reason": "exceeds_credit"}
    charge = order["total"] * 1.08
    return {"status": "ok", "charge": round(charge, 2)}
