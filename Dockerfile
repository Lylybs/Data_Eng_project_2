FROM python:3.6
WORKDIR /Data_Eng_project_2
COPY * ./
RUN pip install -r requirements.txt
CMD ["python","toxic_app.py"]