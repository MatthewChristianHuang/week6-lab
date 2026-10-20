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
│       └── main.yml        # GitHub Actions CI workflow (CI Gate)
├── duckfine.py             # Main library class implementation
├── app.py                  # Flask health and fine-calculation API
├── test_duckfine.py        # Comprehensive unittest suite
├── test_app.py             # Flask API tests
├── requirements.txt        # Python dependencies
├── .gitignore              # Ignores Python bytecode and coverage caches
└── README.md               # Project documentation
```

## REST API

Install dependencies with `pip install -r requirements.txt`, then start the
service with `flask --app app run`.

- `GET /health` returns `{"status": "ok"}`.
- `GET /fine?days=N&deluxe=1` returns the calculated fee as `{"fee": 0.5}`.
  The `deluxe` parameter is optional; only `deluxe=1` enables the deluxe rate.
  Missing, non-integer, or negative `days` values return HTTP 400 with an
  `error` message.