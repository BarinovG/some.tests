import YandexAPI as yapi

class TestYandexFunc:

    # Тест на создание новой папки
    def test_create_folder_new(self):
        assert yapi.create_folder('New_Test') == (201, True)

    #Тест на создание существующей папки
    def test_create_folder_exists(self):
        assert yapi.create_folder('New_Test') == f'already yet'