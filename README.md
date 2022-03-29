# Masters-Term-Paper
Reinforcement Learning for Options Pricing under discrete hedging.

In this paper, I investigate optimal option pricing in discrete dynamic hedging case 
using ML approach. For discrete hedging, it is impossible to hedge perfectly, which is
equivalent to the situation of incomplete market. Wilmott (1994) derived the correction
to the option price in this situation (assuming an options dealer is risk-neutral). Also
recently, there have been several papers applying ML methods to solve this problem. One
of them is the QLBS model by Halperin (2019) based on reinforcement learning. In this
work, I realized learning an optimal option price and its optimal hedging based on the
Q-learning Black-Scholes (QLBS) algorithm in comparison with Black-Scholes model with
adjusted volatility and test them for equivalence. As the result, I demonstrate that the
problem of hedging and pricing in discrete time with Wilmott‘s volatility adjustment is 
equivalent to finding optimal price and hedge received Halperin‘s algorithm (QLBS) with
some assumptions.
