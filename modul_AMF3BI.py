import os
import xml.etree.ElementTree as ET

class KonyvRegiszterUGYP:
    def __init__(self, filename="konyvek_AMF3BI.xml"):
        self.filename = filename
        self.konyvek = self.betolt_konyvek_amf3bi()

    def betolt_konyvek_UGYP(self):
        if not os.path.exists(self.filename):
            return []
        try:
            tree = ET.parse(self.filename)
            root = tree.getroot()
            konyv_list = []
            for item in root.findall("konyv"):
                konyv_data = {
                    "cime": item.find("cime").text,
                    "ara": int(item.find("ara").text),
                    "menny": int(item.find("menny").text)
                }
                konyv_list.append(konyv_data)
            return konyv_list
        except:
            return []

    def uj_konyv_UGYP(self, cime, ara, menny):
        if cime and ara >= 0 and menny >= 0:
            konyv_data = {"cime": cime, "ara": ara, "menny": menny}
            self.konyvek.append(konyv_data)
            root = ET.Element("library")
            for konyv in self.konyvek:
                konyv_sor = ET.SubElement(root, "konyv")
                ET.SubElement(konyv_sor, "cime").text = konyv["cime"]
                ET.SubElement(konyv_sor, "ara").text = str(konyv["ara"])
                ET.SubElement(konyv_sor, "menny").text = str(konyv["menny"])  
            tree = ET.ElementTree(root)
            tree.write(self.filename, encoding="utf-8")
            return True
        return False
   
    def mindenkonyv_UGYP(self):
        return self.konyvek
