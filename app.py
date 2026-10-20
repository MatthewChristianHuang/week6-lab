from flask import Flask, jsonify, request

from duckfine import DuckFine


app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/fine")
def fine():
    days = request.args.get("days")
    try:
        days_late = int(days)
    except (TypeError, ValueError):
        return jsonify({"error": "days must be a non-negative integer"}), 400

    if days_late < 0:
        return jsonify({"error": "days must be a non-negative integer"}), 400

    deluxe = request.args.get("deluxe") == "1"
    fee = DuckFine(member_id="api").charge(days_late=days_late, deluxe=deluxe)
    return jsonify({"fee": fee})
