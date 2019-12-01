'''
grabs album covers from Itunes using API and CoverPy library
using list of album names in format: ### - Artist - Album

run as: python get_albums.py txt_file directory_name
e.g. : python get_albums.py 50s.txt 50s
'''


import coverpy
import urllib.request
import sys

def pull_cover(name1,size,index,dir):
    #import coverpy
    #import urllib.request

    # Instance CoverPy
    cp = coverpy.CoverPy()
    # Set a limit. There is a default (1), but I set it manually to showcase usage.
    limit = 1

    try:
        result = cp.get_cover(name1, limit)
        # Set a size for the artwork (first parameter) and get the result url.
        print(result.name)
        #print(result.artwork(size))
        id = dir + '/image' + str(index) + '.jpg'
        urllib.request.urlretrieve(result.artwork(size), id)
    #except cp.exceptions.NoResultsException:
    #except requests.exceptions.HTTPError:
    #    print("Could not execute GET request")

    except:
        print("Nothing found.")
        print(name1)

#pull_cover("Ok Computer", 500, 2332423, '60s')




i = 0
file_name = sys.argv[1]
dir_name = sys.argv[2]
with open(dir_name + '/' + file_name,'r+') as file:
    for line in file:
        i += 1
        line = line.rstrip()
        kw = line.split('-')
        if len(kw) >= 3:
            pull_cover(kw[1] + kw[2], 64, i, dir_name)
        else:
            pass
