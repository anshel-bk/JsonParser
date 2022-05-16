import json
import os

path = os.path.dirname(os.path.abspath(__file__))+"\jsons_lists" # прописываешь абсолютный путь до папки с джсонами
list_jsons = [file for file in os.listdir(path)]


def get_json_info(json_f):
    json_f = json_f
    with open('jsons_lists/' + json_f) as f:
        dicts = json.load(f)
        return dicts


def get_coords(shapes):
    coords = []
    for shape in shapes:
        coords_face_part = shape.get("points")
        coords_face_part = ' '.join([' '.join([str(coord) for coord in coords]) for coords in coords_face_part])
        coords.append(coords_face_part)
    coords = ' -0.1 '.join(coords)
    coords += " 1.0"
    return coords


def write_info(coords, image_path, count):
    with open("test_result.txt", "a+", encoding="utf-8") as result:
        try:
            result.write(image_path + "\n")
            result.write(coords + "\n")
            print(f"Запись json под номером {count} произведена успешно")
        except Exception as ex:
            print(f"Что то пошло не так в записи под номером {count}\nВозникло исключение {ex}")


def main():
    for count, json_f in enumerate(list_jsons, 1):
        print(f"Обрабатывается файл {json_f}")
        dicts = get_json_info(json_f)
        shapes = dicts.get("shapes")
        coords = get_coords(shapes)
        img_path = dicts.get("imagePath")
        write_info(coords, img_path, count)


main()
