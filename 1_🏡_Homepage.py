import streamlit as st
# import functools
from openai import OpenAI
import json5
import random
import string
# from dotenv import load_dotenv

# load_dotenv()

# OpenAI API key
# replace line 12

client = OpenAI(api_key=api_key)

csv_dataset_file_path = './dataset.csv'

# Misc functions

# Generate a random alphanumeric string of length 5


def generate_uid():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=5))


# @functools.lru_cache(maxsize=128)
def search_result_row(product, other_results = []):
    col1, col2 = st.columns([1, 4])

    with col1:
        st.image(product['product_image_url'], width=100)
    with col2:
        st.subheader(product['product_name'])

        print("In search row")

        if st.button('View', key=product['product_uid']):
            print("Supposed to navigate")

            st.session_state['product'] = product
            st.session_state['other_search_results'] = other_results

            st.switch_page("pages/2_🛒_Product_Page.py")

# Function to search for products


# @functools.lru_cache(maxsize=128)
def run_model_recommendation(search_term):
    # Read the CSV file content
    csv_content = ''
    with open(csv_dataset_file_path, 'r') as csv_file:
        csv_content_lines = csv_file.readlines()
        # Joining CSV content with escaped newlines to insert into JSON
        csv_content = '\\n'.join([line.strip() for line in csv_content_lines])

        prompt = """
                            Train on this CSV,
                            
                            --start training here--
                            {csv_content}
                            --end training here---
                            
                            Take the role of a recomendation system,
                            Using your training data, when asked \"search term '<sarch term or query>'\", produce the json result.
                            Limit results to a maximum of 10 items.
                            
                            DON'T truncate the matches for brevity or any other reason, strictly.
                            If the matches are too much, only include the matches that you can output in the json response.
                            Don't any any text like 'other matches truncated for response brevity' so the json remains valid, strictly.
                            Limit results to not more than 20 items to keep it brief.
                            
                            Search results should be from the training CSV only. return an empty array if there's no result.
                            
                            Produce the output in this format, a JSON array:
                            
                            Search results:
                            ```
                            [
                                    {
                                    "product_uid":"{the valid product uid from your training data",
                                    "product_name":"{the valid product name from your training data",
                                    "product_description":"{the product description from your training data",
                                    "product_image_url":"{the valid product image url from your training data. It 'SHOULD' point to a valid image url, or a placeholder image otherwise, which 'MUST' also be a valid URL",
                                    "product_image_visual_description": "the visual description of the image, you can try loading the image, then try describing it"
                                    "search_relevance_score": "<the score, guess the score based on the relevance of the search result, MUST be a valid floating point number between 0.0 and 1.0>",
                                    "reason_for_recommendaion": "<the reason for commending this product for the given search query>",
                                    "related_items": [
                                        # NOTE that this field is mandatory, and if there are no related products, recommend items that may be closely similar, forexample, hammer is related to nail, Refrigerator is related to fridge, or just an empty array, .
                                        # No more than 5 related items similar in structure to this parent item, related contecxtually baed on relevance, or product name or descripion, processed with natural language.
                                        # They MUST not have the 'related_items' property so we don't do nesting, on that note, there STRICTLY should be no tailing coma after `reason_for_recommendaion` so the JSON remains valid.s
                                        # Remember, related items shold hve the same structure as the parent object except for the 'related_items' field, but they should have product_uid, product_name, product_description, product_image_url, product_image_visual_description, product_image_visual_description, search_relevance_score, and reason_for_recommendaion.
                                        ]
                                    },
                                    ... other matches ...
                                ]
                                ```
                            """.replace('{csv_content}', csv_content)

        # print(prompt)

        completion = client.chat.completions.create(
            # model="gpt-3.5-turbo-0125",
            model="gpt-4-0125-preview",
            messages=[
                {
                    "role": "system",
                    "content": prompt
                },
                {
                    "role": "user",
                    "content": "search term '" + search_term + "'"
                }
            ]
        )

        response = completion.choices[0].message.content

        return response


# @functools.lru_cache(maxsize=128)
def search_products(query):
    raw_result = run_model_recommendation(query)
    raw_result = raw_result.replace('Search results:', '').replace(
        '```json', '').replace('```', '').replace('```', '').replace('json', '')

    print("raw_result: ", raw_result)

    result = json5.loads(raw_result)

    return result

# Main page function with product search and enhanced display


# @functools.lru_cache(maxsize=128)
def main_page():
    st.title('Enhanced Home Depot Search Platform')
    query = st.text_input('Search for products',
                          on_change=clear_product_selection)

    if query:
        results = search_products(query)

        if results:
            for product in results:
                search_result_row(product)

        else:
            st.warning(
                "No products found matching your search. Please try again with a different query.")


# Helper function to clear product selection when initiating a new search

def clear_product_selection():
    if 'product' in st.session_state:
        del st.session_state['product']


# Initialize session state for navigation
if 'navigation' not in st.session_state:
    st.session_state['navigation'] = 'Home'


main_page()
