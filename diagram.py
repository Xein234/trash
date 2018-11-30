def expand(diagram:str):
    assert diagram.startswith('[') and diagram.endswith(']')
    assert set(diagram[1:-1]) <= set('*01')

    stars = diagram.count('*')
    toIncert = ['{:0{}b}'.format(n, stars) for n in range(2**stars)]
    diagram = diagram.replace('*', '{}')
    return [diagram.format(*e) for e in toIncert]

if __name__ == '__main__':
    expand('[*]')
    expand('[*01*010*1]')
