import os
import numpy
import pandas
from matplotlib import pyplot as plt
import torch
import torchvision
from transformers import AutoModel, AutoTokenizer
import utils

papers_path = '/mnt/d416ad47-cd5c-4158-b1de-889fdd9cbcb6/PersonalProjects/STEM Projects/AI-ML-DL/SP-Collab/papers'

model_name = "dmis-lab/biobert-v1.1"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModel.from_pretrained(model_name)

# List of text from research ppaers
documents = utils.extract_text_from_pdf(papers_path)

