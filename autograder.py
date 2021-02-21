#!/usr/bin/python3
# -*- coding: utf-8 -*-

# grader.py
# Autograder for assignments in CS-1101
#
# Deepraj Pandey
# 18 January, 2021

import json
import subprocess as sp

from shlex import split
from termcolor import colored, cprint


def tprnt(*objs, **kwargs):
    """Wrapper print to prefix test results"""
    col = "yellow"
    if objs[0].startswith("FAIL"):
        col = "red"
    elif objs[0].startswith("PASS"):
        col = "green"
    print(colored("*" * 4 + " ", "yellow") + colored(objs[0], col))


def run(cmd, inp, print_output=False):
    """Wrapper to create a child process and run sanitised command"""
    proc = sp.Popen(
        split(cmd),
        # text=True,
        encoding="utf8",
        stdin=sp.PIPE,
        stdout=sp.PIPE,
        stderr=sp.STDOUT,
    )
    out = ""
    ret = -1
    try:
        out, err = proc.communicate(input=inp, timeout=5)
        if print_output:
            print("stdout: {}\n".format(out))
        if err:
            print("stderr: {}\n".format(err))
            print("return code: {}".format(proc.returncode))
        ret = proc.returncode
        proc.terminate()
    except sp.TimeoutExpired:
        proc.kill()
    return ret, out


config = dict()
with open("./conf.json", "r") as f:
    config = json.load(f)

cprint("Starting autograder for {}".format(config["name"]), "yellow")
cprint("=" * (24 + len(config["name"])), "yellow")

# clean dir
run("make clean", "")

max_points = 1.0
points = 0.0

for test in config["tests"]:
    expected_output = test["expected"]

    tprnt("Test: {}".format(test["name"]))

    ret, output = run(test["cmd"], test["input"])
    if ret == 0:
        if not expected_output or output == expected_output:
            points += float(test["points"])
            if config["print_output"]:
                cprint("Command Output", "yellow")
                cprint(output, "white")
            tprnt("PASS\t{}".format(test["points"]))
        else:
            tprnt("FAIL")
            print(
                colored("Your output: ", "red")
                + "{}\nExpected output: {}".format(output, expected_output)
            )
    else:
        tprnt("FAIL")
    cprint("." * 19, "yellow")

cprint("-" * 31, "yellow")
cprint(
    "Provisional Score\t" + colored("{}/{}".format(points, max_points), "green"),
    "yellow",
)
cprint("-" * 31, "yellow")
