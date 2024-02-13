import os
from src.Text_summarization.entity import DataValidationConfig
from src.Text_summarization.logging import logger





class DataValidation:
    def __init__(self, config:DataValidationConfig):
        self.config=config

    def  get_data_validated(self)->bool:

        try:

            ValidationStatus= None
            all_File_path = os.listdir(os.path.join("artifacts","data_ingestion","dataset"))    

            for file  in all_File_path:
                if file not in self.config.all_required_file:
                    ValidationStatus= False
                    with open(self.config.validation_status,'w') as f:
                        f.write(f"Validation status: {ValidationStatus}")
                        logger.info("File not found")

                else:
                    ValidationStatus= True
                    with open(self.config.validation_status,'w') as f:
                        f.write(f"Validation status: {ValidationStatus}")
                        logger.info("File found")


            return ValidationStatus 

        except Exception as e:
            raise e
           
