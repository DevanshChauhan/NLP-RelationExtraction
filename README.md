# Relation Extraction using SVM and RoBERTa on BioRED Dataset

## Project Overview

This project focuses on the task of **Relation Extraction (RE)**, a critical area in Natural Language Processing (NLP). The goal of RE is to determine and categorize the semantic links between entities in a text. In this project, we have developed machine learning models to extract relationships from the **BioRED** dataset. The models we employed include:

1. **Support Vector Machine (SVM)**
2. **Transformer-based model using RoBERTa**

## Dataset

The dataset used in this project is **BioRED** (Biological Research Entity Dataset), a specialized dataset that contains named entities and the relationships between them in biomedical literature.

### Preprocessing

The preprocessing steps included:

- Tokenization of text data
- Entity recognition and extraction
- Data cleaning and formatting to prepare it for model training

## Models and Methodology

### 1. **Support Vector Machine (SVM)**
   - **Model Description**: A traditional machine learning model was trained on the preprocessed BioRED data to predict relationships between named entities.
   - **Performance**: This model achieved an **F-score of 0.55**, which serves as a baseline for comparison.

### 2. **RoBERTa (Transformer-based Model)**
   - **Model Description**: A pre-trained RoBERTa model was fine-tuned on the BioRED dataset for relation extraction. This model leverages transformers for better context understanding and relationship extraction.
   - **Performance**: The RoBERTa-based model outperformed the SVM, with an **F-score of 0.76**, demonstrating its effectiveness for this complex task.

## Results

| Model      | F-score |
|------------|---------|
| SVM        | 0.55    |
| RoBERTa    | 0.76    |

The RoBERTa-based approach shows significant improvement over the traditional SVM model, which is noteworthy given the complexity of the BioRED dataset.

## Conclusion

This project demonstrates the application of both traditional and transformer-based machine learning models for relation extraction in the BioRED dataset. While the SVM model provides a solid baseline, the transformer-based RoBERTa model yields substantially better results. This work highlights the effectiveness of advanced transformer models in complex NLP tasks like relation extraction.

## Requirements

To reproduce the results, you will need the following libraries and dependencies:

- Python 3.8+
- scikit-learn
- PyTorch
- Transformers (Hugging Face)
- pandas
- numpy

You can install the required libraries using the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. **Data Preprocessing**: Preprocess the BioRED dataset by running the `preprocess.py` script.
2. **Model Training**: Train the SVM and RoBERTa models using the `train_svm.py` and `train_roberta.py` scripts, respectively.
3. **Evaluation**: Evaluate the models on the test set using the `evaluate.py` script, and compare the F-scores.

## Future Work

- Further fine-tuning of the transformer-based models for better performance
- Exploration of additional pre-trained models like BERT, GPT, etc.
- Experimenting with other advanced NLP techniques such as graph neural networks (GNNs) for relation extraction

## Acknowledgments

This project was developed as part of an effort to explore machine learning techniques in relation extraction tasks within the biomedical domain. Special thanks to the creators of the **BioRED dataset** for providing a rich and complex dataset for research purposes.

## Contact

For any queries or collaboration opportunities, please feel free to reach out to me:

- **Devansh Chauhan**
- [LinkedIn](https://www.linkedin.com/in/devansh-chauhan-773901171/)
- [GitHub](https://github.com/DevanshChauhan)

