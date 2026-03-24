# ============================================================
# Phase 3 | Topic 1: Probability
# ============================================================
# Probability = kisi event ke hone ki chance (0 to 1)
# P(event) = favorable outcomes / total outcomes
# ============================================================

import random
import collections

random.seed(42)

# ─────────────────────────────────────────
# 1. Basic Probability
# ─────────────────────────────────────────
print("=== Basic Probability ===")

# Coin toss
total   = 1000
heads   = sum(random.choice([0,1]) for _ in range(total))
tails   = total - heads
print(f"Coin toss {total} times:")
print(f"  Heads: {heads} → P(H) = {heads/total:.3f}")
print(f"  Tails: {tails} → P(T) = {tails/total:.3f}")

# Dice roll
rolls = [random.randint(1,6) for _ in range(6000)]
freq  = collections.Counter(rolls)
print(f"\nDice roll 6000 times:")
for face in sorted(freq):
    print(f"  {face}: {freq[face]} → P = {freq[face]/6000:.3f}  (expected: 0.167)")

# ─────────────────────────────────────────
# 2. Conditional Probability
# ─────────────────────────────────────────
print("\n=== Conditional Probability ===")
# P(A|B) = P(A and B) / P(B)
# Example: Students jo pass hue unme se kitne ne study ki?

students = 100
studied_and_passed  = 60
not_studied_passed  = 10
studied_failed      = 15
not_studied_failed  = 15

p_studied  = (studied_and_passed + studied_failed) / students   # 0.75
p_pass_given_studied = studied_and_passed / (studied_and_passed + studied_failed)

print(f"P(studied)           = {p_studied:.2f}")
print(f"P(pass | studied)    = {p_pass_given_studied:.2f}")
print(f"P(pass | not studied)= {not_studied_passed/(not_studied_passed+not_studied_failed):.2f}")

# ─────────────────────────────────────────
# 3. Bayes Theorem
# ─────────────────────────────────────────
print("\n=== Bayes Theorem ===")
# P(A|B) = P(B|A) * P(A) / P(B)
# Example: Spam detection
# P(spam) = 0.3, P(not spam) = 0.7
# P(word "free" | spam) = 0.8
# P(word "free" | not spam) = 0.1
# P(spam | "free" in email) = ?

p_spam         = 0.3
p_not_spam     = 0.7
p_free_spam    = 0.8
p_free_no_spam = 0.1

p_free = p_free_spam * p_spam + p_free_no_spam * p_not_spam
p_spam_given_free = (p_free_spam * p_spam) / p_free

print(f"P(spam)              = {p_spam}")
print(f"P('free' | spam)     = {p_free_spam}")
print(f"P('free' | not spam) = {p_free_no_spam}")
print(f"P('free')            = {p_free:.3f}")
print(f"P(spam | 'free')     = {p_spam_given_free:.3f}  ← Bayes result")

# ─────────────────────────────────────────
# 4. Simulation — Monte Carlo
# ─────────────────────────────────────────
print("\n=== Monte Carlo: Estimate Pi ===")
# Circle ke andar random points dalo — pi estimate karo
import math

n = 100000
inside = 0
for _ in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        inside += 1

pi_estimate = 4 * inside / n
print(f"Points: {n}")
print(f"Pi estimate : {pi_estimate:.4f}")
print(f"Actual Pi   : {math.pi:.4f}")
print(f"Error       : {abs(pi_estimate - math.pi):.4f}")
