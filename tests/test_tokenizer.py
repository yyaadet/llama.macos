import sys
import os

basedir = os.path.dirname(__file__)
llama_lib = os.path.join(basedir, "..")
sys.path.append(llama_lib)

import unittest
from unittest import TestCase
from llama.tokenizer import Tokenizer
from settings import TOKEN_MODEL_PATH


class TestTokenizer(TestCase):
    def setUp(self):
        self.token_model_path = TOKEN_MODEL_PATH
        self.tokenizer = Tokenizer(self.token_model_path)

    def test_encode(self):
        s = "hello world! Let's go"
        s_ids = self.tokenizer.encode(s, True, True)
        except_ids = [1, 22172, 3186, 29991, 2803, 29915, 29879, 748, 2]
        self.assertGreater(len(s_ids), 0)
        self.assertEqual(except_ids, s_ids)

    def test_decode(self):
        s_ids = [1, 22172, 2]
        s = self.tokenizer.decode(s_ids)
        print(s)
        self.assertEqual(s, "hello")

    def test_n_words(self):
        print(self.tokenizer.n_words)
        self.assertGreater(self.tokenizer.n_words, 0)


if __name__ == "__main__":
    unittest.main()