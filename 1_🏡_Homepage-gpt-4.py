from openai import OpenAI
import time
import requests
import json

# OpenAI API key
api_key = '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'

client = OpenAI(api_key=api_key)

# jsonl_file_path = './training-sequence.jsonl'
csv_dataset_file_path = './dataset.csv'
# payload_file_path = './payload.jsonl'

# # OpenAI API URL for uploading documents
# upload_url = "https://api.openai.com/v1/files"

# fine_tune_url = "https://api.openai.com/v1/fine-tunes"

# # start comment here


# def populate_dataset(json_file_path, csv_file_path):
#     with open(json_file_path, 'r') as json_file:
#         data = json.load(json_file)

#     # Read the CSV file content
#     csv_content = ''
#     with open(csv_file_path, 'r') as csv_file:
#         csv_content_lines = csv_file.readlines()
#         # Joining CSV content with escaped newlines to insert into JSON
#         csv_content = '\\n'.join([line.strip() for line in csv_content_lines])

#     # Replace the "{csv_content}" placeholder in the JSON file
#     for message in data['messages']:
#         if message['role'] == 'user':
#             # Replacing the placeholder with actual CSV content
#             message['content'] = message['content'].replace(
#                 '{csv_content}', csv_content)

#     # Write the modified data to "payload.jsonl" as a single line (JSON Lines format)
#     output_file_path = 'payload.jsonl'
#     with open(output_file_path, 'w') as jsonl_file:
#         for _ in range(10):
#             # Writing JSON as a single line without indentation
#             jsonl_file.write(json.dumps(data) + '\n')


# def populate_training_sequence(json_file_path, training_sequence):
#     # Write the dictionary to a file
#     with open(json_file_path, 'w') as f:
#         json.dump(training_sequence, f, indent=4)

# # # Data preparation phase


# training_sequence = {
#     "messages": [
#         {
#             "role": "system",
#             "content": "Train on this CSV, --start training here-- {csv_content} --end training here---"
#         },
#         {
#             "role": "user",
#             "content": """
#                         Take the role of a recomendation system,
#                         You will be prompted with queries for products, in natural language.
#                         Using the csv you trained on, recommend related products. so when you get a query like "search term '<whatever the user searches for>'",
#                         e.g "search term '9 inch nails'",give a json response in this format, a list of max 50 matching items.:

#                         [
#                              {
#                              "product_uid":"{the valid product uid from your training data}",
#                              "product_name":"{the valid product name from your training data}",
#                              "product_description":"{the product description from your training data}",
#                              "product_image_url":"{the valid product image url from your training data. It should point to a valid image url, or a placeholder image otherwise.}",
#                              "product_image_visual_description": "the visual description of the image, you can try loading the image, then try describing it"m
#                              "search_relevance_score": "<the score, guess the score based on the relevance of the search result>",
#                              "reason_for_recommendaion": "<the reason for commending this product for the given search query>",
#                              "related_items": [
#                                  <5 related items similar in structure to this parent item, related contecxtually baed on relevance, or product name or descripion, processed with natural language. They should not have the "related_items" property so we don't do nesting>
#                                  ]
#                              },
#                              ... other matches ...
#                          ]

#                         And that's it. No verbose answers, just the json response.

#                         Remember, no verbose response, just the list of matchign items, and 5 related items based on context, and relevance

#                         Also learn from subsequent queries, and reorder the items in your query result, based on how often they're queried or how relevant they are
#                         """
#         },
#         {
#             "role": "assistant",
#             "content": "I see you provided a CSV file containing home depo products, I'm ready, let's give it a test run, query me."
#         },
#     ],
# }

# # Populate training-sequence.jsonl with the trianing sequence data
# populate_training_sequence(jsonl_file_path, training_sequence)

# # Populate training sequeuce with csv dataset
# populate_dataset(jsonl_file_path, csv_dataset_file_path)

# # end comment here

# # # Headers for the API request
# headers = {
#     "Authorization": f"Bearer {api_key}",
# }

# # Step 1: Upload file for fine-tuning
# with open(payload_file_path, 'rb') as file:

#     # Prepare the data for uploading
#     files = {
#         'file': file
#     }

#     data = {
#         'purpose': 'fine-tune'
#     }

#     # Upload the file
#     response = requests.post(
#         upload_url, headers=headers, files=files, data=data)

#     # Check if the upload was successful
#     if response.status_code == 200:
#         # Get the file ID from the response
#         file_id = response.json()['id']

#         print("File uploaded successfully. File ID:", file_id)
#     else:
#         print("Failed to upload the file:", response.text)


# # Step 2: Initiate fine-tuning
# fine_tune_job = client.fine_tuning.jobs.create(
#     training_file=file_id,
#     model="gpt-3.5-turbo"
#     #   model="gpt-4-0613"
# )

# fine_tune_id = fine_tune_job.id

# print("fine_tune_id: ", fine_tune_id)


# # Step 3: Poll for fine-tuning job completion
# tuning_complete = False
# while not tuning_complete:
#     # Retrieve the state of a fine-tune
#     tuning_task = client.fine_tuning.jobs.retrieve(fine_tune_id)

#     print("tuning_status: ", tuning_task)

#     if tuning_task.status == "failed":
#         raise Exception("Finetuning the model failed")

#     if tuning_task.status == "complete" or tuning_task.fine_tuned_model is not None:
#         fine_tuned_model_id = tuning_task.fine_tuned_model
#         tuning_complete = True

#     print("Waiting for fine-tuning to complete...")
#     time.sleep(60)  # Adjust polling interval as necessary, in seconds


# Step 4: Use the fine-tuned model for completion
# Read the CSV file content
csv_content = ''
with open(csv_dataset_file_path, 'r') as csv_file:
    csv_content_lines = csv_file.readlines()
    # Joining CSV content with escaped newlines to insert into JSON
    csv_content = '\\n'.join([line.strip() for line in csv_content_lines])

    search_term = "Everything"
    completion = client.chat.completions.create(
        # model=fine_tuned_model_id,  # Use the fine-tuned model ID
        # model="ft:gpt-3.5-turbo-0613:personal::8ssGUE0v",  # Use the fine-tuned model ID
        # model="gpt-3.5-turbo-0613",  
        # model="gpt-3.5-turbo-0125",
        model="gpt-4-0125-preview", 
        messages=[
            {
                "role": "system",
                "content": """
                        Train on this CSV,
                        
                        --start training here--
                        {csv_content}
                        --end training here---
                        
                        Take the role of a recomendation system,
                        Using your training data, when asked \"search term '<sarch term or query>'\", produce the json result.
                        Limit results to a maximum of 10 items.
                        
                        Produce the output in this format:
                        
                        Search results:
                        ```
                        [
                                {
                                "product_uid":"{the valid product uid from your training data}",
                                "product_name":"{the valid product name from your training data}",
                                "product_description":"{the product description from your training data}",
                                "product_image_url":"{the valid product image url from your training data. It should point to a valid image url, or a placeholder image otherwise.}",
                                "product_image_visual_description": "the visual description of the image, you can try loading the image, then try describing it"m
                                "search_relevance_score": "<the score, guess the score based on the relevance of the search result>",
                                "reason_for_recommendaion": "<the reason for commending this product for the given search query>",
                                "related_items": [
                                    # 5 related items similar in structure to this parent item, related contecxtually baed on relevance, or product name or descripion, processed with natural language. They should not have the 'related_items' property so we don't do nesting
                                    # Remember, related items shold hve the same structure as the parent object except for the 'related_items' field, but they should have product_uid, product_name, product_description, product_image_url, product_image_visual_description, product_image_visual_description, search_relevance_score, and reason_for_recommendaion.
                                    ]
                                },
                                ... other matches ...
                            ]
                            ```
                        """.replace('{csv_content}', csv_content)
            },
            {
                "role": "user",
                "content": "search term '" + search_term + "'"
            }
        ]
    )

    print(completion.choices[0].message.content)
