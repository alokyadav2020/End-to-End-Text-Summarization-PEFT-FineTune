from src.Text_summarization.config.configuration import ConfigurationManager
from src.Text_summarization.conponents.data_ingestion import DataIngestion


class DataIngestionPipeline:
    def __init__(self):
        pass
    




    def main(self):
      
        config_file =ConfigurationManager()
        data_Ingestion_config = config_file.get_data_ingestion_confid()
        data_Ingestion = DataIngestion(data_Ingestion_config)
        data_Ingestion.downloda_dat_file()
        data_Ingestion.extrac_zip_file()
