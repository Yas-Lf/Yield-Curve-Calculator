# Yield Curve Bootstrapping Project

This project builds a U.S. Treasury **yield curve** using clean and modular Python code. It uses bond prices and coupon data to calculate discount factors, spot rates, and forward rates through a standard bootstrapping method.

The project is organized into four simple modules:

* **main.py**
  This is the main script. It loads the bond data, generates the cash flows, performs the bootstrapping, calculates forward rates, and prints the final results.

* **general_functions.py**
  Contains small helper functions:

  * `parse_maturity`: converts labels like `"Bills_6M"` or `"Notes_2Y"` into time in years
  * `generate_cashflow`: creates the list of cash flows for bills and coupon-paying bonds

* **plot_curves.py**
  Contains the two plotting functions:

  * one for the **spot rate curve**
  * one for the **forward rate curve**
    These functions keep the visuals separate from the core calculations.

* **bond_data.py**
  Stores all the input data (prices, coupons, and maturities) in dictionaries. This makes it easy to update the bonds without changing the code in other files.

...

Overall, the project keeps the bootstrapping logic simple while staying close to how yield curves are built in practice. The code is organized so that each part (data, math, and plotting) is easy to modify or extend.

**Assumptions:** This project assumes **no risk** (all bonds are risk-free) and **no arbitrage**, consistent with standard textbook yield curve construction.

**Note:** The goal of this project was to turn textbook knowledge into practical Python code. It was primarily a learning exercise and not intended for real-world trading or financial decisions.
