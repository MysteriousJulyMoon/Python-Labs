
import pandas as pd
import random
import os


class CsvFileManager:
    def init (self, file_path):
        self.data = pd.read_csv(file_path)
        self.file_path = file_path

    def Show(self, show_type="top", num_rows=5, separator=","):
        if show_type == "bottom":
            print(self.data.tail(num_rows).to_string(index=False, sep=separator))
        elif show_type == "random":
            print(self.data.sample(num_rows).to_string(index=False, sep=separator))
        else:
            print(self.data.head(num_rows).to_string(index=False, sep=separator))

    def Info(self):
        print(f"The number of rows with data and the number of columns in the table: {self.data.shape[0] - 1}x{self.data.shape[1]}")   #Количество строк с данными и количество колонок в таблице
        print("Information about data fields:")  #Информация о полях данных
        for col in self.data.columns:
            non_empty_count = self.data[col].count()
            col_type = self.data[col].dtype
            print(f"{col:<10} Qty {non_empty_count-1:<5} {col_type}")

    def DelNaN(self):
        self.data.dropna(inplace=True)
        print("Empty fields have been deleted.")  #Пустые поля удалены

    def MakeDS(self):
        learning_data = self.data.sample(frac=0.7, random_state=1)
        testing_data = self.data.drop(learning_data.index)

        if not os.path.exists("workdata"):
            os.makedirs("workdata")

        learning_data.to_csv("workdata/Learning/train.csv", index=False)
        testing_data.to_csv("workdata/Testing/test.csv", index=False)
        print("The data was split successfully.")  #Данные разделены успешно

# Создание экземпляра класса CsvFileManager и обработка файла "data.csv"
csv_manager = CsvFileManager("data.csv")

# Пример использования функций:
csv_manager.Show(show_type="top", num_rows=5, separator=",")
csv_manager.Info()
csv_manager.DelNaN()
csv_manager.MakeDS()
