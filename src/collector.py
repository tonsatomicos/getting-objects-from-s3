import botocore.session
import os

from dotenv import load_dotenv
from pathlib import Path

class Collector:
    def __init__(self, aws_access_key_id, aws_secret_access_key):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key= aws_secret_access_key
        self.client = None

    def get_session(self):
        try:
            session = botocore.session.get_session()
            self.client = session.create_client(
                's3', 
                region_name='us-east-2', 
                aws_access_key_id= self.aws_access_key_id, 
                aws_secret_access_key= self.aws_secret_access_key
            )

        except Exception as e:
            print(f'Failed to connection: {e}')

    def get_object(self, bucket_name, path_to_search, local_base_path):
        if not self.client:
            return
        
        try:
            response = self.client.list_objects_v2(Bucket=bucket_name, Prefix=path_to_search)

            if 'Contents' in response:
                for s3_object in response['Contents']:
                    filename = s3_object['Key']
                    local_file_path = Path(Path(local_base_path, 'raw'), os.path.basename(filename))
                    processed_folder =  Path(Path(local_base_path, 'processed'), os.path.basename(filename))

                    if not processed_folder.is_file():
                        try:
                            response = self.client.get_object(Bucket=bucket_name, Key=filename)

                            with open(local_file_path, 'wb') as local_file:
                                local_file.write(response['Body'].read())
                                
                            self.client.delete_object(Bucket=bucket_name, Key=filename)
                            print(f'Downloaded file: {filename}')

                        except Exception as e:
                            print(f'Error when downloading file {filename}: {e}')

                    if processed_folder.is_file():
                        self.client.delete_object(Bucket=bucket_name, Key=filename)
                        print(f'File {filename} already exists in the processing folder, deleting')
            else:
                print('No objects were found.')

        except Exception as e:
            print(f'Failed to list objects: {e}')

        finally:
            if self.client is not None:
                self.client.close()
                self.client = None

def main():
    # Env
    dotenv_path = 'C://Tecnology//Projects//getting-objects-from-s3//config//.env'
    load_dotenv(dotenv_path)
    
    # Collector class configs
    aws_access_key_id = os.getenv("aws_access_key_id")
    aws_secret_access_key = os.getenv("aws_secret_access_key")

    # Collector.get_object class configs
    bucket_name = 'projeto-github-teste'
    path_to_search = 'arquivos_random/random'
    local_base_path = 'C://Tecnology//Projects//getting-objects-from-s3//data'

    # Collector class
    obj_collector = Collector(aws_access_key_id, aws_secret_access_key)
    obj_collector.get_session()

    #
    if obj_collector.client:
        obj_collector.get_object(bucket_name, path_to_search, local_base_path)

if __name__ == "__main__":
    main()