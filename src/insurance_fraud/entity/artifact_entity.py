from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionArtifact:
          train_file_path:Path
          test_file_path:Path

@dataclass(frozen=True)
class DataValidationArtifact:
    validation_status:bool
    valid_train_file_path:Path
    invalid_train_file_path:Path
    valid_test_file_path:Path
    invalid_test_file_path:Path
    drift_report_file_path:Path

@dataclass(frozen=True)
class DataTransformationArtifact:
    transformed_object_file_path:Path
    transformed_train_file_path:Path
    transformed_test_file_path:Path

@dataclass(frozen=True)
class ModelTrainerArtifact:
    trained_model_file_path:Path
    trained_metric_artifact:Path
    test_metric_artifact:Path

@dataclass(frozen=True)
class ClassificationMetricsArtifact:
    f1_Score:float
    precision_Score:float
    recall_Score:float
    roc_auc_Score:float