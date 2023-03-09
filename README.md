# Annotated Text Visualisation

Taken Kaggle's dataset [Hotel Reviews Booking.com](https://www.kaggle.com/datasets/michelhatab/hotel-reviews-bookingcom?resource=download) we got entities and key phrases extracted with AWS Comprehend.

The project demonstrates the way to visualize the findings so the team get the feelings of the raw data.

## Input data
- `reviews.csv` a CSV file with reviews, one review per line
- `keyprases.txt` a text file with records containing extracted key phrases, each record is a json, one record per line. 
- `entities.txt` a text file with records containing extracted entities, each record is a json, one record per line. 

## Installation

1. `make install` loads python packages
2. `make run` runs the streamlit http server

## Key steps

### Prerequisites

Entities and Key phrases extraction is out of the scope and shall be done before. 

### Setup project 

- Specify packages in `requirements.txt`
- Setup directory structure
- Upload data: `reviews.txt`, `keyprases.txt`, `entities.txt`

### Build application

- setup and run a streamlit boilerplate application
- add review visualization
- add key phrases as text annotation
- add entities as text annotations
- add overview of key phrases (list of key phrases and the frequency of occurrence)
- add overview of entities

