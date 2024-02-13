from src.Text_summarization.conponents.data_transformation import DataTransformaton
from src.Text_summarization.config.configuration import ConfigurationManager



class TransformationPipeline:
    def __init__(self):
        pass




    def main(self):
        obj= ConfigurationManager()
        config_data = obj.get_data_transformation_config()
        tokenizer_obj=DataTransformaton(config_data)
        tokenizer_obj.convert()
