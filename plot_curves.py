import matplotlib.pyplot as plt

def plot_spot_curve(spot_rates, parse_maturity):
    """Plot the spot rate curve (Bloomberg-style)."""
    maturities_sorted = sorted(spot_rates.keys(), key=parse_maturity)
    x_labels = maturities_sorted
    y_values = [spot_rates[m]*100 for m in maturities_sorted]

    plt.figure(figsize=(12,6))
    plt.plot(x_labels, y_values, marker='o', color='orange', linewidth=2)
    plt.gca().set_facecolor("black")
    plt.gcf().patch.set_facecolor("black")
    plt.xticks(rotation=45, color='white')
    plt.yticks(color='white')
    plt.title("Spot Rate Curve", color='white', fontsize=16)
    plt.xlabel("Maturity", color='white')
    plt.ylabel("Spot Rate (%)", color='white')
    plt.grid(color='gray', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()


def plot_forward_curve(forward_rates, parse_maturity, start_years=0.5):
    """Plot the forward rate curve (Bloomberg-style). Can skip short maturities."""
    # Filter forwards to start at start_years (default 6M)
    forward_filtered = {
        k: v for k, v in forward_rates.items()
        if parse_maturity(k.split("→")[0]) >= start_years
    }

    x_labels = list(forward_filtered.keys())
    y_values = [v*100 for v in forward_filtered.values()]

    plt.figure(figsize=(12,6))
    plt.plot(x_labels, y_values, marker='o', color='orange', linewidth=2)
    plt.gca().set_facecolor("black")
    plt.gcf().patch.set_facecolor("black")
    plt.xticks(rotation=45, color='white')
    plt.yticks(color='white')
    plt.title(f"Forward Rate Curve (From {start_years*12:.0f}M+)", color='white', fontsize=16)
    plt.xlabel("Period", color='white')
    plt.ylabel("Forward Rate (%)", color='white')
    plt.grid(color='gray', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()
