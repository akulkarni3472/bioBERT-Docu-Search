import numpy
import pandas
from matplotlib import pyplot as plt
import torch
import torchvision
from transformers import AutoModel, AutoTokenizer

papers_path = '../papers'

model_name = "dmis-lab/biobert-v1.1"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModel.from_pretrained(model_name)
