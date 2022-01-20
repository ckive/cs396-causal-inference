import argparse
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf


def observed(n=100, c_dim=6, ols="y ~ a"):
    #regressing y ~ a + c, we take into account the confounding var so we'd expect outcome to be 0.5
    #c being low makes a more likely to be 1
    c = np.random.randint(1, 1 + c_dim, n)
    a = np.random.binomial(n=1 + c_dim - c, p=0.5, size=n)
    a = (a > 0).astype(np.int32)
    #if c is low, y is also low
    y = np.random.binomial(n=a + c, p=0.5)
    df = pd.DataFrame(data=dict(c=c, a=a, y=y))
    return smf.ols(ols, data=df).fit().params['a']


def randomized(n=100, c_dim=6, ols="y ~ a"):
    c = np.random.randint(1, 1 + c_dim, n)
    #here, the relationship between c and a is cut out. a is just a single coin flip
    a = np.random.binomial(n=1, p=0.5, size=n)
    y = np.random.binomial(n=a + c, p=0.5)
    df = pd.DataFrame(data=dict(c=c, a=a, y=y))
    # would expect this to return 0.5, because we're randomly assigning based on 50/50 coin flip
    return smf.ols(ols, data=df).fit().params['a']


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("func", type=str, choices=["observed", "randomized"])
    parser.add_argument("--n", type=int, default=100)
    parser.add_argument("--c_dim", type=int, default=6)
    parser.add_argument("--ols", type=str, default="y ~ a")
    parser.add_argument("--repeats", type=int, default=1)
    args = parser.parse_args()

    np.random.seed(42)

    func = observed if args.func == "observed" else randomized
    results = [func(n=args.n, c_dim=args.c_dim, ols=args.ols)
               for i in range(args.repeats)]
    print("{:.3f} ± {:.3f}".format(np.mean(results), np.std(results)))

# print('bruh')
# a = observed()
# print(a)