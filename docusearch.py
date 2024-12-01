import os
import numpy
import pandas
from matplotlib import pyplot as plt
import torch
import torchvision
from torch.nn.functional import cosine_similarity
from transformers import AutoModel, AutoTokenizer
import utils

papers_path = '/mnt/d416ad47-cd5c-4158-b1de-889fdd9cbcb6/PersonalProjects/STEM Projects/AI-ML-DL/SP-Collab/papers'

model_name = "dmis-lab/biobert-v1.1"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModel.from_pretrained(model_name)

# List of text from research ppaers
documents = utils.extract_text_to_list_pydf2(papers_path)

query = "Hormonal disorder"
query_tokens = tokenizer(query, return_tensors='pt')

with torch.no_grad():
    query_embedding = model(**query_tokens).last_hidden_state.mean(dim=1)

document_embeddings = []
for doc in documents:
    doc_tokens = tokenizer(doc, return_tensors='pt')
    with torch.no_grad():
        doc_embedding = model(**doc_tokens).last_hidden_state.mean(dim=1)
        document_embeddings.append(doc_embedding)

document_embeddings = torch.cat(document_embeddings)

similarities = cosine_similarity(query_embedding, document_embeddings)

num_results = 2
top_k_indices = torch.topk(similarities, k=num_results).indices

for index in top_k_indices:
    print(f"Relevant Document: {documents[index]}")
