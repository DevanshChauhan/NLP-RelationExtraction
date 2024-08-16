# Relation Extraction using SVM and RoBERTa on BioRED Dataset

## Project Overview

This project focuses on **Relation Extraction (RE)**, an essential task in Natural Language Processing (NLP). RE involves determining and categorizing semantic relationships between entities in text. In this project, we apply machine learning techniques to extract relationships from the **BioRED** dataset. The models used include:

1. **Support Vector Machine (SVM)**
2. **Transformer-based model using RoBERTa**

## Dataset

The **BioRED** (Biological Research Entity Dataset) is a specialized dataset containing named entities and their relationships in biomedical literature.

### Preprocessing

Preprocessing includes:
- Tokenizing text data
- Extracting named entities
- Cleaning and formatting the data for training

## Models and Methodology

### 1. **Support Vector Machine (SVM)**
   - **Model Description**: A traditional SVM model trained on the preprocessed BioRED data to predict relationships between entities.
   - **Performance**: Achieved an **F-score of 0.55**, serving as a baseline for comparison.

### 2. **RoBERTa (Transformer-based Model)**
   - **Model Description**: A pre-trained RoBERTa model fine-tuned on the BioRED dataset for relation extraction, leveraging transformers for advanced context understanding.
   - **Performance**: The RoBERTa model achieved a significantly better **F-score of 0.76**, outperforming the SVM model.

## Results

| Model      | F-score |
|------------|---------|
| SVM        | 0.55    |
| RoBERTa    | 0.76    |

## Transformer Model Setup and Instructions

### Installation

To set up the transformer model, follow these steps:

```bash
pip install spacy
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_core_sci_md-0.5.4.tar.gz
pip install -U pip setuptools wheel
python -m spacy download en_core_web_trf 
pip install -U spacy transformers
pip install jupyter-notebook
```

### Training the Transformer Model

1. **Clear Previous Models** (if applicable):
   ```bash
   spacy project clean
   ```

2. **Training on GPU** (strongly recommended):
   ```bash
   spacy project run train_gpu
   ```

3. **Training on CPU**:
   ```bash
   spacy project run train_cpu
   ```

### Evaluation

To evaluate the trained model, use the following command:

```bash
spacy project run evaluate
```

### Prediction

1. Place your prediction files in the `assets` directory, following the format of the sample `Predict.BioC.JSON` file.
2. Run the following command for prediction:

- **On GPU**:
  ```bash
  spacy project run all_gpu
  ```

- **On CPU**:
  ```bash
  spacy project run all
  ```

## Conclusion

This project demonstrates the application of SVM and transformer-based models (RoBERTa) for relation extraction in the BioRED dataset. While the SVM model provides a solid baseline, the transformer-based RoBERTa model significantly improves performance. The included transformer model setup provides a robust starting point for further experimentation in advanced NLP tasks.

## Requirements

To reproduce the results, you will need the following dependencies:

- Python 3.8+
- scikit-learn
- PyTorch
- Transformers (Hugging Face)
- spaCy
- pandas
- numpy

Install the dependencies using the command:

```bash
pip install -r requirements.txt
```

## Future Work

- Further fine-tuning of transformer-based models
- Exploration of additional models like BERT, GPT, etc.
- Experimentation with advanced techniques such as graph neural networks (GNNs)

## Acknowledgments

Special thanks to the creators of the **BioRED dataset** for providing a rich dataset for research. This project was developed as part of an effort to explore machine learning techniques in relation extraction within the biomedical domain.

## Contact

For any queries or collaboration opportunities:

- **Devansh Chauhan**
- [LinkedIn](https://www.linkedin.com/in/devansh-chauhan-773901171/)
- [GitHub](https://github.com/DevanshChauhan)
