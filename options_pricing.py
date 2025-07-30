import numpy as np
from scipy.stats import norm

def black_scholes_price(S, K, tau, r, sigma, option_type='call'):
    """
    Parameters:
    S : Underlying asset price
    K : strike price
    tau : time to maturity (in years) i.e. tau = T - t
    r : annualized risk-free interest rate, continuously compounded
    sigma : standard deviation of stock's return. i.e. sqrt of quadratic varion of stock's
            log price process (volatility)
    option_type : 'call' or 'put'
    """
    d1 =(np.log(S/K) + (r+0.5 * sigma **2) *tau) / (sigma * np.sqrt(tau))
    d2 = d1 - sigma * np.sqrt(tau)

    if option_type == 'call':
        price = S * norm.cdf(d1) - K * np.exp(-r * tau) * norm.cdf(d2)
    else:
        price = K * np.exp(-r * tau) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return price


def greeks(S, K, tau, r, sigma, option_type='call'):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * tau) / (sigma * np.sqrt(tau))
    d2 = d1 - sigma * np.sqrt(tau)

    delta = norm.cdf(d1) if option_type == 'call' else -norm.cdf(-d1)
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(tau))
    vega = S * norm.pdf(d1) * np.sqrt(tau) / 100  # per 1% change
    theta = None
    rho = None

    if option_type == 'call':
        theta = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(tau))
                 - r * K * np.exp(-r * tau) * norm.cdf(d2)) / 365
        rho = K * tau * np.exp(-r * tau) * norm.cdf(d2) / 10000
    else:
        theta = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(tau))
                 + r * K * np.exp(-r * tau) * norm.cdf(-d2)) / 365
        rho = -K * tau * np.exp(-r * tau) * norm.cdf(-d2) / 10000

    return {
        'Delta': delta,
        'Gamma': gamma,
        'Vega': vega,
        'Theta': theta,
        'Rho': rho
    }