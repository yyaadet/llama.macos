# LLaMA

**Notice**
1. This repo can run in CPU, but slow.
2. Add more test codes

**Articles**
1. [深入理解类chatgpt的meta大模型LLaMA工作原理](https://mp.weixin.qq.com/s?__biz=MjM5NjMzMDQ0Mg==&mid=2648534407&idx=1&sn=650d80e3633a869ae60bba4e0e43c964&chksm=bec3232289b4aa3435d19645982938ad42611ff5cc415401b4a2c7cbef627f56486c62f072b0&token=1647633786&lang=zh_CN#rd)
2. [在MacBook Pro M1上从零搭建自己的Chatgpt大模型AI助手](https://mp.weixin.qq.com/s?__biz=MjM5NjMzMDQ0Mg==&mid=2648534401&idx=1&sn=5c549b2a5c9b681c9ede222b44cec778&chksm=bec3232489b4aa3293ba0c2ded8a8d7538ba26b033af0edaf08d2d4b181e1e4715c9d3ce7e21&token=1647633786&lang=zh_CN#rd)


This repository is intended as a minimal, hackable and readable example to load [LLaMA](https://ai.facebook.com/blog/large-language-model-llama-meta-ai/) ([arXiv](https://arxiv.org/abs/2302.13971v1)) models and run inference.
In order to download the checkpoints and tokenizer, fill this [google form](https://forms.gle/jk851eBVbX1m5TAv5)

## Setup

In a conda env with pytorch / cuda available, run:
```
pip install -r requirements.txt
```
Then in this repository:
```
pip install -e .
```

## Download

Once your request is approved, you will receive links to download the tokenizer and model files.
Edit the `download.sh` script with the signed url provided in the email to download the model weights and tokenizer.

## Inference

The provided `example.py` can be run on a single or multi-gpu node with `torchrun` and will output completions for two pre-defined prompts. Using `TARGET_FOLDER` as defined in `download.sh`:
```
torchrun --nproc_per_node MP example.py --ckpt_dir $TARGET_FOLDER/model_size --tokenizer_path $TARGET_FOLDER/tokenizer.model
```

Different models require different MP values:

|  Model | MP |
|--------|----|
| 7B     | 1  |
| 13B    | 2  |
| 33B    | 4  |
| 65B    | 8  |

## FAQ

- [1. The download.sh script doesn't work on default bash in MacOS X](FAQ.md#1)
- [2. Generations are bad!](FAQ.md#2)
- [3. CUDA Out of memory errors](FAQ.md#3)
- [4. Other languages](FAQ.md#4)

## Reference

LLaMA: Open and Efficient Foundation Language Models -- https://arxiv.org/abs/2302.13971

```
@article{touvron2023llama,
  title={LLaMA: Open and Efficient Foundation Language Models},
  author={Touvron, Hugo and Lavril, Thibaut and Izacard, Gautier and Martinet, Xavier and Lachaux, Marie-Anne and Lacroix, Timoth{\'e}e and Rozi{\`e}re, Baptiste and Goyal, Naman and Hambro, Eric and Azhar, Faisal and Rodriguez, Aurelien and Joulin, Armand and Grave, Edouard and Lample, Guillaume},
  journal={arXiv preprint arXiv:2302.13971},
  year={2023}
}
```

## Model Card
See [MODEL_CARD.md](MODEL_CARD.md)

## License
See the [LICENSE](LICENSE) file.
