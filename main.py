from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)


# Global storage for incoming data

@app.route('/stats', methods=['POST'])
def compute_statistics():
    try:
        # Extract data from the request
        numbers = request.json.get('numbers', [])
        print(numbers)
        if not isinstance(numbers, list) or not all(isinstance(n, (int, float)) for n in numbers):
            return jsonify({"error": "Invalid input. Provide a list of numbers."}), 400

        # Add the incoming numbers to the data store
        data_store = numbers

        if not data_store:
            return jsonify({"error": "No data available for statistics."}), 400

        # Compute statistics
        data = np.array(data_store)

        # Convert numpy types to Python types using .item()
        mean = np.mean(data).item() if isinstance(np.mean(data), np.generic) else np.mean(data)
        median = np.median(data).item() if isinstance(np.median(data), np.generic) else np.median(data)
        variance = np.var(data).item() if isinstance(np.var(data), np.generic) else np.var(data)
        std_dev = np.std(data).item() if isinstance(np.std(data), np.generic) else np.std(data)
        min_val = np.min(data).item() if isinstance(np.min(data), np.generic) else np.min(data)
        max_val = np.max(data).item() if isinstance(np.max(data), np.generic) else np.max(data)
        q1 = np.percentile(data, 25).item() if isinstance(np.percentile(data, 25), np.generic) else np.percentile(data,25)
        q3 = np.percentile(data, 75).item() if isinstance(np.percentile(data, 75), np.generic) else np.percentile(data,75)
        iqr = q3 - q1  # Interquartile range

        # Construct response
        response = {
            "boxplot": {
                "min": min_val,
                "q1": q1,
                "median": median,
                "q3": q3,
                "max": max_val,
                "iqr": iqr
            },
            "mean": mean,
            "variance": variance,
            "std_dev": std_dev,
            "total_data_points": len(data_store),
            "all_data": data_store  # Optional: can be removed for large datasets
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
