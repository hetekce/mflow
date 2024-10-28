import json
import mlflow

from mlflow.models import ModelSignature
from transformers import T5ForConditionalGeneration, T5Tokenizer
from mlflow.types.schema import Schema, ColSpec


class TranslateGermanFromEnglish(mlflow.pyfunc.PythonModel):
    
    def __init__(self):
        self.model = T5ForConditionalGeneration.from_pretrained("google-t5/t5-small")
        self.tokenizer = T5Tokenizer.from_pretrained("google-t5/t5-small")
    
    def predict(self, context, model_input):
        input_ids = self.tokenizer(f"Translate English to German and make sure that the encoding is correct: {model_input}", return_tensors="pt").input_ids
        outputs = self.model.generate(input_ids)
        decoded_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Ensure output encoding is utf-8 for the decoded text
        decoded_text = decoded_text.encode('utf-8', 'ignore').decode('utf-8', 'ignore')
        return decoded_text

input_schema = Schema([ColSpec("string", "text")])
output_schema = Schema([ColSpec("string", "text")])
model_signature = ModelSignature(inputs=input_schema, outputs=output_schema)

# Create the signature without Schema
# input_schema = json.dumps([{'name': 'text', 'type': 'string'}])
# output_schema = json.dumps([{'name': 'text', 'type': 'string'}])
# model_signature = ModelSignature.from_dict({'inputs': input_schema, 'outputs': output_schema})

# It is required the model to be registered.
mlflow.set_tracking_uri("http://127.0.0.1:5000")

with mlflow.start_run(run_name="translator") as run:
    run_id = run.info.run_id
    print(f"Run id:  {run_id}")
    print(f"To serve the model run the command:\n"
          f"mlflow models serve -m runs:/{run_id}/model --no-conda -p 5001\n\n")
    
    mlflow.pyfunc.log_model('model', 
                            loader_module=None, 
                            data_path=None, 
                            code_path=None,
                            conda_env=None,
                            python_model=TranslateGermanFromEnglish(),
                            artifacts=None,
                            registered_model_name="model_translator",
                            signature=model_signature,
                            input_example=None,
                            await_registration_for=0
                            )
