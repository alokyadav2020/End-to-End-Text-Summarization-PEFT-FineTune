import os
import sys
from pathlib import Path
import urllib.request as request
import zipfile
from src.Text_summarization.logging import logger
from src.Text_summarization.utils.common import get_size
from src.Text_summarization.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config


        # create_directories([self.config.local_data_file])



    def downloda_dat_file(self):
        
        if not os.path.exists(self.config.local_data_file):
            filename,headers = request.urlretrieve(url=self.config.source_url,filename=self.config.local_data_file)
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  


    def extrac_zip_file(self):

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)