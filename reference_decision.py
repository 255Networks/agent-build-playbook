"""Deterministic evaluator for fictional procedure PO-07."""
import re

MONEY = re.compile(r"[0-9]{1,12}(?:\.[0-9]{1,2})?\Z")


def cents(value):
    if not isinstance(value, str) or not MONEY.fullmatch(value):
        return None
    whole, _, fraction = value.partition(".")
    result = int(whole) * 100 + int(fraction.ljust(2, "0"))
    return result if result > 0 else None


def decide(record):
    def review(reason):
        return {"decision": "REVIEW", "reason": reason}

    order, invoice = record.get("order"), record.get("invoice")
    if not isinstance(order, dict) or not isinstance(invoice, dict):
        return review("MISSING_RECORD")
    if not order.get("id") or order["id"] != invoice.get("order_id"):
        return review("ORDER_MISMATCH")
    if order.get("currency") != invoice.get("currency"):
        return review("CURRENCY_MISMATCH")
    if order.get("currency") != "USD":
        return review("UNSUPPORTED_CURRENCY")
    approved, claimed = cents(order.get("total")), cents(invoice.get("total"))
    if approved is None or claimed is None:
        return review("INVALID_AMOUNT")
    tolerance = min(approved * 2 // 100, 2500)
    if abs(approved - claimed) > tolerance:
        return review("VARIANCE_EXCEEDED")
    return {"decision": "WITHIN_TOLERANCE", "reason": "IN_RANGE"}
