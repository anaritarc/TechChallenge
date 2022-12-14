FROM python:3.9
USER root

COPY requirements.txt /tmp/requirements.txt

COPY __init__.py ./ds/_init__.py 
RUN /__init__.py 

COPY feature_selection.py ./ds/feature_selection.py
COPY model.py ./ds/model.py
RUN /feature_selection.py model.py
