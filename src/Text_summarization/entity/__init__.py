from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path




@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    validation_status: str
    all_required_file: list    



@dataclass(frozen=True) 
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer: Path



@dataclass(frozen=True)
class DataTrainignConfig:
    root_dir: Path
    data_path: Path
    model_ckpt: Path
    num_train_epochs: float
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: str
    eval_steps: None
    save_steps: int
    gradient_accumulation_steps: int


@dataclass(frozen=True)
class ModelEvalutionConfig:
    root_dir: Path
    data_path: Path
    model_path: Path
    tokenizer_path: Path
    metric_file_name: Path

