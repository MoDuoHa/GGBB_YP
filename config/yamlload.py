import yaml


#读取yaml
def loadyaml(filename):
    files=open(filename,'r')
    #读取
    data=yaml.load(files,Loader=yaml.FullLoader)
    return data

# if __name__ == '__main__':
#     print(loadyaml('../data/test.yaml'))