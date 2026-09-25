# week6-lab
# IS212 Week 6 Lab: From Generated Tests to a CI Gate

This repository contains the code, unit test suite, and continuous integration (CI) pipeline configuration for the **QuackLoan** rubber-duck lending library's late-fee system (`DuckFine`).

The objective of this lab is to demonstrate how to combine AI-generated unit tests, mutation testing (fault injection), code coverage analysis, and GitHub Actions to establish a strict CI gate for software quality assurance.

---

## 📋 System Under Test (`DuckFine`)

The `DuckFine` class (`duckfine.py`) calculates late fees according to four core business rules:

1. **Grace Period:** The first **2 days** late are forgiven ($0.00 fine).
2. **Standard Rate:** Fines accrue at **$0.50 per chargeable day** after the grace period.
3. **Deluxe Rate:** Fines are **doubled** ($1.00/day) for Deluxe rubber ducks.
4. **Maximum Fine Cap:** A single fine never exceeds **$5.00**, regardless of days late or deluxe status.
5. **Running Total:** Fines accumulate against `total_owed` for the member.

---

## 🛠️ Project Structure

```text
.
├── .github/
│   └── workflows/
│       └── tests.yml       # GitHub Actions CI workflow (CI Gate)
├── duckfine.py             # Main library class implementation
├── test_duckfine.py        # Comprehensive unittest suite
├── .gitignore              # Ignores Python bytecode and coverage caches
└── README.md               # Project documentation