import os

import torch
import numpy as np
from app.routes_2 import *
from app import model
from app import tokenizer

def test_download_model():
    """
    Unit test to check whether the app/trained_model directory has only
    the following three files: config.json, pytorch_model.bin, training_args.bin
    """
    save_directory = 'app/trained_model'
    to_scan = {'config.json','pytorch_model.bin', 'training_args.bin'}
    for dir_path, dir_names, files in os.walk(save_directory):
        for file in files:
            assert file in to_scan
            to_scan.discard(file)
    assert to_scan == set()

def test_load_model():
    """
    Unit test to check whether the model and the tokenizer 
    are loaded properly.
    """
    assert model != None
    assert tokenizer != None

def test_model():
    """
    Unit test to check the consistency of model. 
    Compares the soft predictions and hard predictions obtained from the model with the 
    expected values. 
    """
    test_sentence = "Since 1978, CEO compensation rose over 1,000% and only 11.9% for average workers."
    soft_preds, hard_preds = predict_statement(sentence=test_sentence, model=model, tokenizer=tokenizer)
    actual_values = np.array([0.3159, 0.6841])
    preds = soft_preds.detach().numpy()[0]
    assert all(np.isclose(actual_values, preds, atol=1e-4))
    assert hard_preds[0] == 1