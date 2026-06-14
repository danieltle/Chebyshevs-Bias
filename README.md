# Chebyshev's Bias and the Prime Race

A computational and theoretical investigation of **Chebyshev's Bias** — the phenomenon where primes congruent to quadratic non-residues consistently outnumber those congruent to quadratic residues over finite ranges, despite being asymptotically equal.

Written as a final paper for **MA 357 (Elementary Number Theory)** at Colby College.

---

## Overview

In 1853, Chebyshev observed that primes congruent to **3 (mod 4)** appear more frequently than primes congruent to **1 (mod 4)**. Although the Prime Number Theorem implies that both residue classes contain asymptotically equal proportions of primes, finite computations reveal a striking and persistent imbalance.

This project investigates that phenomenon computationally across several moduli and explains it using the theoretical framework developed by Rubinstein and Sarnak (1994).

The central question is:

> How can a systematic bias appear in prime distributions when number theory predicts eventual equality?

---

## Repository Contents

| File                | Description                                                                     |
| ------------------- | ------------------------------------------------------------------------------- |
| `chebyshev.py`      | Simulation and visualization engine for prime races modulo $q$                  |
| `Chebyshevs_Bias.pdf` | Research paper containing theoretical background, proofs, analysis, and results |

---

## Mathematical Background

For a modulus $q$, define the prime race function

$$
\psi(x;q,a,b) = \pi(x;q,a) - \pi(x;q,b)
$$

where

$$
\pi(x;q,a)
$$

counts the number of primes $p \le x$ satisfying

$$
p \equiv a \pmod q.
$$

When:

* $\psi(x;q,a,b) > 0$, residue class $a$ is leading.
* $\psi(x;q,a,b) < 0$, residue class $b$ is leading.

The most interesting races occur between **quadratic residues** and **quadratic non-residues**, where the observed bias is strongest.

---

## Running the Simulation

### Requirements

```bash
pip install matplotlib sympy
```

### Run

```bash
python chebyshev.py
```

The default configuration plots the modulo 4 prime race up to $x = 10,000$:

```python
plot_psi(q=4, limit=10000)
```

To investigate other races, modify the parameters at the bottom of the script.

---

## Sample Results

Computations were performed for six moduli

$$
q = 3;4;5;6;7;9
$$

up to

$$
x = 10,000,000.
$$

In every case examined, quadratic non-residue classes exhibited a measurable advantage.

| Modulus | Race                     | Observed Leader |
| ------- | ------------------------ | --------------- |
| $q=3$   | 1 vs 2                   | 2 (mod 3)       |
| $q=4$   | 1 vs 3                   | 3 (mod 4)       |
| $q=6$   | 1 vs 5                   | 5 (mod 6)       |
| $q=5$   | Residues vs Non-Residues | Non-Residues    |
| $q=7$   | Residues vs Non-Residues | Non-Residues    |
| $q=9$   | Residues vs Non-Residues | Non-Residues    |

Rubinstein and Sarnak showed that in the classical modulo 4 race, the class

$$
3 \pmod 4
$$

leads approximately **99.59%** of the time with respect to logarithmic density.

---

## Why Does the Bias Exist?

Rubinstein and Sarnak explained the phenomenon through the bias constant

$$
c(q,a) = -1 + \left| \left\\{ x \pmod q : x^2 \equiv a \pmod q \right\\} \right|.
$$

For a quadratic residue $a$, square roots exist modulo $q$, so

$$
c(q,a)\ge0.
$$

For a quadratic non-residue $b$,

$$
c(q,b)=-1.
$$

This asymmetry shifts the mean of the limiting logarithmic distribution governing prime races, producing a persistent statistical advantage for quadratic non-residues.

Importantly, the bias is **not permanent**.

In 1914, Littlewood proved that

$$
\psi(x;4,1,3)
$$

changes sign infinitely many times. Eventually, every contestant in the race takes the lead infinitely often. However, these sign changes occur so rarely that they are practically invisible within ordinary computational ranges.

---

## Key Takeaways

* Prime races reveal unexpected finite-scale structure in the distribution of primes.
* Quadratic non-residue classes consistently outperform quadratic residues across many moduli.
* The Prime Number Theorem guarantees eventual equality, but not short-term fairness.
* Rubinstein and Sarnak quantified the bias through limiting logarithmic distributions.
* Littlewood's theorem shows that the apparent winner never wins forever.

---

## References

1. Chebyshev, P. L. (1853). *Letter to Fuss on primes of the forms $4n+1$ and $4n+3$.*
2. Rubinstein, M., & Sarnak, P. (1994). *Chebyshev's Bias.* Experimental Mathematics.
3. Littlewood, J. E. (1914). *Sur la distribution des nombres premiers.* Comptes Rendus.
4. Selberg, A. (1949). *An Elementary Proof of the Prime Number Theorem.* Annals of Mathematics.

---

## Author

**Daniel Le**

Mathematics & Statistics • Computer Science

Colby College
