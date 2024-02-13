
from src.Text_summarization.constants import *
from src.Text_summarization.utils.common import read_yaml,create_directories
from src.Text_summarization.entity import (DataIngestionConfig,DataValidationConfig,
                                           DataTransformationConfig,
                                           DataTrainignConfig,
                                           ModelEvalutionConfig)


# ceate configuration manager 
class ConfigurationManager:
    def __init__(self, config_filepath = CONFIG_FILE_PATH, param_filepath = PARAMS_FILE_PATH):
         self.config = read_yaml(config_filepath)
         self.params = read_yaml(param_filepath)
        

         create_directories([self.config.artifacts_root])


    def get_data_ingestion_confid(self) -> DataIngestionConfig:
         config = self.config.data_ingestion

         create_directories([config.root_dir])

         data_ingestion_config = DataIngestionConfig(
              root_dir= config.root_dir,
              source_url = config.source_url,
              local_data_file = config.local_data_file,
              unzip_dir= config.unzip_dir
         )

         return data_ingestion_config
    



    def get_data_validation_config(self)-> DataValidationConfig:
         config= self.config.data_validation

         create_directories([config.root_dir])

         data_validation_config = DataValidationConfig(
              root_dir= config.root_dir,
              validation_status=config.validation_status,
              all_required_file=config.all_required_file
              
         )

         return data_validation_config
    


    def get_data_transformation_config(self)-> DataTransformationConfig:
         config=self.config.data_transformation

         create_directories([config.root_dir])

         data_transformation_config=DataTransformationConfig(
              
              root_dir=config.root_dir,
              data_path=config.data_path,
              tokenizer=config.tokenizer
              )
         
         return data_transformation_config
    


    def get_data_trainign_config(self)-> DataTrainignConfig:
         config= self.config.model_trainer
         param= self.params.TrainingArguments

         create_directories([config.root_dir])

         data_training_config= DataTrainignConfig(
              
              root_dir=config.root_dir,
              data_path=config.data_path,
              model_ckpt=config.model_ckpt,
              num_train_epochs=param.num_train_epochs,
              warmup_steps=param.warmup_steps,
              per_device_train_batch_size=param.per_device_train_batch_size,
              weight_decay=param.weight_decay,
              logging_steps=param.logging_steps,
              evaluation_strategy=param.evaluation_strategy,
              eval_steps=param.eval_steps,
              save_steps=param.save_steps,
              gradient_accumulation_steps=param.gradient_accumulation_steps

         )

         return data_training_config
    

    def get_model_evaluation_config(self)->ModelEvalutionConfig:
         config= self.config.model_evaluation

         create_directories([config.root_dir])

         model_evalution_config= ModelEvalutionConfig(
              root_dir=config.root_dir,
              data_path=config.data_path,
              model_path=config.model_path,
              tokenizer_path=config.tokenizer_path,
              metric_file_name=config.metric_file_name

         )

         return model_evalution_config
    


    



     





         