def validate_body(data, required_values):
    for value in required_values:
        if value not in data:
            return {'error': f'"{value}"  is required in body'}, 400
    return None