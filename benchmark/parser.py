from __future__ import print_function

from numpy import mean

def reader(benchmark):

    with open(benchmark, 'rt') as bench:
        raw = bench.read()

    return [(data.split('\t')) for data in raw.split('\n')][0:-1]


def parsed():
    init    = dict()
    values  = reader('raw.txt')
    mapping = init.fromkeys([key for key, value in values], ())

    for value in values:

        [[mins], [secs,_]] = [i.split('s') for i in value[1].split('m')]
        [ time,   key    ] = [float(mins) * 60 + float(secs),  value[0]]

        mapping[key] += (time,)

    return mapping


def main():
    bench = parsed()

    for key,value in sorted(bench.items()):

        print(key, '{:2.2f}s\t/ {}\t{:2.2f}s'.format(
                sum(value),
                len(value),
                mean(value),
        ), sep='\t')


if __name__ == '__main__':
    main()
