"""
Chebyshev's Bias Visualization Tool

This script simulates and visualizes "prime number races" modulo q, illustrating
the phenomenon known as Chebyshev's Bias—where certain residue classes (typically 
quadratic non-residues) tend to lead the race against others (quadratic residues).

The script computes prime counting functions \pi(x; q, a) and plots the difference 
between pairs of residues up to a specified upper bound.

Requirements:
    - matplotlib
    - sympy

Author: Daniel Le
Date:   06/14/2026
"""

import math
import sympy
import matplotlib.pyplot as plt
import warnings

# Enable LaTeX rendering for high-quality mathematical typography in plots
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'

# Suppress minor matplotlib/LaTeX integration warnings for cleaner execution
warnings.filterwarnings("ignore")

def possible_mod(q):
    """Generates a list of all reduced residue classes modulo q.

    Finds all integers strictly less than q that are coprime to q. These
    represent the valid 'lanes' in the prime number race.

    Args:
        q (int): The modulus for the prime race.

    Returns:
        list of int: A sorted list of residues coprime to q.
    """
    return [x for x in range(1, q) if math.gcd(x, q) == 1]


def is_square(a, q):
    """Determines if a residue is a quadratic residue (perfect square) modulo q.

    Args:
        a (int): The residue class to check.
        q (int): The modulus.

    Returns:
        bool: True if there exists an x such that x^2 ≡ a (mod q), False otherwise.
    """
    return any((x * x) % q == a % q for x in range(1, q))


def is_qr_pair(a, b, q):
    """Checks if a pair of residues consists of one square and one non-square.

    In the context of Chebyshev's Bias, races between a quadratic residue (square) 
    and a quadratic non-residue (non-square) exhibit the most pronounced biases.

    Args:
        a (int): The first residue class.
        b (int): The second residue class.
        q (int): The modulus.

    Returns:
        bool: True if one residue is a square and the other is not; False otherwise.
    """
    a_is_qr = is_square(a, q)
    b_is_qr = is_square(b, q)
    return a_is_qr != b_is_qr


def plot_psi(q, limit):
    """Plots the net difference between all pairs of prime counting functions modulo q.

    Tracks the race between primes up to `limit`. Each valid pair of residue classes 
    (a, b) is plotted as a step function representing \pi(x; q, a) - \pi(x; q, b).
    Pairs showcasing a Square vs. Non-Square matchup are highlighted, while 
    homogenous pairs (e.g., Square vs. Square) are visually de-emphasized.

    Args:
        q (int): The modulus defining the racing lanes.
        limit (int): The maximum integer value to count primes up to.

    Returns:
        None: Displays a matplotlib step plot.
    """
    # Initialize the lanes and fetch all primes up to the limit
    lanes = possible_mod(q)
    primes = list(sympy.primerange(2, limit + 1))

    # History maps each residue to its cumulative prime count over time
    history = {a: [0] for a in lanes}
    x_coords = [0]
    current_counts = {a: 0 for a in lanes}

    # Process primes sequentially to build historical data for the step plot
    for p in primes:
        res = p % q
        if res in current_counts:
            current_counts[res] += 1
        
        x_coords.append(p)
        for a in lanes:
            history[a].append(current_counts[a])

    # Generate all unique pair combinations of racing lanes
    pairs = [(lanes[i], lanes[j]) for i in range(len(lanes)) for j in range(i+1, len(lanes))]
    single = len(pairs) == 1
    colors = plt.cm.tab10.colors

    # Initialize the plot canvas
    fig, ax = plt.subplots(figsize=(12, 6))

    # Iterate through every pair to calculate differences and plot them
    for idx, (a, b) in enumerate(pairs):
        # Calculate the delta history: \pi(x; q, a) - \pi(x; q, b)
        psi = [h_a - h_b for h_a, h_b in zip(history[a], history[b])]
        
        # Determine styling aesthetics
        color = 'blue' if single else colors[idx % len(colors)]
        key_pair = single or is_qr_pair(a, b, q)

        # Draw the step line (high opacity for key races, faint opacity for others)
        ax.step(x_coords, psi, where='post', color=color,
                alpha=0.8 if key_pair else 0.05,
                linewidth=1.4 if key_pair else 0.5,
                label=rf'$\pi(x;{q},{a}) - \pi(x;{q},{b})$')
        
        # Shade the region beneath the step line for visual depth
        ax.fill_between(x_coords, psi, step='post',
                        alpha=0.2 if key_pair else 0.05, color=color)

    # Draw a baseline at y=0 representing a perfectly tied race
    ax.axhline(0, color='red', linestyle='-', linewidth=0.8, alpha=0.3)
    
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'Lead $\psi(x)$')
    ax.set_title(f"Chebyshev's Bias Modulo {q}")
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Example execution: Racing primes modulo 4 up to 10,000
    # Modulo 4 isolates the famous race between 3 (non-square) and 1 (square)
    plot_psi(q=4, limit=10000)