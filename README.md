Transformer Model Instructions:

Install the following libraries

1) pip install spacy
2) pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_core_sci_md-0.5.4.tar.gz
3) pip install -U pip setuptools wheel
4) python -m spacy download en_core_web_trf 
5) pip install -U spacy transformers
6) pip install jupyter-notebook

For Training :

Clear the trained model with command if already existing( else continue with training) 
    spacy project clean

In GPU (recommended strongly):

    spacy project run train_gpu

In CPU:

    spacy project run train_cpu

For evaluation:

    spacy project run evaluate

For Prediction:

Place the file inside assests in the same format as given in the sample Predict.BioC.JSON

Then run this command once done:
In GPU (recommended strongly):

    spacy project run all_gpu

In CPU:

    spacy project run all
