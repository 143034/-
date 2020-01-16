import sys
sys.path.append("..")
import PATHS
path = PATHS.CONFIG_ALL_DIR + r'\Search.txt'
path1 = PATHS.CONFIG_ALL_DIR + r'\Search_Three.txt'
def get_search(paths = path):
    with open(path,'r') as f:
        se = f.read()
        f.close()
        return se


def get_search_three(paths = path1):
    with open(path1,'r') as f:
        se = f.read()
        f.close()
        return se


def get_search_icml(path = path1):
    with open(path1,'r') as f:
        se = f.read()
        if se == '2017':
            se = 'v70'
        elif se == '2019':
            se = 'v97'
        f.close()
        return se

def get_search_nips(paths = path1):
    with open(path1,'r') as f:
        result = ''
        se = f.read()
        if se == '2010':
            result = '23-' + se
        elif se == '2011':
            result = '24-' + se
        elif se == '2012':
            result = '25-' + se
        elif se == '2013':
            result = '26-' + se
        elif se == '2014':
            result = '27-' + se
        elif se == '2015':
            result = '28-' + se
        elif se == '2016':
            result = '29-' + se
        elif se == '2017':
            result = '30-' + se
        elif se == '2018':
            result = '31-' + se
        f.close()
        return result


if __name__ == '__main__':
	f = get_search_three()
	print(f)