## Setup instructions
## Python environment
#### This repository has been tested on Python 3.6 and 3.7. It aims to support any Python 3 version.

#### To setup, start by cloning the repository:

#### git clone https://github.com/mohanchoudhary096/writing-better-questions.git

#### Then, navigate to the repository and create a python virtual environment using virtualenv:

cd writing-better-questions

virtualenv ml_editor

You can then activate it by running:

source ml_editor/bin/activate

Then, install project requirements by using:

pip install -r requirements.txt

The library uses a few models from spacy. To download the small and large English model (required to run the app and the notebooks), run these commands from a terminal with your virtualenv activated:

python -m spacy download en_core_web_sm

python -m spacy download en_core_web_lg

Finally, the notebooks and library leverage the nltk package. The package comes with a set of resources that need to be individually downloaded. To do so, open a Python session in an activated virtual environment, import nltk, and download the required resource.

Here is an example of how to do this for the punkt package from an active virtual environment with nltk installed:

python

import nltk

nltk.download('punkt')

Notebook examples
The notebook folder contains usage examples for concepts covered in the book. Most of the examples only use one of the subfolders in archive (the one that contains data for writers.stackexchange.com).

I've included a processed version of the data as a .csv for convenience.

If you wanted to generate this data yourself, or generate it for another subfolder, you should:

Download a subfolder from the stackoverflow archives

Run parse_xml_to_csv to convert it to a DataFrame

Run generate_model_text_features to generate a DataFrames with precomputed features

The notebooks belong to a few categories of concepts, described below.

### Data Exploration and Transformation
Dataset Exploration (notebooks\dataset_exploration.ipynb)
Splitting Data      (notebooks\splitting_data.ipynb)
Vectorizing Text (notebooks\vectorizing_text.ipynb)
Clustering Data (notebooks\clustering_data.ipynb)
Tabular Data Vectorization  (notebooks\tabular_data_vectorization.ipynb)
Exploring Data To Generate Features (notebooks\exploring_data_to_generate_features.ipynb)
### Initial Model Training and Performance Analysis 
Train Simple Model (notebooks\train_simple_model.ipynb)
Comparing Data To Predictions (notebooks\comapring_data_to_predictions.ipynb)
Top K (notebooks\top_k.ipynb)
Feature Importance (notebooks\feature_importance.ipynb)
Black Box Explainer (notebooks\black_box_explainer.ipynb)
### Improving the Model
Second Model (notebooks\second_model.ipynb)
Third Model   (notebooks\third_model.ipynb)
### Model Comparison
Comparing Models (notebooks\comapring_models.ipynb)
### Generating Suggestions from Models
Generating Recommendations (notebooks\generating_recommendations.ipynb)

## Running the prototype Flask app
#### To run the app, simply navigate to the root of the repository and run:

#### FLASK_APP=app.py flask run

#### The above command should spin up a local web-app you can access at http://127.0.0.1:5000/

## Troubleshooting
#### If you have any questions or encounter any roadblocks, please feel free to open an issue or email me at mohanchoudhary096@gmail.com.
