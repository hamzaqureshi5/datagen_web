import json
import requests


def read_json(file_path: str):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
    return dict(data)


url_m = "http://127.0.0.1:5551/dg"


def dg_function():
    try:
        data = read_json(
            "settings.json"
        )  # You need to define a function to read JSON from a file
        print(data)
        print("======================")
        response = requests.post(url=url_m, json=data)
        if response.status_code == 200:
            print("Request sent successfully")
        else:
            print("Error: Status Code", response.status_code)

    except Exception as e:
        print("An exception occurred:", str(e))

from .models import SecurityKeys, SecurityKeysRandomization, EncryptionKeys, StartingParams

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
