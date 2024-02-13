from transformers import AutoTokenizer
from datasets import load_from_disk
from src.Text_summarization.config.configuration import DataTransformationConfig

import os



class DataTransformaton:
    def __init__(self, config: DataTransformationConfig):
        self.config= config
        self.tokenizer= AutoTokenizer.from_pretrained(self.config.tokenizer)

    def tokenize_function(self,example):
        start_prompt = 'Summarize the following conversation.\n\n'
        end_prompt = '\n\nSummary: '
        prompt = [start_prompt + dialogue + end_prompt for dialogue in example["dialogue"]]
        example['input_ids'] = self.tokenizer(prompt, padding="max_length", truncation=True, return_tensors="pt").input_ids
        example['labels'] = self.tokenizer(example["summary"], padding="max_length", truncation=True, return_tensors="pt").input_ids

        return example

    # The dataset actually contains 3 diff splits: train, validation, test.
    # The tokenize_function code is handling all data across all splits in batches.
    # tokenized_datasets = dataset.map(tokenize_function, batched=True)
    # tokenized_datasets = tokenized_datasets.remove_columns(['id', 'topic', 'dialogue', 'summary',])

    # def convert_examples_to_features(self,example_batch):
    #     input_encodings = self.tokenizer(example_batch['dialogue'] , max_length = 1024, truncation = True )

    #     with self.tokenizer.as_target_tokenizer():
    #         target_encodings = self.tokenizer(example_batch['summary'], max_length = 128, truncation = True )

    #     return {
    #         'input_ids' : input_encodings['input_ids'],
    #         'attention_mask': input_encodings['attention_mask'],
    #         'labels': target_encodings['input_ids']
    #     }
    

    def convert(self):
        dataset_samsum = load_from_disk(self.config.data_path)
        dataset_samsum_pt = dataset_samsum.map(self.tokenize_function, batched=True)
        dataset_samsum_pt = dataset_samsum_pt.remove_columns(['id', 'topic', 'dialogue', 'summary',])

        # dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched = True)
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir,"dataset"))
