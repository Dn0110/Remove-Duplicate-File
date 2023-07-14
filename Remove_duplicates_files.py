"""Remove Arquivos Duplicados"""

import os
import hashlib


path = 'C:\\Users\\anymo\\Desktop\\RECOVER\\Dados_Recupearados\\png\\'
extension = '.jpg', '.JPG', '.png', '.PNG'
details = {}
name_copy = []
siz = []
hash_rm_duplicate = {}
verification = 3


def get_info_files(path):
    print('=' * 25)
    print("[!]:Identifying files...")
    for filename in os.listdir(path):
        # print(filename)
        z = os.path.getsize(path + filename)
        details[filename] = z
        if 'Copia' in filename or 'copia' in filename or 'Copy' in filename or 'copy' in filename:
            name_copy.append(filename)
        siz.append(z)

        if filename.endswith(extension):
            fullpath = os.path.abspath(os.path.join(path, filename))
            with open(fullpath, 'rb') as f:
                md5sum = hashlib.md5(f.read()).hexdigest()
                hash_rm_duplicate[md5sum] = filename
    print('=' * 25)


def action_1():
    # LÓGICA FUNCIONANDO CORRETAMENTE, FALTA TRATAR ERROS.
    global verification
    verification -= 1
    try:
        if len(name_copy) > 0:
            print("[!]:Files identified with names of copies")
            x = input('Do you want remove files with names of copy? [y/n] ')
            if x.isalpha() and len(x) == 1:
                if x == 'y' or x == 'Y':
                    print()
                    for filename in name_copy:
                        print(filename)
                    print("\nTotal files with names of copies:", len(name_copy))
                    x1 = input('Are you sure? [Y/n] ')
                    if x1.isalpha() and len(x1) == 1:
                        if x1 == 'y' or x == 'Y':
                            print("\n[*]:Removing files")
                            for f in name_copy:
                                os.remove(path + f)
                            print("[!]:Finished")

                        elif x1 == 'n' or x1 == 'N':
                            print('Ok, next...')
                    else:
                        print('chose to Y or N')
                elif x == 'n' or x == 'N':
                    print('Ok, next...')
            else:
                print('chose to Y or N')
        else:
            print("\n[!]:Don't have files with name of copys this directory")
    except Exception as e:
        print('Error... action_1', e)


def action_2():
    # Size Check
    global verification
    verification -= 1


def action_3():
    # DESENVOLVENDO... Hash Check
    global verification
    verification -= 1
    print("[!]:Identifying HASH of files...\n")
    # print('---' * 10, 'HASH', '---' * 10)
    # print(hash_rm_duplicate)
    # print('---' * 22)
    total_f = []
    total_f_dup = []
    try:

        for x in os.listdir(path):
            total_f.append(x)

        for x in total_f:
            if x not in hash_rm_duplicate.values():
                total_f_dup.append(x)
                print(path + x)
        print('\n[!]:Total duplicate files:', len(total_f_dup))

        if len(total_f_dup) > 0:
            x = input("You're want to remove duplicate files? [y/n] ")
            if x.isalpha() and len(x) == 1 and x == 'y' or x == 'Y':
                x1 = input("Are you sure? [y/n] ")
                if x1.isalpha() and len(x1) == 1 and x1 == 'y' or x1 == 'Y':
                    print("\n[*]:Removing files")
                    for f in total_f_dup:
                        os.remove(path + f)

                    print("[!]:Finished")

                elif x1 == 'n' or x1 == 'N':
                    print('To the next...')
                else:
                    print('Chosen to Y or N')
            elif x == 'n' or x == 'N':
                print('To the next...')
            else:
                print('Chosen to Y or N')
        else:
            print("[!]:Don't have duplicate files this directory")
    except Exception as e:
        print('Erro... action 3', e)


if __name__ == '__main__':
    try:
        get_info_files(path)
        action_1()
        print('*---------------------------------*')
        action_3()
    except KeyboardInterrupt:
        print('\nCtrl + C')
        exit(0)
    except Exception as e:
        print('Erro... Program', e)