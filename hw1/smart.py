from subprocess import call

NE = {
    "type": "observed",
    "method": "y ~ a + c"
}
SW = {
    "type": "randomized",
    "method": "y ~ a"
}
SE = {
    "type": "randomized",
    "method": "y ~ a + c"
}

for quad in [NE, SW, SE]:
    for r in [10, 100, 1000]:
        for dims in [10, 500]:
            print("Quad: {}, repeats: {}, dims: {}".format(quad, r, dims))
            call(["python", "lecture2demo.py", quad['type'], 
            "--repeats", str(r), "--c_dim", str(dims), "--ols", quad['method']])
