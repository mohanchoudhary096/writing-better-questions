from functools import lru_cache

REQUIRED_FEATURES=[
    "is_question",
    "action_verb_full",
    "language_question",
    "question_mark_full",
    "norm_text_len"
]


def find_absent_features(data):
    missing=[]
    for feat in REQUIRED_FEATURES:
        if feat not in data.keys():
            missing.append(feat)
    return missing


def check_features_types(data):
    types={
        "is_question": bool,
        "action_verb_full": bool,
        "language_question": bool,
        "question_mark_full": bool,
        "norm_text_len": float
    } 
    mistypes=[]
    for field, data_type in types:
        if not isinstance(data[field], data_type):
            mistypes.append((data[field], data_type))
    return mistypes

def run_heuristic(question_len):
    pass

@lru_cache(maxsize=128)
def run_model(question_data):
    pass


def validate_and_handle_request(question_data):
    missing=find_absent_features(question_data)
    if len(missing) > 0:
        raise ValueError(f"Missing features: {missing}")
    wrong_types=check_features_types(question_data)
    if len(wrong_types) > 0:
        if "text_len" in question_data.keys():
            if isinstance(question_data["text_len"], float):
                return run_heuristic(question_data["text_len"])
        raise ValueError(f"Incorrect types : {wrong_types}")
    return run_model(question_data)


def verify_output_type_and_range(output):
    if not isinstance(output, float):
        raise ValueError(f"Wrong output types: {output, type(output)}")
    if output <= 0 or output >=1:
        raise ValueError(f"Output out of range: {output}")


def validate_and_correct_output(question_data, model_output):
    try:
        verify_output_type_and_range(model_output)
    except ValueError:
        run_heuristic(question_data["text_len"])
    
    # If we did not raise an error , we return our model result
    return model_output

