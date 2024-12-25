from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

# Global storage for incoming data

@app.route('/stats', methods=['POST'])
def compute_statistics():

    try:
        # Extract data from the request
        numbers = request.json.get('numbers', [])
        if not isinstance(numbers, list) or not all(isinstance(n, (int, float)) for n in numbers):
            return jsonify({"error": "Invalid input. Provide a list of numbers."}), 400

        # Add the incoming numbers to the data store
        data_store = numbers

        if not data_store:
            return jsonify({"error": "No data available for statistics."}), 400

        # Compute statistics
        data = np.array(data_store)
        mean = np.mean(data)
        median = np.median(data)
        variance = np.var(data)
        std_dev = np.std(data)
        min_val = np.min(data)
        max_val = np.max(data)
        q1 = np.percentile(data, 25)  # First quartile
        q3 = np.percentile(data, 75)  # Third quartile
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
