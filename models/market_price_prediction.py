## Fine-Tuning the FinBERT Sentiment Analysis model

# importing the necessary libraries
import pandas as pd
import torch
from sklearn.model_selection import train_test_split
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments, pipeline

# Load and preprocess the dataset
data = pd.read_csv('/kaggle/input/sentiment-analysis-dataset/training.1600000.processed.noemoticon.csv', encoding='ISO-8859-1')

# data.head()  # used to view the first 5 entries in our dataframe

# data.columns.values.tolist()   # list the list of the dataframe

texts = data['text of the tweet\xa0'].tolist()
labels = data['polarity of tweet\xa0'].tolist()

# Inspect the unique labels
print("Unique labels before conversion:", set(labels))

# Convert sentiment labels to binary (0 and 1)
labels = [0 if label == 0 else 1 for label in labels]

'''
# Inspect the unique labels after conversion
print("Unique labels after conversion:", set(labels))
'''

# Split the dataset
train_texts, test_texts, train_labels, test_labels = train_test_split(texts, labels, test_size=0.1)

# Load the tokenizer
tokenizer = BertTokenizer.from_pretrained('ProsusAI/finbert')

# Tokenize the data
train_encodings = tokenizer(train_texts, truncation=True, padding=True)
test_encodings = tokenizer(test_texts, truncation=True, padding=True)

# Convert to PyTorch dataset
class FinancialDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

train_dataset = FinancialDataset(train_encodings, train_labels)
test_dataset = FinancialDataset(test_encodings, test_labels)

# Load the model
model = BertForSequenceClassification.from_pretrained('ProsusAI/finbert')

# Define training arguments
training_args = TrainingArguments(
    output_dir='./results',          
    num_train_epochs=3,              
    per_device_train_batch_size=8,  
    per_device_eval_batch_size=8,   
    warmup_steps=500,                
    weight_decay=0.01,               
    logging_dir='./logs', 
    logging_steps=10,  # Reduce logging frequency to speed up training
)

# Initialize Trainer
trainer = Trainer(
    model=model,                         
    args=training_args,                  
    train_dataset=train_dataset,         
    eval_dataset=test_dataset             
)

# Train the model
trainer.train()

# Save the model
model.save_pretrained('./finbert_finetuned')
tokenizer.save_pretrained('./finbert_finetuned')




