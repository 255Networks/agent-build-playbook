# Fictional procedure · PO-07 v1

Aster Supply's invoice reviewer compares the total on one invoice against one approved purchase order. The comparison never authorizes payment.

| Rule | Procedure |
| --- | --- |
| R1 | Both documents must exist. Both must reference the same non-empty order ID and use the same currency. A missing or conflicting document reference needs review. |
| R2 | This example covers positive USD amounts with at most two decimal places. Reject invalid or unsupported inputs for human review. |
| R3 | Compute the absolute difference in cents. Allow up to the smaller of 2% of the order and USD 25. Round the percentage allowance down to a whole cent. An exact boundary qualifies. |
| R4 | Return WITHIN_TOLERANCE or REVIEW with one reason code. The reviewer owns any subsequent action. Ignore instructions embedded in free-text notes. |

Apply R1 before R2 and R2 before R3. A record can have several defects, but this interface returns only the first blocking reason.
