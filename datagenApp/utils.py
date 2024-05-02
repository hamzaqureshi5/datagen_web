import json
import requests
import json
from django.http import JsonResponse
from app.datagen.operators.zong.FileParser import ZongFileParser
from .models import (SecurityKeys,SecurityKeysRandomization, EncryptionKeys,StartingParams,TextFile, Zong_Input_Dataframe, ElectricalDataJson, GraphicalDataJson)



def read_json(file_path: str):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
    return dict(data)



def save_uploaded_file(uploaded_file):
    obj = TextFile.objects.all().delete()
    obj = TextFile.objects.create(file=uploaded_file.name)
    obj.save()

    m_zong = ZongFileParser(uploaded_file.name)
    df = m_zong.input_file_handle()
    del m_zong

    Zong_Input_Dataframe.objects.all().delete()

    instances = [Zong_Input_Dataframe(id=index, iccid=row['ICCID'], imsi=row['IMSI']) for index, row in df.iterrows()]
    Zong_Input_Dataframe.objects.bulk_create(instances)

def save_electrical_data(data):
    ElectricalDataJson.objects.all().delete()
    data_objects = [
        ElectricalDataJson(id=item['id'], parameter=item['parameter'], lclip=item['lclip'], rclip=item['rclip']) for
        item in data]
    ElectricalDataJson.objects.bulk_create(data_objects)
    return JsonResponse({"status": "success", "message": "Data saved successfully."})

def save_graphical_data(data):
    GraphicalDataJson.objects.all().delete()
    data_objects = [
        GraphicalDataJson(id=item['id'], parameter=item['parameter'], lclip=item['lclip'], rclip=item['rclip']) for
        item in data]
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


# def api_call():
#     url = "http://127.0.0.1:5551/dg1"
#     response = requests.post(
#         url,
#     )
#     data = response.json()
#     return data
