from __future__ import print_function

def reader(benchmark='output.txt'):

    with open(benchmark, 'rt') as bench:
        raw = bench.read()

    return [(data.split('\t')) for data in raw.split('\n')][0:-1]


def parsed():
    init    = dict()
    values  = reader()
    mapping = init.fromkeys([key for key, value in values], ())

    for value in values:

        [[mins], [secs,_]] = [i.split('s') for i in value[1].split('m')]
        [ time,   key    ] = [float(mins) * 60 + float(secs),  value[0]]

        mapping[key] += (time,)

    return mapping


def main():
    bench = parsed()

    for k,v in sorted(bench.items()):
        print(k, list(v), sep='\t')


if __name__ == '__main__':
    main()
