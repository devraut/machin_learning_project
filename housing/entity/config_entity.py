from collections import namedtuple

DataIngestionConfig=namedtuple("DataIngestionConfig",
                               ["dataset_download_url","tgz_download","raw_data_dir","ingested_train_dir","ingested_test_dir"])
                               
DataTransformationConfig=namedtuple("DataTransformationConfig",["add_bedroom_per_room","transformed_train_dir","transformed_test_dir","preprocessed_object_file_path"])    

ModelTrainCofig=namedtuple("ModelTrainingCofig",["trained_model_file_path","base_accuracy"])

ModelEvaluationConfig=namedtuple("ModelEvaluationConfig",["model_evaluation_file_path","time_stamp"])

ModelPusherConfig=namedtuple("ModelPusherCofig",["export_dir_path"])