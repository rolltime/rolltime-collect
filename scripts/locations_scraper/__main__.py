#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(dir)

from utilities.prompt_format import item
from locations_scraper.scraper import Main as ScraperMain

def Main():
  '''Wrapper.'''
  ScraperMain()


if __name__ == '__main__':
  Main()
