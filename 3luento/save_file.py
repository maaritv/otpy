import os

def check_path(path_str):
  print(len(path_str))
  if (path_str[0]=="/"):
    raise ValueError("Et voi luoda tiedostoa koneen juureen. Anna suhteellinen polku.")

def validate_not_empty(str):
  if (len(path_str)==0):
    raise ValueError("Polun pitää olla pidempi kuin 0")

def save_data_to_file(pathstr, data):
  with open(pathstr, "w", encoding="utf-8") as f:
  # Jos data ei ole merkkijono, muunnetaan se
    if not isinstance(data, str):
      data = str(data)
    f.write(data)

def check_data(data):
    print("Tämä tarkastus sisältää tarvittaessa sovelluskohtaista logiikkaa. Vaikkapa, että ei saa sisältää tiettyjä sanoja tai merkkejä.")

def file_exists(path):
    return os.path.exists(path)

path_str=input(f"Anna polku")
check_path(path_str)
data=input("anna data, joka pitää kirjoittaa tiedostoon")
validate_not_empty(data)
check_data(data)
path_str=f"{path_str}/myfile.txt"
if (file_exists(path_str)):
    print("Tiedosto on jo olemassa. Haluatko korvata sen? (k/e)")
    answer=input()
    if (answer=="k"):
        save_data_to_file(path_str, data)
    else:
        print("Tiedoston tallennus peruutettu.")
save_data_to_file(path_str, data)