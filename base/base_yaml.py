import  yaml
def yaml_data_with_file(file_name):

    with open("./data/"+file_name+".yaml","r") as f:
        data=yaml.load(f)
        return data