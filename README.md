# Idiom Detection with LLaMA, Qwen, and XLM-R

This repo contains experiments on idiom (idiomatic vs literal) detection for multiword expressions (MWEs), based on **SemEval 2022 Task 2 – Subtask A** and an additional **low-resource idiom dataset**.  

We use:
- **LLMs:** LLaMA-3.2 Instruct, Qwen2.5 Instruct (zero-shot / one-shot, no fine-tuning).
- **Encoder model:** XLM-RoBERTa base (fine-tuned).
- **Languages:** English, Portuguese, and low-resource languages (e.g., Bengali, Punjabi, Malayalam).
- **Extras (EN):** Word Sense Disambiguation (WSD) with WordNet.

---

## Repo structure (main notebooks)

- `subtask1-en-llama.ipynb` – EN + LLaMA (zero/one-shot).
- `subtask1-en-qwen.ipynb` – EN + Qwen (zero/one-shot).
- `subtask1-en-qwen-wsd.ipynb` – EN + Qwen + WSD.
- `subtask1-en-xlmr.ipynb` – EN + XLM-R fine-tuning.
- `subtask1-en-xlmr-wsd.ipynb` – EN + XLM-R + WSD.

- `subtask1-pt-llama.ipynb` – PT + LLaMA.
- `subtask1-pt-qwen.ipynb` – PT + Qwen.
- `subtask1-pt-xlmr.ipynb` – PT + XLM-R trained on PT.
- `subtask1-pt-xlmr-en.ipynb` – XLM-R trained on EN, evaluated on PT.

- `subtask1-lrl-llama.ipynb` – LRL + LLaMA (zero-shot).
- `subtask1-lrl-qwen.ipynb` – LRL + Qwen (zero-shot).
- `subtask1-lrl-xlmr-en.ipynb` – XLM-R trained on EN, evaluated on LRL.

Each notebook loads data, builds the context text (previous / target / next sentence with marked MWE), runs the model, and writes predictions + metrics to an `outputs_*` folder.

---

## Data

**1. SemEval 2022 Task 2 Subtask A**

Download the official data and place it like:

```text
data/
  SemEval_2022_Task2-idiomaticity/
    SubTaskA/
      Data/
        train_zero_shot.csv
        train_one_shot.csv
        dev.csv
        dev_gold.csv
        eval.csv
        eval_submission_format.csv
````

Set `DATA_DIR` in the notebooks, e.g.:

```python
from pathlib import Path
DATA_DIR = Path("data") / "SemEval_2022_Task2-idiomaticity" / "SubTaskA"
```

**2. Low-resource idioms**

Place your file as:

```text
data/
  lrl_idioms.csv
```

Expected columns: `Language`, `Previous`, `Target`, `Next`, `MWE`, `Label`.

---

## Environment setup

Example with conda:

```bash
conda create -n idioms python=3.10 -y
conda activate idioms
```

Install dependencies:

```bash
pip install torch transformers accelerate sentencepiece \
            pandas numpy scikit-learn jupyter nltk
```

For WSD notebooks (once):

```python
import nltk
nltk.download("wordnet")
nltk.download("omw-1.4")
nltk.download("stopwords")
```

If needed for LLaMA / Qwen:

```bash
huggingface-cli login
```

---

## How to run

1. Start Jupyter from the repo root:

   ```bash
   jupyter notebook
   ```

2. Open the notebook you want (e.g. `subtask1-en-qwen.ipynb` or `subtask1-en-xlmr.ipynb`).

3. In the first cells:

   * Set `DATA_DIR` to your SemEval path.
   * Set `RUN_DEVICE = "gpu"` or `"cpu"`.
   * Optionally change the model name (e.g. smaller Qwen).

4. Run all cells. The notebook will:

   * Load and preprocess data.
   * Train (XLM-R) or run inference (LLaMA/Qwen).
   * Evaluate on the dev split (macro-F1, accuracy, confusion matrix).
   * Write eval predictions in SemEval submission format under `outputs_*`.

---

## Notes

* LLaMA / Qwen notebooks treat LLMs as frozen classifiers using prompts and the logits for `"0"` vs `"1"`.
* XLM-R notebooks fine-tune `xlm-roberta-base` with class-weighted loss and select the best model on dev macro-F1.
* WSD notebooks add a WordNet gloss for the MWE’s head word as extra input.

If you get file/path errors, check `DATA_DIR` and the location of `data/lrl_idioms.csv`.
