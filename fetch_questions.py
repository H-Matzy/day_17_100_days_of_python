import requests


def fetch_quiz_questions(amount=10):
    url = f"https://opentdb.com/api.php?amount={amount}&type=boolean"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the request fails

        data = response.json()
        results = data.get("results", [])

        # Format the data as needed to match the sample in data.py
        formatted_questions = []
        for result in results:
            question = {
                "text": result["question"],
                "answer": result["correct_answer"],
                "category": result["category"]
            }
            formatted_questions.append(question)

        return formatted_questions

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []