
def parse_maturity(name):    # e.g., "Bills_6M" → 0.5, "Notes_2Y" → 2
    tag = name.split("_")[1]

    if "M" in tag:  # months
        months = int(tag.replace("M", ""))
        return months / 12

    if "Y" in tag:  # years
        years = int(tag.replace("Y", ""))
        return years

    return 0  


def generate_payment(years, coupon_rate):
    # Bills (zero-coupon)
    if years < 1:
        return [1]  # single payment at maturity

    # Notes/Bonds (semi-annual)
    frequency = 2
    periods = int(years * frequency)  # SAFEST FIX: force integer
    payment_amount = coupon_rate / frequency

    cashflows = []
    for p in range(periods):
        if p == periods - 1:
            cashflows.append(payment_amount + 1)
        else:
            cashflows.append(payment_amount)

    return cashflows