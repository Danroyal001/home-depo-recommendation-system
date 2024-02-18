import pandas as pd
import torch
from torch.utils.data import Dataset
from transformers import DistilBertTokenizerFast, DistilBertForQuestionAnswering, Trainer, TrainingArguments

# Define the path to your dataset
csv_file_path = './distillbert_dataset.csv'

# Attempt to load the dataset
try:
    df = pd.read_csv(csv_file_path)
except FileNotFoundError:
    raise Exception(f'The file {csv_file_path} was not found.')

# Initialize the tokenizer
tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased')

# Prepare the dataset class
class QADataset(Dataset):
    def __init__(self, encodings):
        self.encodings = encodings

    def __getitem__(self, idx):
        return {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}

    def __len__(self):
        return len(self.encodings.input_ids)

# Tokenize the contexts and questions
encodings = tokenizer(df['question'].tolist(), df['context'].tolist(), truncation=True, padding=True, max_length=512, return_tensors="pt")
dataset = QADataset(encodings)

# Define the model
model = DistilBertForQuestionAnswering.from_pretrained('distilbert-base-uncased')

# Training arguments
training_args = TrainingArguments(
    output_dir='./results', 
    num_train_epochs=3, 
    per_device_train_batch_size=2, 
    warmup_steps=500, 
    weight_decay=0.01, 
    logging_dir='./logs',
)

# Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
)

# Train the model
trainer.train()

# Save the fine-tuned model
model.save_pretrained('./fine_tuned_model')

# Function for asking questions using the trained model
def ask_question(question, context):
    inputs = tokenizer(question, context, add_special_tokens=True, return_tensors="pt")
    input_ids = inputs["input_ids"].tolist()[0]
    outputs = model(**inputs)
    answer_start_scores = outputs.start_logits
    answer_end_scores = outputs.end_logits
    answer_start = torch.argmax(answer_start_scores)
    answer_end = torch.argmax(answer_end_scores) + 1
    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end]))
    return answer

# Example usage (replace placeholders with actual data)
context = "The context for the question."
question = "The question to be asked."

print(ask_question(question, context))
