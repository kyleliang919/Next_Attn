# Next_Attn
## Installation
```
pip install torchtitan
```
```
conda install conda-forge::torchtitan
```

## Run command
download the Llama 3.1 tokenizer to your local machine.
```
# Get your HF token from https://huggingface.co/settings/tokens

# Llama 3.1 tokenizer
python scripts/download_tokenizer.py --repo_id meta-llama/Llama-3.1-8B --hf_token=...
```

```
CONFIG_FILE="./torchtitan/models/llama3/train_configs/llama3_8b.toml" ./run_train.sh
```


```
# For 16B model support:
python scripts/download_tokenizer.py --repo_id deepseek-ai/deepseek-moe-16b-chat
```

```
# 16B parameter model: adapted from older 16B parameter model from https://huggingface.co/deepseek-ai/deepseek-moe-16b-base
CONFIG_FILE="./torchtitan/models/deepseek_v3/train_configs/deepseek_v3_16b.toml" ./run_train.sh
```