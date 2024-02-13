from transformers import DataCollatorForSeq2Seq
from transformers import TrainingArguments, Trainer
from src.Text_summarization.entity import DataTrainignConfig
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from peft import LoraConfig, get_peft_model, TaskType
from datasets import  load_from_disk
import torch
import os


class PEFTModelTrainer:
    def __init__(self, config: DataTrainignConfig):
        self.config=config



    def Trainign(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"   
        print(device)
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        # seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)

        lora_config = LoraConfig(
        r=32, # Rank
        lora_alpha=32,
        target_modules=["q", "v"],
        lora_dropout=0.05,
        bias="none",
        task_type=TaskType.SEQ_2_SEQ_LM # FLAN-T5
                                  )
        peft_model = get_peft_model(model_pegasus, 
                            lora_config)
        
        peft_training_args = TrainingArguments(
                            output_dir=self.config.root_dir,
                            auto_find_batch_size=True,
                            learning_rate=1e-3, # Higher learning rate than full fine-tuning.
                            num_train_epochs=1,
                            logging_steps=1,
                            max_steps=1    
                                             )

       

        dataset_samsum_pt = load_from_disk(self.config.data_path)
        dataset_samsum_pt = dataset_samsum_pt.filter(lambda example, index: index % 100 == 0, with_indices=True)
        print("========Trainable Data Set")
        print(dataset_samsum_pt)
        print("===========================")
        peft_trainer = Trainer(
                                model=peft_model,
                                args=peft_training_args,
                                train_dataset=dataset_samsum_pt["train"],
                                )
       
        peft_trainer.train()

        model_pegasus.save_pretrained(os.path.join(self.config.root_dir,"flan-t5-base-model") )
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))
