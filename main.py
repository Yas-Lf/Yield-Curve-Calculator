import matplotlib.pyplot as plt
from plot_curves import plot_spot_curve, plot_forward_curve
from general_functions import parse_maturity, generate_payment
from bond_data import Bonds, Prices
# -------------------------


discount_factors = {}
spot_rates = {}

# Sort maturities by years
maturities = sorted(Bonds.keys(), key=lambda x: parse_maturity(x))

# Bootstrapping loop
for maturity in maturities:
    years = parse_maturity(maturity)
    coupon = Bonds[maturity]
    cashflows = generate_payment(years, coupon)
    price = Prices[maturity]

    if years < 1:  # Bill / zero-coupon
        DF = price / cashflows[0]
        r = DF**(-1/years) - 1
        discount_factors[maturity] = DF
        spot_rates[maturity] = r
    else:  # Notes/Bonds 
        PV_earlier = 0
        # Sum PV of all previous cashflows
        for i in range(len(cashflows) - 1):
            t_i = (i + 1) / 2  # semi-annual periods
            DF_i = None
            # Find previous DF corresponding to this period
            # Assume linear search: pick closest shorter maturity
            for m in discount_factors:
                if parse_maturity(m) >= t_i:
                    continue
                DF_i = discount_factors[m]
            if DF_i is None:
                DF_i = 1 / (1 + coupon / 2)**(i+1)  # fallback
            PV_earlier += cashflows[i] * DF_i

        # Last cashflow
        CF_last = cashflows[-1]
        DF_last = (price - PV_earlier) / CF_last
        discount_factors[maturity] = DF_last
        r_last = DF_last**(-1/years) - 1
        spot_rates[maturity] = r_last

# till here the spot rates have been calculated

discount_factors = {}

for maturity, r in spot_rates.items():
    t = parse_maturity(maturity)  # convert "6M" → 0.5, "2Y" → 2 ...
    DF = 1 / (1 + r)**t
    discount_factors[maturity] = DF

# print discount factors
print("\nDiscount Factors:")
for maturity, DF in discount_factors.items():
    print(f"{maturity}: {DF:.6f}")

# Calculate forward rates between consecutive maturities
forward_rates = {}
maturities_sorted = sorted(discount_factors.keys(), key=parse_maturity)

for i in range(len(maturities_sorted)-1):
    t1_name = maturities_sorted[i]
    t2_name = maturities_sorted[i+1]
    
    t1 = parse_maturity(t1_name)
    t2 = parse_maturity(t2_name)
    
    DF1 = discount_factors[t1_name]
    DF2 = discount_factors[t2_name]
    
    f = (DF1 / DF2)**(1 / (t2 - t1)) - 1
    forward_rates[f"{t1_name}→{t2_name}"] = f

# print forward rates  
print("\nForward Rates:")  # <-- blank line before forwards
for f, fr in forward_rates.items():
    print(f"{f}: {fr*100:.2f}%")

# print spot rates
print("\nSpot Rates:")   # <-- blank line before spot rates
for m, r in spot_rates.items():
    print(f"{m}: {r*100:.3f}%")

# plot results
plot_spot_curve(spot_rates, parse_maturity)
plot_forward_curve(forward_rates, parse_maturity, start_years=0.5)