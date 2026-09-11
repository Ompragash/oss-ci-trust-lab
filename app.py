"""Small application used to exercise contributor CI."""
import json


def total_cost(items, discount_percent=0):
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100")
    if any(item < 0 for item in items):
        raise ValueError("Prices cannot be negative")
    return round(sum(items) * (1 - discount_percent / 100), 2)


if __name__ == "__main__":
    print(json.dumps({"application": "oss-ci-isolation-lab", "total": total_cost([10, 20], 10)}))
