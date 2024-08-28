import google.generativeai as genai
import sys
import re

GOOGLE_API_KEY = "AIzaSyBPECzTHf4puygABmCZF6H91ZP-yU3nD8g"  # Replace with your actual Gemini API key

# Configure Gemini with the API key
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-pro")

def get_gemini(Question):
   


    prompt = """As a Netflix data analyst with direct access to the MongoDB database where the dataset is stored, your role is to directly fetch and provide specific data points from the database according to the queries received. 
    The dataset contains fields such as `show_id`, `type`, `title`, `director`, `cast`, `country`, `date_added`, `release_year`, `rating`, `duration`, `listed_in`, and `description`.

For each query:

1. Treat this as a new, independent request. Do not consider any previous queries or responses.

2. Verify if the dataset contains the required information to answer the query. If the necessary data is unavailable, promptly inform the user that the query cannot be answered with the available dataset.

3. If the data is available:
   - Connect to the MongoDB database.
      from pymongo import MongoClient
      client = MongoClient("mongodb+srv://nkash:g3fWLeuje4TLnLpG@cluster0.ayufk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
      db = client['netflix_db']
      collection = db['netflix_data']
   - Directly execute the query to fetch the relevant data from the `netflix_data` collection.
   - Quickly process and analyze the data to answer the specific question posed by the user.
   - Provide a concise answer based on the data retrieved, including any significant findings or numbers relevant to the query.
   - Disconnect from the database once the information has been retrieved and the response prepared.

4. Keep the response focused and direct, ensuring that the user's query is answered efficiently and accurately. Avoid detailing the analytical steps. Do not include code snippets unless specifically requested.

5. In cases where the query lacks details or is ambiguous, clarify the query with the user to ensure the response is as accurate as possible.
"""
    # prompt = "Forget all previous instructions"
    

    response = model.generate_content(prompt+Question)
    return response.text

def extract_python_code(response):
    # Use regex to find content between ```python and ``` markers
    match = re.search(r'```python\n(.*?)```', response, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def execute_gemini_result(Question):
    response = get_gemini(Question)
    code = extract_python_code(response)
    if code:
        return exec(code)
    else:
        print ("Response:"+response)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        question = sys.argv[1]
        execute_gemini_result(question)
    else:
        print("No question provided")
# def execute_gemini_result(Question):
#     exec(get_gemini(Question))
