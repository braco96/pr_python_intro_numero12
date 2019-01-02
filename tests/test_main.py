import os, io, json, math, re, importlib
import pytest
mod = importlib.import_module('main')


def test_suma():
    assert mod.suma(2,3) == 5
