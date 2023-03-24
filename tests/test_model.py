import sys
import os

basedir = os.path.dirname(__file__)
llama_lib = os.path.join(basedir, "..")
sys.path.append(llama_lib)

import unittest
from unittest import TestCase
from settings import TOKEN_MODEL_PATH
from llama.model import Attention, ModelArgs, FeedForward, TransformerBlock, Transformer


class TestAttention(TestCase):
    def setUp(self):
        self.args = ModelArgs()

    def test_init(self):
        network = Attention(self.args)
        print(network)
        self.assertIsNotNone(network)

    def test_forward(self):
        pass


class TestFeedForward(TestCase):

    def setUp(self):
        self.args = ModelArgs()

    def test_init(self):
        network = FeedForward(self.args.dim, self.args.dim * 2, self.args.multiple_of)
        print(network)
        self.assertIsNotNone(network)


class TestTransformerBlock(TestCase):
    def setUp(self) -> None:
        self.args = ModelArgs()

    def test_init(self):
        network = TransformerBlock(1, self.args)
        print(network)
        self.assertIsNotNone(network)


class TestTransformer(TestCase):

    def setUp(self) -> None:
        self.args = ModelArgs()
        self.args.vocab_size = 32000

    def test_init(self):
        network = Transformer(self.args)
        print(network)
        self.assertIsNotNone(network)


if __name__ == "__main__":
    unittest.main()