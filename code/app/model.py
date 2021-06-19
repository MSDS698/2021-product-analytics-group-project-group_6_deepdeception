from transformers import DistilBertForSequenceClassification
from transformers import DistilBertTokenizerFast
import torch


def load_model(model_directory=None, model=DistilBertForSequenceClassification,
               tokenizer=DistilBertTokenizerFast, tokenizer_class='distilbert-base-uncased'):
    """
    Function to load a pretrained hugging face model.
    Returns a model and tokenizer
    """
    tokenizer_ = tokenizer.from_pretrained(tokenizer_class)  # Load tokenizer
    model_ = model.from_pretrained(model_directory)  # Load pretrained model
    return model_, tokenizer_


def predict_statement(sentence: str, model=None, tokenizer=None):
    """
    Function to get predictions from the inputted model and tokenizer
    Returns soft and hard predictions from a SINGLE sentence
    """
    inputs = tokenizer(sentence, truncation=True, padding=True, return_tensors="pt")
    outputs = model(**inputs)
    logit_probs = outputs.logits
    soft_preds = torch.softmax(logit_probs.float(), dim=1)  # Get soft predictions
    hard_preds = logit_probs.detach().numpy().argmax(
        axis=1)  # Get the predictions based on the higher probablity on columns
    return soft_preds, hard_preds
