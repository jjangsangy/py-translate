# -*- coding: utf-8 -*- #

from __future__ import print_function

from numpy import mean, std

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
        [(time), (keys)  ] = [float(mins) * 60 + float(secs),  value[0]]

        mapping[keys] += (time,)

    return mapping


def main():
    bench = parsed()
    flat  = [x for l in bench.values() for x in l]
    fmt   = '{}\t{:2.2f}s\t ÷  {}\t{:2.2f}s'

    print("Code\tSum\t Runs\tMean")
    for keys,value in sorted(bench.items()):

        print(fmt.format(
             keys,
             sum(value),
             len(value),
            mean(value))
        )

    print()
    print("Total Time:\t{:2.2f}s".format(sum(flat)))
    print("Sample Size:\t{}".format(len(flat)))
    print("Average:\t{:2.2f}s".format(mean(flat)))
    print("Standard Dev:\t{:2.2f}s".format(std(flat)))


if __name__ == '__main__':
    main()
