from src.Text_summarization.config.configuration import ConfigurationManager
from src.Text_summarization.conponents.data_training_PEFT import PEFTModelTrainer



class PEFTTrainingPipeline:
    def __init__(self):
        pass



    def main(self):

        obj= ConfigurationManager()
        config_data = obj.get_data_trainign_config()
        Model_obj=PEFTModelTrainer(config_data)
        Model_obj.Trainign()
