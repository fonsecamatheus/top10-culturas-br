from src.extract.data_extract import DataExtract
from src.extract.http_requester import HttpRequester
from src.transform.data_transform import DataTransform

if __name__ == '__main__':
    response = HttpRequester()
    response = response.http_response()
    data = DataExtract(response)
    data_extract = data.extract_values()
    df = DataTransform(data_extract)
    df = df.data_transforms()
    print(df.head())
