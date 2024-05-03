import json
import requests
import json
from django.http import JsonResponse
from app.datagen.operators.zong.FileParser import ZongFileParser
from .models import (
    SecurityKeys,
    SecurityKeysRandomization,
    EncryptionKeys,
    StartingParams,
    TextFile,
    Zong_Input_Dataframe,
    ElectricalDataJson,
    GraphicalDataJson,
    ElectricalOutputData,
    GraphicalOutputData,
    ServerOutputData,
)


def read_json(file_path: str):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
    return dict(data)


def save_uploaded_file(uploaded_file):
#    obj = TextFile.objects.all().delete()
    obj = TextFile.objects.create(file=uploaded_file.name)
    obj.save()

    m_zong = ZongFileParser(uploaded_file.name)
    df = m_zong.input_file_handle()
    del m_zong

    Zong_Input_Dataframe.objects.all().delete()

    instances = [
        Zong_Input_Dataframe(id=index, iccid=row["ICCID"], imsi=row["IMSI"])
        for index, row in df.iterrows()
    ]
    Zong_Input_Dataframe.objects.bulk_create(instances)


def save_electrical_data(data):
    ElectricalDataJson.objects.all().delete()
    data_objects = [
        ElectricalDataJson(
            id=item["id"],
            parameter=item["parameter"],
            lclip=item["lclip"],
            rclip=item["rclip"],
        )
        for item in data
    ]
    ElectricalDataJson.objects.bulk_create(data_objects)
    return JsonResponse({"status": "success", "message": "Data saved successfully."})


def save_graphical_data(data):
    GraphicalDataJson.objects.all().delete()
    data_objects = [
        GraphicalDataJson(
            id=item["id"],
            parameter=item["parameter"],
            lclip=item["lclip"],
            rclip=item["rclip"],
        )
        for item in data
    ]
    GraphicalDataJson.objects.bulk_create(data_objects)
    return JsonResponse({"status": "success", "message": "Data saved successfully."})


def save_keys(request):
    op = request.POST.get("op_key_text", "")
    k4 = request.POST.get("k4_key_text", "")
    si = request.POST.get("data_size_text", "")
    iccid = request.POST.get("iccid_text", "")
    imsi = request.POST.get("imsi_text", "")
    pin1 = request.POST.get("pin1_text", "")
    puk1 = request.POST.get("puk1_text", "")
    pin2 = request.POST.get("pin2_text", "")
    puk2 = request.POST.get("puk2_text", "")
    adm1 = request.POST.get("adm1_text", "")
    adm6 = request.POST.get("adm6_text", "")

    pin1_rand = request.POST.get("pin1_rand_check", False)
    puk1_rand = request.POST.get("puk1_rand_check", False)
    pin2_rand = request.POST.get("pin2_rand_check", False)
    puk2_rand = request.POST.get("puk2_rand_check", False)
    adm1_rand = request.POST.get("adm1_rand_check", False)
    adm6_rand = request.POST.get("adm6_rand_check", False)

    SecurityKeys.objects.create(
        pin1=pin1,
        puk1=puk1,
        pin2=pin2,
        puk2=puk2,
        adm1=adm1,
        adm6=adm6,
    )

    SecurityKeysRandomization.objects.create(
        pin1_rand=pin1_rand,
        puk1_rand=puk1_rand,
        pin2_rand=pin2_rand,
        puk2_rand=puk2_rand,
        adm1_rand=adm1_rand,
        adm6_rand=adm6_rand,
    )

    EncryptionKeys.objects.create(
        k4=k4,
        op=op,
    )

    StartingParams.objects.create(
        size=si,
        iccid=iccid,
        imsi=imsi,
    )

    return {
        "K4": k4,
        "OP": op,
        "SIZE": si,
        "ICCID": iccid,
        "IMSI": imsi,
        "PIN1": pin1,
        "PIN2": pin2,
        "PUK1": puk1,
        "PUK2": puk2,
        "ADM1": adm1,
        "ADM6": adm6,
    }


default_headers = (
    "ICCID",
    "IMSI",
    "PIN1",
    "PUK1",
    "PIN2",
    "PUK2",
    "KI",
    "EKI",
    "OPC",
    "ADM1",
    "ADM6",
    "ACC",
)


import pandas as pd
from app.datagen.STCAppScriptV6 import *
from app.datagen.GlobalParams import PARAMETERS

params = PARAMETERS.get_instance()


def SET_ALL_DISP_PARAMS_SECURITY_KEYS():
    params.set_PIN1("0000")
    params.set_PUK1("00000000")
    params.set_PIN2("5555")
    params.set_PUK2("4444")
    params.set_ADM1("11111111")
    params.set_ADM6("11111111")
    params.set_ACC("0111")


def SET_ALL_DISP_PARAMS_STARTING_PARAMS():
    params.set_IMSI(999990000000400)
    params.set_ICCID(999900000000000400)
    params.set_DATA_SIZE(7)

    params.set_PRODUCTION_CHECK(True)
    params.set_ELECT_CHECK(True)
    params.set_GRAPH_CHECK(True)
    params.set_SERVER_CHECK(True)


def SET_ALL_DISP_PARAMS_DICT():
    gdict = GraphicalDataJson.get_json()
    edict = ElectricalDataJson.get_json()

    params.set_SERVER_DICT(edict)
    params.set_ELECT_DICT(edict)
    params.set_GRAPH_DICT(gdict)


def SET_ALL_DISP_PARAMS_DOCUMENT():
    params.set_INPUT_PATH("templates/N2023031016844011.txt")


def SET_ALL_DISP_PARAMS_RANDOMIZATION_CHECK():
    params.set_PIN1_RAND(False)
    params.set_PUK1_RAND(True)
    params.set_PIN2_RAND(False)
    params.set_PUK2_RAND(False)
    params.set_ADM1_RAND(False)
    params.set_ADM6_RAND(True)
    params.set_ACC_RAND(False)


def SET_ALL_DISP_PARAMS_ENCRYPTION_KEYS():
    params.set_K4("111150987DE41E9F0808193003B543296D0A01D797B511AFDAEEEAC53BC61111")
    params.set_OP("1111006F86FAD6540D86FEF24D261111")


def preview_files_gets():
    Initial_DataFrame = pd.DataFrame()
    s = DataGenerationScript()
    SET_ALL_DISP_PARAMS_DOCUMENT()
    SET_ALL_DISP_PARAMS_ENCRYPTION_KEYS()
    SET_ALL_DISP_PARAMS_SECURITY_KEYS()
    SET_ALL_DISP_PARAMS_STARTING_PARAMS()
    SET_ALL_DISP_PARAMS_RANDOMIZATION_CHECK()
    SET_ALL_DISP_PARAMS_DICT()
    Initial_DataFrame, keys_dict = s.DATA_PARSER_INITIAL(
        demo_data1=True,
        default_headers2=default_headers,
        op_4="7B980530B5F04285DB3D9AA678FADFEE",
        k4_4="77E1385B1568CDB1D7CBD668B86606786150D233874CE188B29C46DAB127440B",
        keys=True,
    )
    #    print(Initial_DataFrame)
    #    print("Keys used in this data generation attempt are : ", keys_dict)

    laser_df = pd.DataFrame()
    elect_df = pd.DataFrame()
    server_df = pd.DataFrame()
    if params.get_SERVER_CHECK() is True:
        server_df = s.DATA_PARSER_FINAL(
            params.get_SERVER_DICT(),
            Initial_DataFrame,
            clip=False,
            encoding=False,
            caption="SERVER",
        )
    if params.get_GRAPH_CHECK() is True:
        laser_df = s.DATA_PARSER_FINAL(
            params.get_GRAPH_DICT(),
            Initial_DataFrame,
            clip=True,
            encoding=False,
            caption="LASER",
        )
    if params.get_ELECT_CHECK() is True:
        elect_df = s.DATA_PARSER_FINAL(
            params.get_ELECT_DICT(),
            Initial_DataFrame,
            clip=False,
            encoding=True,
            caption="ELECT",
        )

    return elect_df, laser_df, server_df, keys_dict


def save_df_to_db(df, category: str):
    if category == "elect":
        for index, row in df.iterrows():
            row_data = df.iloc[index]
            comma_separated = ",".join(row_data.astype(str))
            record = ElectricalOutputData(row_value=comma_separated)
            record.save()
    if category == "graph":
        for index, row in df.iterrows():
            row_data = df.iloc[index]
            comma_separated = ",".join(row_data.astype(str))
            record = GraphicalOutputData(row_value=comma_separated)
            record.save()
    if category == "server":
        for index, row in df.iterrows():
            row_data = df.iloc[index]
            comma_separated = ",".join(row_data.astype(str))
            record = ServerOutputData(row_value=comma_separated)
            record.save()
