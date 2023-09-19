import argparse
from scipy.stats import poisson

def main(mean, cutoffs):
    
    print(f'With {mean:.2f}X coverage.')
    dist = poisson(mu=mean)
    for cutoff in cutoffs:
        sf = dist.sf(cutoff)
        print(f'X>{cutoff} {sf:0.2%}')
    


suffix2mult = {'k': 1_000,
               'm': 1_000_000,
               'b': 1_000_000_000,
               'g': 1_000_000_000,
               }

def parse_suffixed_number(number):
    
    if number[-1].isalpha():
        suffix = number[-1].lower()
        mult = suffix2mult[suffix]
        return float(number[:-1])*mult
    return float(number)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Sequence depth estimator."
    )
    
    parser.add_argument("--estimated_coverage", 
                        type=int,
                        help="The estimated coverage."
    )
    parser.add_argument("--genome", 
                        type=str,
                        default='3b',
                        help="Genome size. Accepts suffixes like k, m, and b."
    )

    
    parser.add_argument("--bases", 
                        type=str,
                        help="The number of sequenced bases. Accepts suffixes like k, m, and b.")
    
    parser.add_argument("--depth",
                        nargs='+', type=int,
                        default=[0, 5, 10, 50],
                        help='The depth thresholds to evaluate')
    return parser.parse_args()


if __name__ == '__main__':
    
    args = parse_args()
    
    if args.estimated_coverage:
        estimated_coverage = args.estimated_coverage
    elif args.bases:
        
        genome_size = parse_suffixed_number(args.genome)
        bases = parse_suffixed_number(args.bases)
        estimated_coverage = bases/genome_size
        print(f'Calculated a mean coverage of {estimated_coverage:.2f}')
        
    else:
        raise AssertionError('Either --bases or --estimated_coverage must be provided.')
    
    main(estimated_coverage, args.depth)