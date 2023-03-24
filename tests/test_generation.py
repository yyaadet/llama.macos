import sys
import os

basedir = os.path.dirname(__file__)
llama_lib = os.path.join(basedir, "..")
sys.path.append(llama_lib)

import unittest
from unittest import TestCase
from settings import TOKEN_MODEL_PATH, LLM_MODEL_PATH
from llama.generation import LLaMA
from llama.model import ModelArgs, Transformer
from llama.tokenizer import Tokenizer
from example import load


class TestAttention(TestCase):
    def setUp(self):
        self.llama = load(LLM_MODEL_PATH, TOKEN_MODEL_PATH, 0, 0, 512, 32, True)

    def test_generate(self):
        prompts = [
            "implement lr with python"
        ]
        generate_text = self.llama.generate(prompts, 128)
        self.assertGreater(len(generate_text), 0)
        print(generate_text)


if __name__ == "__main__":
    unittest.main()