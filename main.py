import math


def citire_lista():
    '''
    elementele se introduc separate prin cate un spatiu
    '''
    str_lst = input("Introduceti elementele : ")
    str_elem = str_lst.split(" ")
    result_lst = []
    for str_elem in str_elem:
        elem = float(str_elem)
        result_lst.append(elem)
    return result_lst


def get_parte_intreaga(lst):
    '''
    extrage partea inteaga dintr-un numar rational
    :param lst: o lista de numere de tip float
    :return: lista formata din partea intreaga a numerelor initiale
    '''
    result_list = []
    for element in lst:
        result_list.append(math.trunc(element))
    return result_list


def get_numere_din_interval(lst):
    '''
    formeaza o lista noua cu elementele ce apartin unui interval dat
    :param lst: lista de numere de tip float
    :return: lista noua cu elementele ce apartin unui interval dat
    '''
    inceput = float(input('Dati inceputul intervalului :'))
    sfarsit = float(input('Dati sfarsitul intervalului :'))
    result_list =[]
    for element in lst:
        if (inceput < element and sfarsit > element):
            result_list.append(element)
    return result_list


def extract_fractionar(n):
    '''
    extrage partea fractionara a unui numar
    :param n: un numar rational
    :return: partea fractionara a numarului dat
    '''
    return str(n).split('.')[1]


def test_extract_fractionar():
    assert extract_fractionar(2.1788) == '1788'
    assert extract_fractionar(14.0) == '0'
    assert extract_fractionar(159877.1) == '1'
    assert extract_fractionar(2.28) == '28'
    assert extract_fractionar(4.9876) == '9876'


def PIntreaga_divizor_pentru_PFractionara(lst):
    '''
    creeaza o lista noua formata din numere a caror parte intreaga este divizor al partii fractionale
    :param lst: lista de numere de tip float
    :return: noua lista formata
    '''
    test_extract_fractionar()
    result_list = []
    for element in lst:
        if(math.trunc(element) != element):
            if(int(extract_fractionar(element)) % math.trunc(element) == 0):
                result_list.append(element)
    return result_list


def primeste_nume(n:str):
    '''
    returneaza numele caracterului
    :param n: un caracter
    :return: un string ce reprezinta numele caracterului
    '''
    if n == '1':
        return 'unu'
    elif n == '2':
        return 'doi'
    elif n == '3':
        return 'trei'
    elif n == '4':
        return 'patru'
    elif n == '5':
        return 'cinci'
    elif n == '6':
        return 'sase'
    elif n == '7':
        return 'sapte'
    elif n == '8':
        return 'opt'
    elif n == '9':
        return 'noua'
    elif n == '0':
        return 'zero'
    elif n == '.':
        return 'virgula'


def formare_nume_numar(n):
    '''
    formeaza numele numarului n
    :param n: un numar float
    :return: un string cu numele numarului
    '''
    str_numar = str(n)
    nume = ''
    for caracter in str_numar:
        nume = nume + str(primeste_nume(caracter))
    return nume


def test_formare_nume_numar():
    assert formare_nume_numar(1.1) == 'unuvirgulaunu'
    assert formare_nume_numar(7) == 'sapte'
    assert formare_nume_numar(14) == 'unupatru'
    assert formare_nume_numar(3.12) == 'treivirgulaunudoi'


def get_numere_ca_nume(lst):
    '''
    transforma numerele unei liste in cuvinte
    :param lst: lista de numere float
    :return: lista de cuvinte
    '''
    test_formare_nume_numar()
    result_list = []
    for element in lst:
        result_list.append(formare_nume_numar(element))
    return result_list


def main():
    while True:
        print('1.Citire lista.')
        print('2.Afisarea listei formata din partea intreaga a numerelor.')
        print('3.Afisarea numerelor ce fac parte dintr-un interval dat.')
        print('4.Afisarea numerelor a caror parte intreaga este divizor al partii fractionale.')
        print('5.Afisarea numerelor in cuvinte.')
        print('x.Iesire.')
        optiune = input('Selectati optiunea : ')
        if optiune == '1':
            lista = citire_lista()
            print(lista)
        elif optiune == '2':
            print(get_parte_intreaga(lista))
        elif optiune == '3':
            print(get_numere_din_interval(lista))
        elif optiune == '4':
            print(PIntreaga_divizor_pentru_PFractionara(lista))
        elif optiune == '5':
            print(get_numere_ca_nume(lista))
        elif optiune == 'x':
            break


main()
