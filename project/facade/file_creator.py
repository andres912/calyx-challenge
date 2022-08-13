class FileCreator:

    STORAGE_FOLDER = "stored_data"
    MUSEUMS_FILE_PATH = f"{STORAGE_FOLDER}/museums.csv"
    CINEMAS_FILE_PATH = f"{STORAGE_FOLDER}/cinemas.csv"
    LIBRARIES_FILE_PATH = f"{STORAGE_FOLDER}/libraries.csv"

    @classmethod
    def create_files(cls, requested_data):
        with open(cls.MUSEUMS_FILE_PATH, "w") as f:
            f.write(requested_data.museums_data)
        with open(cls.CINEMAS_FILE_PATH, "w") as f:
            f.write(requested_data.cinemas_data)
        with open(cls.LIBRARIES_FILE_PATH, "w") as f:
            f.write(requested_data.libraries_data)
