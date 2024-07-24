from src.extract.data_extract import DataExtract
from src.extract.http_requester import HttpRequester
from src.load.data_load import DataLoad
from src.transform.data_transform import DataTransform

if __name__ == '__main__':
    response = HttpRequester()
    response = response.http_response()
    data = DataExtract(response)
    data_extract = data.extract_values()
    df = DataTransform(data_extract)
    df = df.data_transforms()
    data_load = DataLoad(df)
    data_load.load_data()
