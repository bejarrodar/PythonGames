import csv


def write_results(save:dict,game:str,file:str = "save.csv"):
    """Writes the results to file

    Args:
        save (dict): keys = 'win','lose','tie' as int
        game (str): 'rps','ttt','num','connect'
        file (str): the name of the save file to be saved
    """
    old_data = read_results(file)

    match game:
        case "rps":
            write_out = [save["win"],save["lose"],save["tie"],
                         old_data[3],old_data[4],old_data[5],
                         old_data[6],old_data[7],old_data[8],
                         old_data[9],old_data[10],old_data[11]]
        case "ttt":
            write_out = [old_data[0],old_data[1],old_data[2],
                         save["win"],save["lose"],save["tie"],
                         old_data[6],old_data[7],old_data[8],
                         old_data[9],old_data[10],old_data[11]]
        case "num":
            write_out = [old_data[0],old_data[1],old_data[2],
                         old_data[3],old_data[4],old_data[5],
                         save["win"],save["lose"],save["tie"],
                         old_data[9],old_data[10],old_data[11]]
        case "connect":
            write_out = [old_data[0],old_data[1],old_data[2],
                         old_data[3],old_data[4],old_data[5],
                         old_data[6],old_data[7],old_data[8],
                         save["win"],save["lose"],save["tie"]]

    print(write_out)
    with open(file, "wt", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(write_out)

def read_results(file: str= "save.csv") -> list:
    """reads game results from file

    Args:
        file (str): the name of the save file to be saved

    Returns:
        list: [rps wins, rps lose,rps tie, ttt win, ttt lose, ttt tie,
            num win, num lose, num tie, connect wins, connect lose, connect tie]'
    """
    save_list = []
    try:
        with open(file, "rt", encoding="utf-8") as csv_file:
            data = csv.reader(csv_file)
            for each in data:
                save_list.append(each)
            return save_list[0]
    except FileNotFoundError:
        print("File not found")
        return [0,0,0,0,0,0,0,0,0,0,0,0]
