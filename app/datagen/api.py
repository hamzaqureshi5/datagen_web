import os
import json
from flask import Flask, request, jsonify, send_file, send_from_directory
from STCAppScriptV6 import list_2_dict, dict_2_list, read_json, DataGenerationScript
from global_parameters import PARAMETERS, DATA_FRAMES
from operators.zong.read_files import ZongReaderHandle
from operators.zong.gen_files import ZongGenerateHandle


# from database_operations import database


class API:
    def __init__(self) -> None:
        # self.params = PARAMETERS.get_instance()
        # self.dataframe = DATA_FRAMES.get_instance()
        self.params = PARAMETERS()
        self.dataframe = DATA_FRAMES()
        self.output_dir = ""
        pass

    def __del__(self):
        del self

    def SET_ALL_FOR_API(self, data):
        self.params.set_K4(data["DISP"]["K4"])
        self.params.set_OP(data["DISP"]["op"])
        self.params.set_IMSI(data["DISP"]["imsi"])
        self.params.set_ICCID(data["DISP"]["iccid"])
        self.params.set_PIN1(data["DISP"]["pin1"])
        self.params.set_PUK1(data["DISP"]["puk1"])
        self.params.set_PIN2(data["DISP"]["pin2"])
        self.params.set_PUK2(data["DISP"]["puk2"])
        self.params.set_ADM1(data["DISP"]["adm1"])
        self.params.set_ADM6(data["DISP"]["adm6"])
        self.params.set_ACC(data["DISP"]["acc"])
        self.params.set_DATA_SIZE(data["DISP"]["size"])

        self.params.set_PRODUCTION_CHECK(data["DISP"]["prod_check"])
        self.params.set_ELECT_CHECK(data["DISP"]["elect_check"])
        self.params.set_GRAPH_CHECK(data["DISP"]["graph_check"])
        self.params.set_SERVER_CHECK(data["DISP"]["server_check"])

        self.params.set_SERVER_DICT(list_2_dict(data["PARAMETERS"]["server_variables"]))
        self.params.set_ELECT_DICT(list_2_dict(data["PARAMETERS"]["data_variables"]))
        self.params.set_GRAPH_DICT(data["PARAMETERS"]["laser_variables"])
        self.params.set_INPUT_PATH(data["PATHS"]["INPUT_FILE_PATH"])

        self.params.set_PIN1_RAND(data["DISP"]["pin1_rand"])
        self.params.set_PUK1_RAND(data["DISP"]["puk1_rand"])
        self.params.set_PIN2_RAND(data["DISP"]["pin2_rand"])
        self.params.set_PUK2_RAND(data["DISP"]["puk2_rand"])
        self.params.set_ADM1_RAND(data["DISP"]["adm1_rand"])
        self.params.set_ADM6_RAND(data["DISP"]["adm6_rand"])
        self.params.set_ACC_RAND(data["DISP"]["acc_rand"])

    def read_input_file(self):
        path = self.params.get_INPUT_PATH()
        m_zong = ZongReaderHandle(path)
        df = m_zong.input_file_handle()
        print(df)
        self.dataframe._INPUT_DF = df
        del m_zong

    def generate(self):
        print(self.params.check_params())
        if self.params.check_params():
            data_generator_instance = DataGenerationScript()
            try:
                (
                    self.dataframe._ELECT_DF,
                    self.dataframe._GRAPH_DF,
                    self.dataframe._SERVR_DF,
                    self.dataframe._KEYS,
                ) = data_generator_instance._preview_files_gets()
                print(self.dataframe._ELECT_DF)
                del data_generator_instance
            except Exception as e:
                print("Error!", e)

    def create_files(self, data):
        m_zong = ZongGenerateHandle()
        m_zong.set_json_to_API(data)
        m_zong.Generate_laser_file(
            dict_2_list(self.params.get_GRAPH_DICT()), self.dataframe._GRAPH_DF
        )
        m_zong.Generate_servr_file(
            dict_2_list(self.params.get_SERVR_DICT()), self.dataframe._SERVR_DF
        )
        m_zong.Generate_elect_file(
            dict_2_list(self.params.get_ELECT_DICT()), self.dataframe._ELECT_DF
        )


def dg_function(data: json):
    api = API()
    api.SET_ALL_FOR_API(data)
    api.read_input_file()
    api.generate()
    api.create_files(data)


app_instance = Flask(__name__)
secret_api_key = "3327bc09-53c4-11ee-ae21-8cf8c5e498b3"


@app_instance.route("/dg", methods=["POST", "GET"])
def receive_json():
    api_key = request.headers.get("X-API-Key")
    if api_key == secret_api_key:
        try:
            # Get JSON data from the request
            json_data = request.get_json()
            dg_function(json_data)

            return jsonify({"message": "OUTPUT files saved successfully."}), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"Error": "Unauthorized access."}), 401


# if __name__ == "__main__":
#    app.run(debug=True)

# =========================================#
# ==================TEST===================#
# =========================================#

# if __name__ == "__main__":
#     data = read_json("settings.json")
#     dg_function(data=data)
#     exit()
