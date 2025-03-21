# pipelines in python
# Finding the longest pipeline and return maximum threshold time
# Given pipeline
pipelines = [
    ("Data Ingestion", 30),
    ("preprocessing", 45),
    ("Model Training", 120),
    ("Evaluation", 20),
]
threshold = 40

# to find the longest pipeline we are using the time given with the corresponding pipelines above
long_pipeline = max(pipelines, key=lambda x: x[1])   # the lambda function will access the time of pipelines

# identify the pipeline which are exceding the threshold value given with corresponding pipelines
exceding_pipeline = [pipeline for pipeline in pipelines if pipeline[1] > threshold]

print("Longest pipeline : ", long_pipeline)
print("List of pipelines exceeding threshold : ", exceding_pipeline)
