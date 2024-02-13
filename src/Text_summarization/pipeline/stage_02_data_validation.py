from src.Text_summarization.entity import DataValidationConfig
from src.Text_summarization.conponents.data_validation import DataValidation
from src.Text_summarization.config.configuration import ConfigurationManager




class DataValidationPipeLine:
    def __init__(self):
        pass




    def main(self):

        obj= ConfigurationManager()
        config_data= obj.get_data_validation_config()
        validation_status= DataValidation(config_data)
        status =validation_status.get_data_validated()
        print(status)

        return status





   