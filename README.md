# Options Pricing and Visualization

A very simple app to visualize European option prices. Mostly an exercise in streamlit to learn how to build a basic web app.

Contact: josephbaroni@outlook.com

(figured out how to properly display markdown/latex yay!)

---

The Black-Scholes equation is a partial differential equation of the form

$$ \frac{\partial V}{\partial t} + \frac{1}{2} \sigma^{2} S^{2} \frac{\partial^{2} V}{\partial S^{2}} + rS \frac{\partial V}{\partial S} -rV =0 $$

where:
- $t$ is the time in years
- $r$ is the continuously compounded interest rate
- $S(t)$ is the price of the underlying asset at time $t$
- $V(S,t)$ is the price of the option
- $\sigma$ is the standard deviation of stock's returns (volatility)
- $C(S,t)$ price of a European call option
- $P(S,t)$ price of a European put option
- $T$ time of option expiration
- $\tau$ time until maturity, $\tau = T - t$
- $K$ strike price of the option.

Solving the equation with boundary conditions

$$ C(0,t) = 0 \, \, \forall t $$

$$ C(S,t) \rightarrow S-K \, \text{as} \, S \rightarrow \infty$$ 

$$ C(S,T) = \max \{ S-K, 0 \} $$

we obtain the Black-Scholes formula for a call option:

$$C(S(t),t) = N(d_{+})S(t) - N(d_{-})Ke^{-r \tau} $$

$$ d_{+}=\frac{1}{\sigma\sqrt{\tau}}\Big(\ln\Big(\frac{S(t)}{K}\Big)+\Big(r+\frac{\sigma^{2}}{2} \Big) \tau \Big)$$

$$ d_{-} = d_{+} - \sigma \sqrt{\tau} $$ 

and using put-call parity $(C-P = S-DK)$ we obtain for a corresponding put option

$$ P(S(t),t) = N(-d_{-})Ke^{-r \tau} -N(-d_{+})S(t) $$

where $N(x)$ is the standard normal cdf:

$$ N(x) = \frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{x} e^{-z^{2}/2} \, dz $$

 
---

## Run Locally

### 1. Clone the repo

```bash
git clone https://https://github.com/josephbaroni/options-pricing-and-visualization.git
cd options-visualizer
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run main.py
```
